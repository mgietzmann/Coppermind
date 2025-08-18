“Fishers are some of the most qualified people to develop and improve bycatchmitigation techniques” (Gilman et al., 2006, p. 6)
## Reasons to Avoid Bycatch

“Both gill-net and trap-net fishers foundthat as the Lake Trout population increased in the 2000s, sorting, handling, and releasing Lake Trout bycatch fromtheir gear became a major task” (Bergstedt et al., 2016, p. 3)

“The issue is addressed as a component in agrowing number of broad international resolutions,including Agenda 21 (1992); the Cancun Declaration (1992); UN General Assembly Resolutions 49/118(1994) and 50/25 (1995); the Rome Consensus on WorldFisheries (1995); the UN Food and Agriculture Orga-nization International Code of Conduct for ResponsibleFisheries (1995); and the Kyoto Declaration and Plan ofAction (1995) [6,15,17]” (Gilman et al., 2006, p. 1)

“For instance, hundreds of thousands of seabirds, including tens of thousands of albatrosses, are caught annually in longline fisheries worldwide, posing acritical global threat to some albatross and large petrelpopulations [15,16,20]” (Gilman et al., 2006, p. 2)

“Cumulative turtle mortality in pelagic longline gear worldwide poses a priority threat to sea turtles, in particular, to leatherback (Dermochelyscoriacea) and loggerhead (Caretta caretta) sea turtles” (Gilman et al., 2006, p. 2)
## Avoiding Bycatch

“There are many strategies to manage commercialmarine fisheries bycatch. These include formal constraints through laws, regulations, and policies; multilateral accords; marine protected areas, including areaand seasonal closures; best practices for handling and release of bycatch species; changes in fishing gear and methods; eco-labeling; industry self-policing; industry awareness-raising and capacity-building; and fleet communication programs [6,16]. Multiple methods can be implemented in combination to pursue sustainably managing fisheries bycatch.” (Gilman et al., 2006, p. 2)

It's better to move fishing effort to areas of low predicted bycatch as opposed to just away from areas with high instantaneous bycatch [[Shirk 2023]]. Relatively minor changes to fishing effort can result in large declines of bycatch [[Shirk 2023]]. 

With marine environments changing due to climate change it is becoming increasingly important to understand their underlying mechanisms. [[Sabal 2023]] For example, during the Pacific marine heat wave humpback whales (Megaptera novaeangliae, Balaenopteridae) moved inshore to feed resulting in record numbers of whale entanglements with the Dungeness crab [[Sabal 2023]].

If target and bycatch species have distinct distributions in the water column this can be used to understand and reduce bycatch [[Sabal 2023]].

“The differential response between target and by-catch for day vs night sets indicates that there may be potential to alter target:bycatch ratios or to reduce bycatch of specific species by changing the time of day of setting.” (Orbesen et al., 2017, p. 9)

“It is important to understand that there are differential responses between target species and bycatch, and small shifts in fishing effort could have large impacts on catch rates of key bycatch species” (Orbesen et al., 2017, p. 12)

[[Illumination for Escapement]]


## Modeling Bycatch

Some folks will model based on bycatch data. [[Shirk 2023]] [[Sabal 2023]] 

Quasi-poisson distribution with log link function [[Sabal 2023]]. 

Some folks using hurdle models [[Shirk 2023]]. 

Linear models GLMs and GAMs or trees are used [[Shirk 2023]]. [[Shirk 2023]] found the trees were better. However they were having some issues with overfitting [[Shirk 2023]]. 

Features used include fishing sector, year, haul duration, day of year, time of day, fishing depth, location, ocean depth, sea surface temperature anomaly, upwelling, and bottom slope [[Shirk 2023]]. 

Cyclic cubic regression to get time on a loop [[Sabal 2023]]. 

Folks have used blocked time series cross validation [[Shirk 2023]].

### To Make the Models Useful...

“The accurate prediction of the effect of depth regula-tions requires knowledge of the geographic location (andthrough that of bottom depth) concurrent with measurementsof fish depth to determine the proportions of fish suspendedabove the bottom” (Bergstedt et al., 2016, p. 15)

## Examples

[[Pacific Coast Hake Fishery#Chinook salmon Bycatch]]

[[Pelagic Long Lines#Bycatch]]

[[Lake Whitefish Fishery#Bycatch]]

[[Walleye Pollock Fishery#Bycatch]]

[[Orbesen 2017]] [[Sabal 2023]] [[Shirk 2023]] [[Bergstedt 2016]] [[Gilman, 2006]]