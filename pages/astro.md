--- 
title: Astrophotography 
titlebar: true
---

![My current rig](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/current-rig.jpg)

This is my current Astrophotography Rig. It looks like a bit of a mess, but
allow me to try to explain what's happening here.

## Introduction to Astrophotography

OK, so what is Astrophotography? Obviously, yes, camera take picture of space
much wow. But like, _how_ does one do that?

I am learning "deep sky" astrophotography, that is, taking pictures of nebulae,
galaxies, etc. In order to do that effectively, you have to take _lots_ of
images of the same object. And ideally, these images should be very long
exposure time. You need a bunch of images because camera sensors in dark places
are "noisy". You've seen this if you've ever tried to take a phone camera
picture at a concert or indoors; that randomly colored "snow" or "grain" is the
random noise of your environment affecting your camera sensor. We use lots of
images of the same object in order to help us average out the noise and get
only the best possible data to compose our final shot with. We also want long
exposure times because camera sensors take a certain minimum amount of light to
"activate", and the longer we keep the shutter open, the more light they can
collect from the very faint objects we're photographing. In theory this should
be incredibly simple to do, just point your camera at the sky, open the
shutter, and wait. However, there is a physical reality we have to deal with
that makes astrophotography way more difficult: the rotation of the Earth.

### Goddammit, the Earth MOVES!?

Yeah, this single issue is what makes Astrophotography such a massive pain in
the ass (they said, lovingly). The Earth goes through a full day/night cycle
every 24[^1] hours, and a rotation is 360&deg;, so doing the math, the night
sky shifts 15&deg; per hour, or 1/4&deg; per minute. We have to make our camera
move at _exactly_ the same speed, arcing across the sky to match the rotation
of the Earth. That way, we stay fixed on one patch of sky the whole night.
Worse than that, in fact, we have to take into account the fact that we (almost
certainly) aren't at the equator, which means we have to ensure our camera
rotates along an arc that is perpendicular to the North Pole. This way, our arc
of rotation perfectly counteracts the motion of the Earth. In order to do this,
we use a special piece of hardware called an _equatorial mount_.

## Equatorial Mounts

Equatorial Mounts do the math and movement described above; they are calibrated
to track the Earth over the course of the night, and when properly calibrated
allow extremely long exposure times, up to multiple minutes at a time.

The particular mount I'm using right now is called the [OpenAstroTracker](https://wiki.openastrotech.com/OpenAstroTracker),
an _absolutely fabulous_ open source project that has served me very well
getting started in this hobby. It's almost fully 3d-printed, which I find
incredibly impressive (there is some seriously cool 3d print engineering
happening here), and it's been a hell of a lot of fun to get up and running.

<!--TODO(bando): replace with an image of my kit -->
![OpenAstroTracker, image courtesy wiki.openastrotech.com](https://wiki.openastrotech.com/alu-oat.jpg)

The big wheel turning left and right in the above image is the _Right
Ascension_[^2], or rotation tracking, wheel. It's the one that's calibrated to
turn to match the rotation of the Earth. The camera is mounted on a
_Declination_ assembly, which tilts it up and down to track a particular
distance away from the North Pole. This is, as it turns out, enough to
track every position in the night sky.

### But...why not uppy-downy-sidey-sidey mounts?

This was, in fact, my first question upon embarking on my astrophotography
journey. Why can't we just put the camera on a 2 dimensional pivot and move
both the uppy-downy and the sidey-sidey gradually in order to accomplish the
same movement?

The answer is...you _can_, kind of. This is what's known in the astronomy world
as an altitude-azimuth (AltAz) mount, which does what it says: you can change
the altitude (uppy-downies) or azimuth (sidey-sideys) to point to anywhere
in the sky. However, this has three serious drawbacks for astrophotography
specifically:

1. Because these coordinates are relative to your position on the ground and
   not the sky, a star's position does _not_ stay fixed throughout the night.
   Its altitude and azimuth change constantly. Now, you can of course do some
   relatively simple math to calculate from one coordinate system to another,
   but as I'm a software engineer I'm legally required to be bad at math with
   decimal points and so I don't want to do that.

2. Moving two motors in coordination with each other is _much_ harder to calibrate
   than moving just one. Both motors have to move perfectly in concert with one
   another in order to ensure you stay fixed on your position, and with cheap
   AliExpress stepper motors this is very difficult to accomplish.

3. _Rotation_. This is the big problem, actually; an equatorial mount ensures
   that your camera's rotation relative to the sky doesn't change throughout
   your camera exposure since you are tracking with the sky's rotation. However,
   with an AltAz mount you are guaranteed star trails at longer exposures even
   with perfect tracking unless you also rotate your camera over time to compensate
   for the shift in the camera's framing over time. This is a bit hard to visualize
   but trust me, this is in fact the problem. You can adjust for this with a rotator,
   that is, another motor that adjusts your camera's rotation, but then you're
   dealing with a _third_ motor to coordinate and problem (2) becomes even worse.

## Guiding

Another thing you might notice about the picture of the mount above is the big ol'
tube underneath where the camera goes. That's called the _guider scope_, and it's
literally just a super high magnification telescope with a tiny camera sensor. Its
job is to, when we're taking long exposures, track the position of one star and
ensure that star stays perfectly fixed in place by sending tiny micro-adjustments to
the mount. It doesn't help in the imaging process directly, but it does ensure that we
are dead-on accurate when keeping the camera's shutter open for very long periods of time.

On this rig, the guide scope is the OpenAstroGuider, made by the same wonderful folks
as the OpenAstroTracker at large. It's got a tiny but quite sensitive Sony IMX290 sensor
in it, and a cheap shitty doublet lens I bought on AliExpress. Did you know AliExpress
is where great astrophotography equipment comes from? Yeah me either before I started this
rabbit hole.

## Taking pictures

OK, so now we have our camera attached to a thing that can reliably track the sky.
What next?

_We gotta take some pictures_, of course!

The way I do this is using my laptop (seen in the foreground of the shitty picture
at the top of this article). My laptop runs a piece of software called [N.I.N.A.](https://nighttime-imaging.eu/),
which stands for Nighttime Imaging 'n' Astronomy (lol). It's an open source observatory
control software and it lets me do the following:

- Calibrate my mount to ensure we're circling around the North Star correctly
- Control my camera, instructing it to take test shots to ensure we're focused and framed
  exactly right for the target we're photographing, and then running the photographing
  session
- orchestrate the hardware of the mount, the guide scope, and potentially other stuff
  in the future (like a fucking DOME to cover my equipment!?)

When this project bills itself as observatory control software, it isn't kidding; it
supports everything from dinky hardware like my camera and mount all the way up to full
on multimillion dollar commercial observatories and everything in between. It's _wild_
that this kind of power is both open source and readily available these days.

To get great astrophotography shots, we have to capture four kinds of images:

- "Lights", which represent the actual light data we care about. This is the images
  of the stars, galaxies, nebulae, etc.
- "Flats", which help create a model of the optical imperfections in your camera's 
  "imaging train" (astro nerd speak for the path light travels to get to the sensor).
  A flat image is taken by putting a light panel that shines uniform brightness over
  the end of your camera lens, with the shutter speed set so that the light captured
  has the equivalent energy of roughly a "middle grey" (50% power, also known as 18% gray).
  N.I.N.A. thankfully has a wizard that does this for you. You need 10+ of these, I try
  to take 20 or so though. Keep in mind, flats need to be captured with the exact focus
  as your lights so that we can ensure we correct any optical distortion in your final
  image, like vignetting, dust on the sensor, uneven brightness, etc.
- "Darks", which are used in calibrating the camera's response to darkness. Darks are
  super useful because they allow us to figure out what our camera's noise floor is,
  which we can use later to help get us a sharper image. To capture a dark, you literally
  just take several (usually 10ish) shots of your camera at the exact focal length and
  aperture and shutter and everything, but with the lens cap on. This gives you data on
  your camera's performance in darkness.
- "Biases", which are used in calibrating the camera's internal electrical noise. Biases
  are taken at your camera's shortest shutter speed with the lens cap on, and measure how
  much noise from your darks is attributable to just the processing your camera does, as
  opposed to the sensor itself. You usually take 10 or so of these as well.

Some day when I have some more time and energy, I'll write up some info on how this is
actually processed into a final image, but in the meantime...that's it! That's basic
astrophotography.

## Rig specifications

- **Mount**: OpenAstroTracker v3, no automatic polar alignment (yet)
- **Camera**: Canon 60D, unmodified, usually with an EF 100-400mm L IS II or EF 100mm Macro
- **Computer**: HP Victus something or other with 32 GB of RAM and an NVidia RTX 5060 Laptop GPU
- **Camping Chair**: REI, baby

---

[^1]: It's actually even slightly more annoying than this; for astronomy what
      we care about _Sidereal time_, which is the amount of time it takes for the
      Earth to rotate in place back to the same position relative to the stars.
      Since the Earth is rotating _both_ around its own axis and around the sun,
      a Sidereal day is actually 23 hours, 56 minutes, and 4.1 seconds. This is
      way too complicated to use for the math in this post, so we're going to
      pretend we aren't dealing with Earth's orbit.

[^2]: This coordinate system is complex enough that I don't particularly feel
      like explaining it here. If you want more detail, This [Sky And
      Telescope](https://skyandtelescope.org/astronomy-resources/right-ascension-declination-celestial-coordinates/)
    article is a pretty good resource for understanding it.
