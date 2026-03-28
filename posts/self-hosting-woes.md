---
title: The Woes of self-hosting
date: 03-28-2026
---

I guess I should have realized that this self-administration stuff would
be more of a pain in the ass than just running a site "the normal way".

I think I mentioned this in my first post, but I decided to run this thing
using Flask and Caddy, a stack that I am moderately familiar with, partially
as a way to feel like I owned something on the internet again, and partially
to give me some easy shortcuts.

Caddy is ridiculously convenient as a webserver; with approximately 5 lines
of very simple configuration and a valid DNS record pointing to it, Caddy can
(and does!) automatically contact LetsEncrypt and get you a valid TLS cert.
This is _wildly_ different from how it was back in ye olden days. Even when
LetsEncrypt existed but something like Caddy didn't really, the process of
actually getting a cert for an SSL-secured website was fucking _onerous_.
My first job had an internal CA that we all used for intranet projects, and
it was such a pain in the ass to create a certificate request, submit it
correctly, install the certificate into NGINX (the "world's most popular
web server" at the time[^1]), and get your site up and running. That process
alone was easily half a day of work if you hadn't done it before, and still
an hour-plus of tedium if you had. I finally broke down and wrote a shell
script to do it for me after cert four or five, and I guess today you could
just bully Claude into doing it for you, but _still_. What a pain in the ass.

Nowadays, you just boot up Caddy and voila! Secure site! That is, so long
as you read the fucking documentation:

> The data directory must not be treated as a cache. Its contents are not
> ephemeral or merely for the sake of performance. Caddy stores TLS
> certificates, private keys, OCSP staples, and other necessary information to
> the data directory. It should not be purged without an understanding of the
> implications.

Yeah...guess who forgot to mount _that_ directory in their docker container.
So of course, I'm setting up this site and all its infra, and everything
is going swimmingly until I reboot the proxy a few times, and all of a sudden
TLS stops working. Because LetsEncrypt (quite reasonably) has a limit on how
many certificates you can request for the same domain/IP before it assumes
you're doing something wrong or stupid and puts you in a **2 day long** timeout.

So...this is a roundabout way of saying my site was down for 2 days because
I got trigger happy with rebooting the docker container.

....Oops.

---

[^1]: I have no idea if this is still the case, but it always felt goofy
      to see that written out, and I'm going to assume it's still goofy
      marketing fluff.
