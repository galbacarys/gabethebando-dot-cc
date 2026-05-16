---
title: 'The Woes of self-hosting, part two: Electric backup scripts'
date: 04/19/2026
---

I logged into the server that hosts this site today to do some maintenance, and
it said it needed a reboot. Okay, cool, thought I. I `sudo apt upgrade`d,
everything looked good, I read over my reboot script to ensure everything would
be fine, and I rebooted.

Well, dear reader, you might notice that the page counter at the bottom of the
page has been reset. There's a reason for this: _I wasn't running sqlite backups
the entire time the site has been running_.

Peeling back the curtain, this site is Flask for the pages you see, Sqlite for
storage (mostly just the counters on the bottoms of pages for now, but more is
coming soon), Litestream to back up the Sqlite database to DigitalOcean spaces,
Caddy to serve everything, Docker to orchestrate, and DigitalOcean as a host. It
turns out that my launch scripts were using the `.env` file in each repo I have
for different parts of this stack, _not_ the central `.env` I have in my scripts
directory that handles turning off test (i.e. don't back up to Litestream) mode.

So...for the last 2 weeks, this site has had Litestream installed in the app
container, doing _nothing_, and when I rebooted I lost all that sweet sweet
counter data.

## Why we subject ourselves to this shit

A lot of folks on the indie web use web hosts like neocities, etc. to host their
shit, and very reasonably. They use other peoples' guestbook services and
whatnots to add dynamicity to their sites. And they are happy and productive and
make beautiful things, far more beautiful than I could ever make.

And instead of all of that, I host all my shit on one creaky digitalocean box
that I hand-maintain. Its raw IP address is just...there. You could try to SSH
into it if you wanted I guess, there's no firewall rule stopping you (and folks
do - the ssh logs are fun to read sometimes). Something about doing it all
myself feels more raw, more personal, and more real, even though it's a
_massive_ pain in the ass most of the time. And it makes the indie web feel just
a bit cozier for me. I have no ill will or harsh feelings for the folks who take
the "easy" way out here (it's not even easy - it takes _work_ to make a good
website and I applaud folks who make prettier shit than I ever could). I guess I
just...want to own it. It feels good to own it. It feels like how I remember
computers felt as a kid.
