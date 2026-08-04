---
title: "Astrophotography, 7-29-26: M92, The Hercules Cluster"
date: 07-31-2026
---

![M92, the Globular cluster in Hercules](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/m92-cincy-7-29.jpg)

M92, the Globular Cluster in Hercules. This cluster is about 26,000 light years
(152 quadrillion miles!) away and has a mass of roughly 330,000 suns. Given its
chemical composition we can place its age at around 11 billion years old, only
a little younger than our galaxy as a whole.

Globular clusters are incredibly cool - they represent the end of star
formation in a region of space. Once you run out of stuff to make new stars
with, you're left with a slowly rotating cluster of tightly packed stars. These
stars are locked gravitationally and most will never leave the close proximity
they share with the other stars. The night sky must be _spectacular_ inside one
of these: a hundred thousand bright stars all around you, many as close
together as our sun is from Neptune. 

While not as visually spectacular as the brightly-colored nebulae in the night
sky, globular clusters are a cosmic time capsule; they contain mature stars
with chemical compositions that give us a very precise idea of exactly how old
they are. Because they are essentially "out of gas" to make new stars, we can
use this information to determine how old their region of the galaxy is, and
extrapolate backwards to the age of our galaxy, and our Universe as a whole.

## Capture information

- 85x60s exposures (85 mins total/120 minutes captured - 35 minutes of data
  discarded due to focus issues 🫠)
- Stacked in Siril, stretched and de-noised with GraXPert
- Denoising, photometric color calibration and desaturation applied
- Canon 60d (unmodified), Canon EF 100-400L Lens at 400mm, f/6.3, clip-in light
  pollution filter in front of camera sensor
- OpenAstroTracker with AutoPA and OpenAstroGuider upgrades
- NINA control software

All software and hardware used to capture this image is completely open source.

I had some really good stuff happen during this session: I am (almost) fully
automating my rig these days using the [NINA Advanced
Sequencer](https://nighttime-imaging.eu/docs/master/site/sequencer/advanced/advanced/).
This is a _super_ cool feature of NINA that isn't really matched by any other
observatory control software I know of; it's essentially a highly customizable
DAG workflow definition that allows you to define all the steps your observation
session should take. With some tinkering (including setting up a custom horizon
for my front balcony and defining some variables using the Sequencer+ plugin by
Carl Björk) I can set my rig up on the front balcony of my house while it's
still light out on an extension cord, and then control the entire setup using
[Touch-N-Stars](https://github.com/Touch-N-Stars/Touch-N-Stars) from my iPad.

At this point, my setup looks something like this:

- Startup sequence:
    - Initialize all the hardware (Camera, Lens, Lens Focuser, Mount, Guider,
      Weather API)
    - Calibrate the focuser
    - "Park" the mount in a safe, low-power position
    - Wait until 10 minutes before astronomical dusk

[Note: because I'm using a camera lens rather than a telescope and holding focus
between sessions is effectively impossible, I hand focus (remotely!) at this
point to get to a rough focus; this takes about 5 minutes of snapshotting and
moving the focus point].

- Polar alignment and calibration:
    - unpark the scope
    - Run initial focus
    - Plate solve to understand where the telescope is pointing
    - Slew to a predefined point in the Western sky (my balcony has a very clear
      view of the Western sky, but almost no view of the Eastern sky)
    - Run 3-point polar alignment[^1]
    - Re-park the scope

- Wait until the target in question is visible in the sky, then slew to it
- Focus one last time
- Calibrate guider and start guiding
- Begin captures (predefined as part of the sequence - I'm usually doing 1
  minute captures now per exposure and "dithering"[^2] after every 3 exposures).

The sequencer tool in NINA is so powerful that I can even define rules like "if
the focus exceeds 5% difference between captures, stop capturing and re-focus"
or "send a notification to this HTTP endpoint if we lose guiding performance".

I will probably write an article soon about how I've come to understand NINA's
sequencer and maybe contribute some changes back to it; it's very nearly perfect
but it's still got a few annoying quirks that I'm still working out. 

But, the upshot is that I was able to set my scope up at 8PM when it was still
light out, wait inside while it got dark enough to do our first rough focus, and
then leave the system completely hands off until 1 AM when the 2 1/2 hour sequence
was done to put everything away.

Improvements for the future:
- DC power for my camera so that I'm not constrained by camera batteries any
  longer
- HTTP notifications to ping me loudly if something goes wrong


I feel like I've reached a big level-up milestone in my astrophotography, and
I'm super excited for the future.

[^1]: I talked a little about automated polar alignment in a [Past Astro
    notes](https://gabethebando.cc/post/astrophotography-session-4-17-26-shawnee-state-park)
    post. Now that everything is working correctly, automated 3PPA takes under a
    minute, with the caveat that I have to have the mount within ~3 degrees of
    aligned in both Altitude and Azimuth to start with. This is easy when you're
    always shooting from a consistent location with an obvious reference point
    (my balcony), but less so when you're out in an unfamiliar field. Consistent
    observing locations make things much faster.

[^2]: Dithering is something I'm experimenting more with recently. The basic
    idea is to kick your mount in a random direction every so often between
    shots; this helps the stacking software average out noise more easily when
    doing your stacking (which is essentially an averaging process across many
    shots). Camera sensors tend to have both random noise (which averages out
    easily - the SNR is very high for this kind of noise because randomness
    doesn't survive averaging across many samples) and constant thermal noise,
    especially in un-cooled cameras like mine. This kind of noise needs
    randomness in placement on the image to be averaged properly, hence
    dithering: if we move the sources of consistent noise all over the image
    randomly, they _become_ random in effect, making averaging them out easier.
    If you look carefully at the image above, there's still some blotchiness in
    some places; this is caused by the constant thermal noise not quite having
    enough randomness injected into it to be removed completely. Longer
    exposures have helped quite a bit (the SNR goes way up), and longer sessions
    with more exposures will help eliminate the rest.
