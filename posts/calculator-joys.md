---
title: The Unexpected and Previously Unremembered Joys of Graphing Calculators
date: 05/21/2026
draft: true
---

For reasons that are a bit hard to explain[^1], I have picked up my old calculus textbook from college, and I'm starting
to re-teach myself the basics of calculus. It's been quite a lot of fun, actually; I _hated_ math classes in high school
and college because no one ever taught me to _enjoy_ math, but something clicked in the last five or six years and made
math not only way more entertaining than it was in school, but a truly beautiful subject on the same level as things
like functional programming and music. Applied correctly, it's elegant and consistent and symmetrical and feels so good
to manipulate.

Part of the exercise of pulling all this math from the deep recesses of my brain has been re-engaging with the old tools
of the trade: pencil and paper (a true blast from the past - I haven't spent an extended amount of time using physical
pepr since I bought my first iPad a few years back), and a TI 84 Silver Edition graphing calculator. And what a goddamn
_delight_ it is to use.

## The Gorgeous Symmetry of TI's Graphing Calculators

As someone who's been programming for a very, very, very long time (literally 21 years at this point), my TI 84 remains
my favorite programming environment I've ever used. It's just so beautifully elegant: there are 26 variables, simply
named `A` through `Z`, plus 6 "lists" (think arrays) and some matrices. Each of these is _global_ - this means that any
change to a variable is reflected globally in the entire calculator's operating system. This sounds terrible, of course;
who would want global scope? But with some careful thinking, this can be a huge asset.

You see, the `X` and `Y` variables are also globally shared, and these are the same ones used in the graphing screen. So
if you use the intersection solver, the `X` and `Y` variables _are set to the intersection point_. Any program you write
has its outputs immediately saved. Oh yeah, and you can write programs! In a relatively easy to use dialect of BASIC!
The beauty of all of this extends to every corner of the OS. Storing and recalling values into variables is a
first-class construct (thus, for example, you can _store_ values into `X` and `Y` when convenient, and it will reflect
on the graphing screen).

The BASIC dialect built into TI-83/84 calculators is certainly a bit primitive as programming languages go, but it's
quite functional and has some interesting affordances for the hosted environment. You can't type out the names of
functions, you have to dive into a menu to copy them into your program, and all you "type" are the


[^1]: Not actually hard to explain: this is a bit of hubris on my part. I've gotten it in my head that maybe someday it
    would be great to go back to school and get a master's in Physics and Astronomy so I could level up my photography
    and start doing some real(tm) science(tm). This is a vanity project and I should probably be ~~taken out back and 
    shot~~ _given a gentle push away from this path_, but here we are.
