Salmon eat squid and herring and anchovies which in turn eat euphausiids and copepods. This then falls back to diatoms and other phytoplankton which in turn wheels about weather and the like. Point is that I believe in understanding the oceanography and primary and secondary productivity in the GOA I will start to understand how these environmental features really matter. 

- [ ] Learning through pictures
	- [x] Find models/pictures of plankton distributions over the years
		- [ ] Upload the dataset to Athena
	- [ ] Find models/pictures of ocean currents, temps, etc over the years
	- [ ] Find models/pictures of ocean chemistry over the years
	- [ ] How to break the fluid dynamics up into nice pieces?
	- [ ] What are the lifecycles of these critters?
	- [ ] How to represent these timings?
	- [ ] Why the shelf, really?
- [ ] How to view pictures nicely
	- [x] Explore deck.gl
	- [x] Explore kepler.gl
	- [x] Sort out how to make tiles
	- [ ] PMTiles Builder
		- [ ] How to take different levels of h3 and a map (h3->zoom) and build pmtiles that work (include time so we can double check that works as well)
		- [ ] How to aggregate up to different levels of h3
		- [ ] How to join into geospatial data (i.e. with polygons)
		- [ ] Pull it all together
		- [ ] Make a job?

My conclusions from this exercise is that Kepler is really annoying. It is just so point and click and it makes trying to do anything super difficult and totally unrepeatable. Also PMTiles _do not_ support temporal features at all and Kepler does not recognize things in them that are clearly dates, so while we get spatial scaling we totally lose the ability to usefully visual time (I'd have to load each timestep as a different layer and manage them all independently). As a result I'm just going to focus on plotly because it can deal with this scale just fine, makes everything super repeatable, gives me tons of programatic control (I can control colors without clicking and typing stuff) and then lets me save everything nicely. 

The programatic nature of plotly reigns supreme. :) I can customize colors, resolution, shapes, everything, totally programmatically making life easy and repeatable. And in the end, often enough I want to actually be able to do math on the maps, which is impossible otherwise. 

I'm going to try to get really good at using plotly by just practicing only using go. Hopefully that will help me dig deep and really understand what's going on in the library. 


- [ ] *What do they feed on?:* Figure out what salmon feeding habits are. 
	- [ ] Daly 2017
	- [x] Daly 2009
	- [x] Weitkamp 2008
- [ ] *What is habitat?:* How do feeding habits create habitat? What are other ways habitat could be formed in the big blue. 

----

### Data Visualization

Ended up looking at deck.gl and realized kepler.gl is just using it and has everything I want. 

Basically moral of the story is that one can provide a huge amount of functionality with just kepler GL if you're willing to load in your data yourself. 

And it can use tile layers now so that should allow me to scale all of this really well... 


https://search.dataone.org/view/10.24431/rw1k8f0



----

## Some Questions

- [ ] Why do we see less productivity when the water is deep? (even inshore [Kodiak])
	- [ ] Is kodiak creating a wind boundary?
	- [ ] Or is it a current sweeping through that region and moving nutrients away?
		- [ ] Actually I do wonder whether this is just a current sweeping things along 
		- [ ] I bet you its not actual productivity but the currents that create these hotspots
- [ ] Why are there only plankton blooms over the continental shelf? 
	- [ ] Why does the iron end at the shelf? 
	- [ ] Why not out in these eddies? Is it perhaps no brood stock? 
- [ ] Why does ammonia show up where plankton aren't?
	- [ ] Because while it is a byproduct, the ammonia is also used up by primary producers.
- [ ] Why is the water so fresh in September?
	- [ ] Does that have something to do with the variability in their movement? 
- [ ] What's up with the two month delay between copepods and euphasiids and diatoms
- [ ] What's up with meso2+3 lining up so well with salinity (6)
	- [ ] It's because it's lining up with the diatoms - who start near the coast and then spread out
- [ ] Why is the diatom bloom larger in the north than in the south??
	- [ ] Less silica (this is totally the limiting nutrient out here... and I bet is why I'm seeing what I'm seeing in the salmon model)
- [ ] Why is there a double peak in nano
	- [ ] Perhaps an oscillation with their predator (micro1 - Cook's inlet)
	- [ ] Looks like diatom's don't have the double peak because their cycle takes longer (peak is reached a month or two after micro and takes longer to die out)
- [ ] What's up with the Nano's starting way up Cook's inlet? 
	- [ ] Iron???? and low current???
- [ ] Why do the diatoms all start directly next to the coast?
- [ ] Are the diatoms getting eaten or just exhausting some kind of resource?
	- [ ] Or is whatever is pushing out the fresh water also pushing them? 
	- [ ] I think they are running out of silica 
- [ ] There are also a hell of a lot more diatoms than nano's so I bet you they could survive on far fewer nutrients. 

Currents, predators following, exhausting resources (all could define the movement here)






2:30p July 10 Trondheim 
10:00a July 17 Trondheim

Get some flight insurance 