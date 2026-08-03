---
title: "Software Engineering in the age of GenAI: The Next 10 Years"
draft: true
date: 8-31-26
---

As a software engineer, it's fascinating watching other engineers work.

My brother is a mechanical engineer at Boeing working on flight controls. When
he talks about his work (and he does...a _lot_[^1]...), it's all about
compliance and parts libraries and getting technical drawings certified and
verifying he's following a big manual of design rules. In short, it's
_engineering_ work. He does stress simulations and thermal expansion analysis
and materials science and freakin' _math_ on a daily basis. He has half a decade
of physics and chemistry classes down cold, and it's frankly distressing as a
software engineer to hear him talk about how much _stuff_ he does.

We as software engineers simply don't deal with a lot of the trappings of the
real world in many circumstances. Oftentimes, our only physical constraints are
the memory of the machine(s) we're deploying our code to, the size of our disks,
and maybe network latency. If you're really lucky (or unlucky) and work on
something embedded or very low-level, you care slightly more about these
physical constraints and may have more imposed upon you, like the size of cache
lines, the effects of your software controls on physical devices, or thinking
about the PHY-level protocols of signals flowing over cables. These things are
somewhat more "real-world" than writing web apps, but again, it's just not the
same level of rigor as many other engineering discipline.

Even before the vibe-coding era, we did _code on vibes_. We made compromises in
our designs using complex- and important-sounding logic, making graphs and
comparison charts trying to show that one option is clearly better than the
other, but ultimately either the decision is obvious and the analysis is for
show, or the option truly doesn't matter all that much. This is perhaps a
controversial or even career-hurting thing to admit, but I don't know that I've
ever been faced with a make-or-break technical decision in my career that was
truly _make-or-break_; had we made the opposite choice, the outcome would likely
have been roughly the same (outside of perhaps moderately increased compute
costs or slightly worse maintainability long-term).

I'm reminded of a quote from one of my favorite movies, 2007's _Ratatouille_:
Anton Ego's monologue from near the end of the movie resonates deeply with my
experience as a software engineer (my changes bracketed):

> In many ways, the work of a [software engineer] is easy. We risk very little,
> yet enjoy a position over those who offer up their work and their selves to
> our judgment. We thrive on negative criticism, which is fun to write and to
> read. But the bitter truth we [engineers] must face is that, in the grand
> scheme of things, the average piece of junk is probably more meaningful than
> our criticism designating it so.

In other words, **the effort of having built the thing is almost certainly more
meaningful than the arguments we have about building the thing.**

## So...What does this have to do with modern GenAI?

In a world where "good enough" is almost always good enough, how do we get over
ourselves and start building faster, better, and cheaper? I think in some ways
GenAI _can_ provide us a path forward.

I've heard the comparison several times that GenAI is to software engineering as
CAD/CAM is to paper drafting, and I think that's the apt comparison. There are
folks out there who treat GenAI as something closer to a full replacement for a
software engineer, and those people are straight up wrong in my opinion.

Having done plenty of "agentic coding"[^2] in the last 8 months or so, I've
discovered the things that AI models are currently[^3] capable of doing, and
many many more things they are galaxies away from ever being able to do. In
general, I can group these into two categories: implementation work and
architecture work.

Imagine you're an architect designing a new building. Let's assume this building
is something quite boring, like a
[5-over-1](https://en.wikipedia.org/wiki/5-over-1). This is not a convenience
for the sake of the analogy, it's a deep and uncomfortable reality about the
work we do as engineers: generally, what we're working on is _quite boring_ and
_quite standard_. How many REST APIs (or GraphQL APIs, or gRPC APIs, or...)
have you written in your life as an engineer? It's likely a hell of a lot, and
it's OK to admit it.

So anyway, you're an architect, building your 5-over-1. There are constraints to
deal with: the space you have for parking, the amount of road frontage you have,
local zoning and building codes, the prevailing winds and where the sunlight
will come from. There are things that make each project unique enough that you
can't "just" copy-paste a building from one city to another. Your job is to take
all these details into consideration when designing your building, but
ultimately the building needs to get designed and eventually built. This is the
most direct comparison we have to our job as modern software engineers: we have
constraints, we have deadlines, we have circumstances that make our job not
totally cut-and-paste, but in many ways each project has roughly the same shape.
It's just a 5-over-1, it's just an API endpoint. And your expertise is exercised
by fitting those constraints. That's it. That's your job.

Architects have a library of designs to pull from when building 5-over-1s. They
have pre-designed floorplans they can drag-and-drop, they have hallway layouts
and parking structure designs and facades they can add to their building. HVAC
and electrical conduit follow a bunch of rules that can be encoded into CAD
software, and the architect's job becomes handling the weird corner cases where
the software can't handle auto-routing these pieces. They have a very small
amount of artistic license, and they may utilize that creativity 

[^1]: Sorry, Danny.

[^2]: The fact we call "running claude code on your computer" agentic coding is
    kind of goofy, but we must use industry terms in order to communicate with
    industry.

[^3]: I am not going to try to predict the future (despite the title of this
    article) when it comes to model capabilities. I _personally_ don't believe
    that models are going to improve as significantly in the next 10 years as
    they have in the last 5 years, because at a certain point it's diminishing
    returns.
