- [ ] Follow the paper writing method you crafted for yourself 
- [ ] Work out what your goal and objectives are
- [ ] Work out the waypoints 
- [ ] Build out your methods 


- [ ] Build Behavioral Space Engine for "Navigation" Features
- [ ] Train New Models and Explore Space
- [ ] Find some Kickass Applications
- [ ] Build out the Outline

I think the main focus here has to be show, don't tell. So I need to find some simple but power applications of the movement models and have that be what's showcased. I will also need to do more research on what's known about the drivers of salmon movement today. 

Some ideas:
- Gradient Fields
	- Show what collects and what disperses fish
- Timing
	- Show how long a specific marine protected area will last
- Dispersion 
	- If we have a whole load of fish in a specific area, how long till folks can safely go back?

Before this though I just want to think through if I'm posing these features correctly at all. 

Most behaviors have to be intentioned with a trigger, destination, and route finding. Key is to find it and prove it out in the data. 

I'm going to go back over the visuals and see what I can find in terms of those things. And then think of applications I can build off of that. 

## Some Observations

1. There's a tendency for the fish to move offshore during the winter months our the AI. Whereas during the summer the fish in the GOA are real close to the shore
2. No one ever really leaves the continental shelf. 

Distance from edge of shelf. Distance from shore. Depth. Season (month). Also the direction opposite shelf (i.e. orthogonal too) would be really interesting as well. Distance travelled as well of course. Some notion of south and northness too would be helpful. Offshore inshore. 

Orientation features. Distance to shore, distance to edge of shelf, angle compared to shelf, south vs north, east vs west, distance moved, time of year, distance north. We'll build some models with this tonight and then we can come back to questions of applications tomorrow. (I'm just really curious)

1. Start out with some way of determining what's continent, coast, and offshore
2. Build out the features for an h3 cell (how do we do this through athena?)
3. Build the features!

(Just remember this has to work with athena as the main engine at the end of the day)
