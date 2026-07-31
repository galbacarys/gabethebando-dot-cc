# gabethebando dot cc, my personal site

This is the code the powers https://gabethebando.cc, my personal website. It is
decidedly not fancy and quite bespoke, but I think it's neat and so I figured I
would make it available to the internet for y'all to poke at it.

The site is powered by sqlite and python, using litestream to continuously back
up the SQLite database to DigitalOcean Spaces, an S3-compatible storage product.
The site is designed to run on DigitalOcean but could probably be adapted to run
on another cloud provider without much work. But then you'd have to deal with
the mild esoteric-ness of the rest of the codebase, so I guess that's a you
problem.

## Deploying this

Don't. I have a pile of shell scripts that I use to build the docker container
and deploy it, as well as a Caddy proxy configuration to make HTTPS and routing
work, but I'm not inclined to publish those because they're messy and bad. Just
admire the creaky but somehow still breathing blog before you.
