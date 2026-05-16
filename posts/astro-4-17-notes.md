---
title: 'Astrophotography Session: 4-17-26, Shawnee State Park' 
date: 04/20/2026 
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
  fix: a new battery bank and a USB-C to 12V barrel jack (the most cursed cable
  to ever exist).

I spent three nights working on this, and only managed to get it working two
nights before we were meant to leave. So, let's call this an inauspicious start.

## Setup at Shawnee State Park

![Setup at the park](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/002-setup.jpg)

Things actually went relatively smoothly here. Putting everything together went
super well, and I was up and running within about 25 minutes which is
shockingly fast for me. The process here is (relatively) simple:

1. Set up the shitty little fold up camping table I use as a base
2. Put the Alt-Az base on the table, pointed roughly North[^2]
3. Put the RA-Dec cage (the round bit from the picture in my [Astrophotography](/page/astrophotography)
   overview page) onto the Alt-Az base, balancing the cage on the
   rollers and rear pivot and threading the belt through.
4. Tension the RA and Dec motors against their belts, tightening them
   in place with a hex key.
5. Install the camera onto the ArcaSwiss Plate, and mount the plate onto
   the base inside the RA-Dec cage
6. Hook up all the cables, including a power cable to the Alt-Az base which
   contains the stepper drivers, the stepper motor cable for the DEC axis,
   and USB cables galore.

The weather looked pretty good, and I was feeling really good about my chances
for great results.

![Weather forecast](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/weather.jpg)

The goals for the evening were pretty simple:

- Test out the automatic polar alignment
- Test out autofocus (a feature of NINA I didn't know existed - use the autofocus
  driver _inside your camera lens!_)
- Image M81 and M82: Bode's galaxy, a beautiful Grand Design Spiral Galaxy, and
  the Cigar Galaxy, a fascinating irregular "starburst" that is oriented so that we
  see it from the side.

## The trouble begins

Almost immediately, things began to go wrong.

Autofocus was the first victim of my bad luck. The general principle is simple here: hand-focus
so that you're kinda close, then let the autofocus algorithm take over. It moves the focus way
out and then slowly in, a few steps at a time, taking a picture each time and measuring the average
"width" of each star in pixels. NINA plots these widths on a graph, takes a hyperbolic regression,
and the trough of the star width is your focus point. Simple enough, small stars = in focus stars.

I could not, for the life of me, get it to focus. The readings bounced all over the place, and the
regression never got good enough that NINA could confidently pick a focus point. And besides, it
seemed to be skipping over the obviously correct focus point over and over. I decided to hand-focus
with a Bahtinov mask (a neat little tool for manual focusing that's too interesting to leave as a 
footnote in this post) and move on.

And so I started doing some quick test images, and I was getting star trails (i.e., stars smeared
on a line). This was very, very bad news.

There are only a few things that can cause star trails in an astro image:
- Severely incorrect polar alignment
- Your Right Ascension axis moving the wrong way or being very miscalibrated
- Overlong exposures with inaccurate tracking

The trouble was, I was getting star trails with _one second_ images. This is a nightmare scenario:
somehow my mount had completely knocked itself out of whack and was tracking so inaccurately that
I was getting absolute garbage out of it. I began to panic.

## Foreshadowing is a literary technique in which...

So...I pointed my mount the _wrong fucking direction_. Somehow, instead of pointing to the North,
which is 100% required, I pointed it _straight West_. I had checked my direction on Google maps
and using a compass app, and somehow ended up in the wrong direction entirely.

I finally realized the error of my ways when I decided to start over, because I didn't know what
else to do. I pulled out my compass app again, and realized I was facing straight towards the West.
I quickly turned my mount around and instantly got pinpoint stars again.

Goddammit.

The bad news was that I had wasted an entire hour debugging this, and I was now definitely not going
to get enough data to make great images of M81 and M82 before I got too tired, but the good news
was that I could keep going down my list of stuff to try.

## AutoPA is an automatic Pain in the Ass

AutoPA didn't fucking work.

Well, that's not true. It _did_ work, but it took a _long_ fucking time to work. I found out later
that the steppers I had ordered from $sketchy-guy-on-amazon were 1.8 degree steppers, not .9 degree
steppers, and so the mount was moving the Alt and Az axes almost twice what it was supposed to. So
AutoPA, which in all the YouTube videos I had seen of it was a 2 minute process, ended up taking nearly
half an hour. And the Altitude adjustment squealed like a pig every time it had to move. It was 
so loud I think I scared the random people who pulled up in this parking lot with this screaming
contraption with wires sticking out of every end and an increasingly angry nerd with a laptop.

So here's what I learned _reading the fucking firmware code_ the next day:
- AutoPA figures out how much it needs to adjust, e.g. 36'15" to the right and 25'20" down. It then
  moves _90%_ of the distance it estimated. This is intentional as it prevents crossing the midpoint
  and ensures all our movements are in the same direction. This avoids "slop", or play caused by
  the stepper motors switching directions due to the width difference between a tooth on the pulley
  and a tooth on the belt.
- Due to my stepper motor mismatching, my steppers were moving double what they intended to, so 
  instead of moving 90% of the distance, they moved ~180% of the distance, or 90% of the way to
  the other side, ending up only 10% closer instead of 90% closer.

![AutoPA in action...sort of](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/003-polar-align.jpg)

So...AutoPA _did_ work. But it took so long that I could have done it myself faster. This was
a huge disappointment.

## And then things fell apart

...literally.

![Shit's broke](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/004-broken.jpg)

That's a loose bolt.

I finally had my polar alignment, I was finally focused, and...the mount literally fell apart.
I suspect this bolt got loose (or maybe was never fully tightened) due to the higher weight
I've been putting on the mount with the addition of my fancy new 100-400mm Canon bazooka lens.

Sigh. This came apart the moment I tried to train my lens at M81/M82, and I gave up. I packed
up and went home.

I took zero pictures. I learned a lot. I cried a little bit. It'll be better next time.

[^1]: This is kind of a fascinating phenomenon: since the Earth is effectively
    just a giant-ass gyroscope, it processes over time. So, even though for
    thousands of years we've used Polaris as our North Star because it's a
    bright and easy to locate star that is near our celestial North pole, it's
    actually slowly getting worse and less accurate over time as the Earth
    processes. Eventually, it will no longer be close enough to the CNP that we
    can even use it at all.

[^2]: Foreshadowing is a literary technique in which a small, relevant piece of
    information is revealed early in the story to hint at what may be coming
    later.
