---
title: 'Astrophotography Session: 5-9-26, Cincinnati'
date: 5/15/2026
---

For the first time in a very long time, things _basically just worked_. My only
"failure" of the evening was not getting enough data, and that's just because I
took too long to get set up, but that's a fixable future problem. Overall, I'm
pretty pleased!

## The final result, first!

![The Bodes and Cigar Galaxies](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/bodes-cigar-5-9.jpg)

Click [here](https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/bodes-cigar-5-9.jpg)
to get a closer view. This is M81 and M82, the Bodes and Cigar galaxies
respectively! The Bodes is the spiral on the left, and the Cigar is
the...cigar-ish looking blob in the bottom left. This is a total of about 50
minutes of "integration" (pictures) stacked in [Siril](https://siril.org), the
best open-source astrophotography processing software I've yet found. This was
shot on my OpenAstroTracker with 15 second exposures on a Canon 60D with an EF
100-400 IS II lens at f/5.6 and a focal length of 400mm.

Overall I'm pretty happy with these results especially given the less than ideal
exposure lengths and the lack of sharpness of the 100-400 lens wide open; I did
some experimenting with my post processing and switched away from fully
automatic post processing scripts and towards [manual
stacking](https://siril.org/tutorials/tuto-manual/) and processing. This was a
_huge_ level up to my image processing, and I learned a bunch about the actual
process of stacking, so I think this was 100% worth it in the end even if it
made my processing take quite a bit longer.

## Successes

Generally speaking, _everything_ worked without too much fuss! My main goals for
the evening were to make sure each major component of the rig actually connected
together and operated correctly:

- Camera: 15 second exposures were no problem, I probably could have gone longer
  but ran into a weird issue with bulb exposure
- Mount: I had replaced a bunch of the parts on the rig with new ones printed
  from PETG-CF (carbon fiber reinforced PETG, a much stiffer material than the
  PLA I originally used)
- Focuser software for the lens: this just worked, no notes!
- AutoPA: Fucking _magic_. I made a fix in the OAT firmware to move only half
  the distance the tracker "wanted" to move, so that it would undo the double
  movement correction from before, and it dialed in a nearly perfect polar
  alignment faster than I could walk to my car to get a camping chair and back.
  SERIOUSLY nice piece of kit.
- Guider: mostly worked! Calibration was a bit tough, but I realized after about
  45 minutes of tinkering that calibration works best close to 0 degrees
  declination, and I was quite a bit higher than that.
- Dithering: worked a charm!

The goal was to exceed a 30 second exposure but I couldn't do that for 2
reasons: one, I never got my guiding to be under 1 pixel (~2.25arcsec) accuracy;
I hovered at around 3 the whole night, and that limited my exposure a bit. And
two, my camera absolutely freaked out when I tried to do a bulb exposure. For
reference, bulb exposure is a camera mode where you hold the shutter open for an
arbitrary amount of time, and is super important for longer exposure astro. I am
hoping to get to 2-3 minutes per exposure, but for now 30 seconds is the next
hurdle. Anyway, the issue I ran into was that my camera couldn't hold the
shutter open _at all_ when bulb mode was enabled. It would close in under 1/10
of a second and freeze. I think this is a driver bug, so hopefully there's an
easy solution, but I don't know what to do next to fix it.

## Stuff to improve on

Setup time was a pain in the ass - my not realizing that calibration of guiding
needs to happen as close to the celestial equator as possible, and as soon
after polar alignment as possible, was a big time sink. I also need to figure
out how to make bulb mode work. My next goal is 1 minute exposures!
