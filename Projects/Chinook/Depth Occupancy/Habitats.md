## Coherent Structures

https://www.youtube.com/watch?v=lveOu7jLNh0

https://numbacs.readthedocs.io/

## Some Thoughts

What makes habitats the same or different?

- Assembly (what organisms are present in each space) is ultimately what matters

But it seems to be driven by:
- Timing of primary production


It seems like timing is really correlated to everything... and it's something I can measure. So with this sim can I predict pzooplankton and other things using just those features (and something like a random forest)? Can I prove that the information about species assemblage is **captured by phytoplankton timing**? Because clearly currents show me where different habitats are but not necessarily what they are...

## Timelines

Let's see if we can compress timelines into a couple key features that can then be passed onto the full model. 

### Stability of Timelines

First off it seems that the best way to think about this stuff is in terms of timelines and scalings. I.e. that there are certain standard temporal patterns in particular regions and that each region is a mix of some set of these standard patterns. Then on top of this there is an overall scaling to set the productivity as a whole to the right level. What's interesting is that viewed in this light, individual H3 cells from one year to the next show dramatically different patterning. They angle they point in our unit sphere moves around dramatically _and_ the actual magnitude changes quite dramatically as well. The ocean, as it turns out, is a very dynamic place. 

I still think this timelines piece is important but I also think that habitat as being fixed in space is nonsense. These are islands floating around the world, coming into existence and then disappearing just as rapidly. This notion of timeline I think still makes a great deal of sense, but given the dynamism of the space I also think looking at the time line of one specific H3 cell is probably not the way forward. We would more likely need to integrate all of the various sources forward to get a real sense of the "habitat" in a specific area. And then there's the followup question of how does one capture a single feature that can work across the year (when later timelines are not known to you). Perhaps it is that habitat is a different thing with each month... I suppose that would be right. 

The more specific question to tee me up for next time is this - given I now know that it's a bunch of floating islands, how would I think about the integration of timelines? And then how would I go about breaking those down into pieces? I.e. into constituent timelines and overall abundance? 

I'm definitely on the right track here, but we're just having to burrow down a little deeper with each fold. 

The other question is do I just call this here and write a paper? Or do I dig in one step further? I should probably answer that question first :) 

Alright after some thought I think the main thing here is to just see how different the back tracked timelines are as compared to the in place ones. If they are not crazy different we'll just keep what we have. If they are we'll do the backtrack calculation. 
