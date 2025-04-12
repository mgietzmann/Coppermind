## Waypoints

- [x] A quick intro to why targeted fisheries practice matters
- [x] A note on the fact that movement is the only way to help understand how to do spatial avoidance
- [x] A background on time/area closures as one strategy
- [x] A quick intro to Chinook in terms of bycatch importance
- [x] What is known about Chinook movements today
- [x] What kinds of models exist today
- [x] The need for models that allow us to sim
## Goal

Our goal is to demonstrate the value that models, which express movement as discretized distributions, can bring to informing more targeted fisheries practice. We will do this by:
1. Introducing a strategy for building probabilistic deep learning models over electronic tagging movement data.
2. Building a movement model that predicts the likelihood of movement of individual Chinook salmon between adjacent grids in a discretized grid of the Gulf of Alaska
3. Evaluating the model against the observed movements in the tagging data
4. And providing a series of illustrative examples of how the model's predictions can be used to inform more targeted fisheries practice 

### Objectives

#### Introducing the Strategy

This is done. 
#### Building a Movement Model 

This is mainly about features. 

- [ ] Distance from a Coast & Distance off Shelf
- [ ] East v West & North v South
- [ ] Season
- [ ] Direction off Coast
- [ ] Depth
- [ ] Distance
#### Evaluating the Model

Here we will be using the whole colored paths comparisons as well as the overall model evaluation.

#### The Illustrative Examples

1. **Pooling vs Diffusion:** If you have a series of areas in close proximity to one another and some result in pooling (increases in exposure or duration) as opposed to diffusion (decreases in exposure or duration) then the pooling areas become likely hotspots _relative_ to the diffusive areas.
2. **Pool Movement and Connectivity:** Understanding where the pools move and how they are connected through time helps us indicate:
	1. Increased likelihood of hotspots (if you can be relatively certain of a set of hotspots then what they are connected to becomes more likely)
	2. How the best fishing spots move as a function of time and where the danger zones move with time (also required to look for where movement is opposed to the actual target species)
	3. Ways in which repeat exposure could likely happen
3. **Value and Timing of Dynamic Closures:** whether through slowing rates of diffusion or pooling where are the spots where dynamic closures make sense vs where don't they? And then also what should the specific timing be on those closures. 
4. **Separation of Concerns:** one particularly interesting application here is the question of whether the GOA/EBS divide is actually a good idea. How connected are the two areas? 
5. **Protected Areas:** are seasonal closures even a possibility? Or is there a lot of diffusion? (This would be if you wanted to protect a specific subset of the species)
