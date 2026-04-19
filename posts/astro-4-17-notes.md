---
title: 'Astrophotography Session: 4-17-26, Shawnee State Park' 
draft: true
date: 04/19/2026 
---

I am often guilty of trying to change too much at once whenever I'm doing
something difficult. The moment I find any modicum of success, I start trying
to push the envelope. This is often a good thing, or at least not terribly
harmful, but this past weekend I pushed too far and ended up with an
_absolutely shit_ night of astrophotography. I have exactly zero astro shots to
show for all the work I did, but the process is at least interesting enough to
write about, so I'll try and salvage something from this godawful night by
making _content_ about it.

## Alt/Az steppers

![Altitude adjuster](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/000-alt-adjuster.jpg)

![Azimuth adjuster](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/001-az-adjuster.jpg)

The OpenAstroTech project has really innovated in the Astrophotography
community by introducing a feature usually only available on extremely
expensive equipment: Automatic Polar Alignment, or AutoPA. The basic idea here
is that we can use extra adjustment axes to move the whole astrophotography
setup (mount, camera, and all) up/down/left/right to ensure you're perfectly
aligned with the North celestial pole (roughly speaking, this is the star
Polaris, although technically the celestial pole is actually not quite at
Polaris but just down and to the left of it[^1]). This theoretically means
that setting up your rig should be _much_ easier.

Note the word "theoretically". It will come back later.

Getting to a working AutoPA setup was seemingly pretty simple: two more stepper
motors, some extra 3D printed parts and pulleys and belts, and we'd be off to
the races.  The basic theory of operation here is similarly simple, too: the 
whole mount is put on top of a pivot point in the rear and two roller bearings
in the front. The Altitude stepper is connected to a reduction gearbox and
pushes the rear of the mount up or down to change the angle of the central axis
of the mount, and the front of the mount is pulled left and right by the Azimuth
stepper, which has a teethed pulley against a belt strung across the front of
the mount's base. However, assembling the AutoPA system came with some really
seriously annoying issues, many owing to the purchasing of these parts on
Aliexpress since trying to ask Amazon for anything mechanical will only result
in sadness.

Just to name a few:
- the shaft for the reduction gearbox was both too long and not uniformly the
  advertised 5mm diameter. This little motherfucker gave me so much stress:
  the driveshaft for the Altitude stepper had to have two bearings, a worm gear,
  and a pulley fitted on to it, and I had to literally hammer them into place by
  holding the bearings with vise grips, putting the shaft into a metal jig I
  rigged up, and hammering on the vise grips until the bearing got to the right
  place. What a massive pain in the ass.
- The stepper motors came with connectors which used a different pitch (spacing
  between the pins) than the board they were supposed to plug into, which meant
  I couldn't connect them to power. I ordered new cables (from Amazon so they'd
  arrive quickly) and the new cables were wired incorrectly! I ended up having
  to carefully take the connectors apart using a sharp pin to push the lock tab,
  reordering the wires, and reassembling them, and I ended up with the motors
  having their polarities flipped so they run the wrong direction. At least
  _that_ was something I could fix in software.
- The cheap 5V-12V converter I was using to power this rig before didn't put
  out enough power, causing the whole thing to spazz out whenever I tried to
  move either of the new motors. This ended up being another Amazon purchase to
  fix.

I spent three nights working on this, and only managed to get it working two
nights before we were meant to leave. So, let's call this an inauspicious start.

## 

[^1]: This is kind of a fascinating phenomenon: since the Earth is effectively
    just a giant-ass gyroscope, it processes over time. So, even though for
    thousands of years we've used Polaris as our North Star because it's a
    bright and easy to locate star that is near our celestial North pole, it's
    actually slowly getting worse and less accurate over time as the Earth
    processes. Eventually, it will no longer be close enough to the CNP that we
    can even use it at all.
