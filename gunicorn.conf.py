import atexit
import subprocess
import os


def on_starting(server):
    restore_proc = subprocess.run(
        [
            "litestream",
            "restore",
            "-o",
            "db.sqlite3",
            f"s3://{os.environ['SPACE_NAME']}.nyc3.digitaloceanspaces.com/db",
        ]
    )
    if restore_proc.returncode != 0:
        raise Exception("Could not restore litestream db, check logs")

    # Write a global app secret to tmp fo usage by workers
    with open('/tmp/ephemeral-app-secret', 'w') as f:
        f.write(str(os.urandom(24)))
        print("Wrote ephemeral secret")

    if os.getenv('TEST') is not None:
        return # don't turn on litestream!!
    monitor_proc = subprocess.Popen(
        [
            "litestream",
            "replicate",
            "db.sqlite3",
            f"s3://{os.environ['SPACE_NAME']}.nyc3.digitaloceanspaces.com/db",
        ]
    )
    
    atexit.register(lambda: monitor_proc.terminate())
