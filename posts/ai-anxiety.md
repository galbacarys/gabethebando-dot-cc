---
title: AI Anxiety
date: 04/01/2026
---

I do the majority of my software develompent at work these days making heavy
use of AI, specifically Claude Code and the Opus 4.6 model. I have started to
get recognized as an "AI expert" at work, which...yikes. I feel like I'm just
trying to keep my head above water, keep up with the crowd, whatever, and as I
think I said in the "about" page (or maybe the first post on this blog? Man,
I'm tired...) the more I use AI tools the more I get anxious about whether I'm
going to replace myself by over-leveraging AI. I start to worry that I'm not
doing anything even closely resembling software engineering anymore. What
happens if I'm "found out"? What happens if they cut off the token spigot? What
if the whole world falls apart and my family starves to death?

It gets really intense really fast.

I'm noticing my mental health suffer as I use genAI tools more. I get anxious
that I am losing my ability to write good code, I increasingly feel like I'm
days from getting outed as a fake software developer[^1], I _feel_ like a fake
software developer. And in many ways my work is less fun and less worthwhile.
I get a lot more "stuff" done in the abstract sense: I've shipped more shit
in the last 6 months than I ever have in a similar period before, and all of
it feels way less meaningful because I haven't had to work as hard for it. So
it all feels fakey fakey fake fake fake fake.

## How did I get here?

I used to care _deeply_ about software craft. I worked hard to write good code
that documented itself, that was elegant and clear, that showed off just how
goddamn _smart_ I was. I always felt terrible at it, but I cared; I spent way
too much effort (I still spend way too much effort) configuring vim and tmux
and zsh to be highly customized just for me, and I relished in showing off
to people how fast I was at solving problems with code (even when the code
itself wasn't all that great). I was so good at reading code and understanding
it, I worked really really hard to absorb new projects and be able to work
on them quickly.

But over the last several years, my priorities have shifted. I don't code
"for fun" anymore. I have a toddler and hobbies and I'm growing distrustful
of computers and this industry in general, and I just don't get the same joy
I used to out of being in front of a computer. I started using IDEs (gasp)
to write some of my code[^2], and I started getting less engaged with work.
I think some of this is inevitable. I'm older now, I'm more aware of my worth
as a laborer and less enthusiastic about throwing my weekend down the tube
to solve some "neat" tech problem. And ultimately...it's just work. So many
other things bring me joy, and work is the thing I do to make money. This is
good(tm).

And then one day, last October, I was working on an internal project that I
just simply didn't care about that much; I think it was a set of SQL queries
to answer some questions about the composition of our game portfolio or
something, and I was always terrible at writing SQL, and I was tired. Some
random Tuesday, an email came in announcing an early access program for AI
coding tooling (the tool of choice at the time was Roo Code). In a moment of
weakness and laziness, I decided to say "fuck it" and try it out.

Reader, I was blown away.

I vaguely described what I was trying to do, pointed it at a DDL for the table,
it spun for 2 or 3 minutes, and spat out 10 queries that answered my questions
and within 15 minutes wrapped them in a little web UI to be queried whenever
someone happens to ask. It was _mind blowing_ and it was _scary_.

The next two or three months were filled with both feverish enthusiasm for
all the _stuff_ I could _build_ and also dread that maybe the one thing
I've ever found that I can make money at is going away soon. I spent many an
hour reading articles talking about how AI is going to replace all the engineers,
especially the ones who depend too much on it, except that another article said
that the folks that spent the time to learn the tools would be the _only_ ones
with jobs in the future, except that _another_ another one said that if you give
over your work to the clankers you're just training them to replace you, and
on and on and on it goes. By the end of the year, I had gotten to the point where
I decided that day one back in the office of the new year (2026) I would simply
swear off of AI entirely.

And then it happened. A project that I had no prior knowledge of, that was way
out of my normal wheelhouse, and that had a very tight deadline. Well, shit.

I had to build an entire Unreal Engine game (demo, really) that showed off all the
features of a particular part of our platform. I am a failed amateur game developer
many times over, I know how to build games generally, but UE had always been a
mystery to me. And so I, in another moment of weakness, turned to Claude Code (the
new hotness of AI coding agents).

Again, I was blown away. Claude Code understood deeply what I was asking for, long
before I fully understood what I was asking for. It could synthesize sources from
around the internet to answer difficult questions about how deep, scary corners of
the engine worked. _It could and would frequently read engine source code_. This was
a level of research prowess that even at my peak I couldn't manage. I felt utterly
replaceable, and replaced.

And then something happened over the next couple of weeks. I was pretty much forced
to lean on Claude for the work I was doing, and slowly I found myself both
understanding Unreal better and learning to use Claude less as a magic skinner box
of engineering results and more as a real tool. I learned to start curating what
information the model sees, I learned to ask for exactly the right thing the first
time and use pre-written plans, I launched background workflows that could
solve problems as I worked on other stuff, it started to properly augment my
productivity. I'm starting to get recognized as an expert now at work; people
are impressed by my ability to both use and teach this tooling, and I'm starting to
unclench slightly about all these tools.

The hard thing is still convincing myself I'm doing real work and that I'm not just
offloading all my thinking to the AI. I have some evidence that this isn't the case:
I have been hand-curating a big huge git repo of notes that I have the agent use to
get better context on the (very weird) stack we operate on, I've built tools that
help me do my job more effectively in this brave new AI future (albeit those tools
were mostly prompted together). I still steadfastly refuse to do _any_ AI-assisted
writing. Maybe that's a stupid line to draw, but I care deeply about how I communicate
and I would much rather my imperfect thoughts leak out of my brain than that my thoughts
are averaged out and smoothed into a homogenous loaf.

## So...now what?

I guess, if you're feeling AI anxiety like I have been, good. Lean into it, let yourself
be uncomfortable. If you choose to adopt AI tools because you feel like you need to,
do so in small ways that make you feel like the core of your work is still yours. If you
go too far off the rails and don't feel like you have ownership of your shit anymore,
find something to own fully again. Take stuff away from the AI. As I've said in more than
one presentation about how to get onto AI at work, you always have the power to unplug
your computer and chuck it in the ocean if it does stupid things. This applies to your
AI coding agent; if it's being stupid throw it away and give yourself a breather.

I wish I could give better advice; I wish we lived in a world where I didn't have to think
about whether my work is human enough. And I wish I was a good enough, confident enough
programmer that I didn't resort to these tools in the first place, because the pandora's
box is open now. But while it's open, let's try to take care of ourselves and each other,
yeah?


[^1]: This may be a longer standing anxiety though...

[^2]: I really shouldn't give myself shit for this. I was writing _Java_ for
fuck's sake, the language that broke 1000 vim configurations.
