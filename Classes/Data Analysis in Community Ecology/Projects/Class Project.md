#research #class #abundance

## Part 2

### Structure of the Homework

- [ ] Background - Provide a very brief background and rationale for the study (5 points)
- [ ] Problem description – What is (are) the question(s) you would like to answer with this class project? What are your goals/objectives for this project? You can provide some broader context, but don't expand the objectives beyond a feasible, limited, and clearly defined project for class. (10 points)
- [ ] Data – Provide a brief description of the study and/or data sources (Variables, study area(s), time period covered, etc.). If suitable, include a map, data table, or other summary of the data to help me understand the dataset you are using. (10 points)
- [ ] Data checking and preliminary exploratory analysis – This should include a brief description to explain and summarize some essential characteristics of the data, including units and scale of measurement. Include 2-3 figures that, to the extent possible, display the bulk of or all of the data for a quick visual assessment. For each figure, include stand-alone captions (i.e. without reference to text) that clearly describe figures. (20 points)
- [ ] Describe any issues that may affect the analysis or interpretation of your data such as missing values, unbalanced data (data gaps, time series of different length, etc.), presence of many zeros, or data with an otherwise unusual distribution. (5 points)

### Things I Need

- [ ] Pull down the full dataset 
- [ ] What kind of environmental data are we going to be using?
- [ ] For each column in the dataset create a description and plot out the data
- [ ] Figure out how to pull the descriptions down to what's described above
- [ ] Write out 3-5 from the above
- [ ] Come back to the problem description and background

## 2025-03-21

### Pulling the Data

Python API - https://afsc-gap-products.github.io/gap_products/content/foss-api-py.html

Holy cow this thing takes a while, a query in one region, in one year, for one species took 5 minutes... and it took longer in their example notebook - https://pyafscgap.org/

10 minutes to grab a single year in full so definitely worth doing things in bulk... 

And of course the pandas conversion in the docs doesn't work... There's a couple get_X that should be get_X_maybe. Thankfully I have access to the source code :) 

Alright it takes ten minutes to get a year but we have a year! 

Let's see what we actually care about from this data. 

We can use depth, temperature (surface and bottom), stratum, net height, net width

I've got the years from 1982 - 2024 (42 years) which means it'll take around 7 hours to pull all of this data down. 

Alright latitude seems to be missing from a lot of the original records in 1982 so I've gone ahead and surrounded all the "get_X" with try/excepts so we can see what data we're actually able to retrieve and then clean things up later on the basis of that. 

Alright when I get to the hotel I'll let this churn away overnight so that we get all the data and then we can proceed to do some cleanup. 

### Cleaning the Data

Alright we've got it all so let's see what we've got. First question is whether we want to predict the cpue or the actual biomass. I think cpue is probably better just because it is standardized to the length and width of the tow. Otherwise we'll get a ton of variance just from towing differences (at least in theory). 

So first off only 2% of the data has non-zero cpue. 

Question is - what species do we want to keep around as there are 975 in total. 

There are a bunch that end in sp. which I think indicates that it's not particularly meaningful to any specific fisheries. Damn there are only 1.5% of the records with a HIGH level of confidence. This happens to be 70% of the data with actual catches. But this corresponds to only 9% of the overall species. 

So I think we'll start by restricting ourselves to species that have high confidence. (which is 89 species) 

Over all of the years if we look for species whose confidence is moderate to high 95% of the time we get a sample we get 473 out of 1,327 species. 

**Year, haul and station are a unique key for each haul.** 

Never mind made a mistake only 273 species have both high confidence and are actually a species designation. 

If we limit it to species that show up in at least 5% of hauls then we're down to 66 species. 

Visualizations I want to include:
- [x] Geo plot faceted across columns (environmental) that show the environmental data for a particular year
- [x] Table of species and general stats on each
- [x] Faceted distributions across the various "environmental" features
- [x] Couple of example species distributions (when non-zero)

### Worries About the Project

So I'm worried that the way I'm putting this project together right now leaves me with absolutely no uses for the stuff actually dealt with in class as I can just start at the end and build models to find the most important features. However I think I solve this if I use a clustering or dimensionality to reduce to groups that vary together and then from there show the informativeness in each group. That will also greatly reduce the number of models I actually need to train and will give some indication of what the groups are which would be a lot more ecologically interesting that just a reverse through all species and having no idea who's connected to who. 

The last thing I need to sort out is what to replace my "variance predicted" with to calculate my information score given how many zeroes there are in this data. 

Tomorrow morning I'll walk on that and then in the afternoon we can just write this front to back :) (we can add figures later) 

### Looking for an Information Metric

I think I could go down a classification x regression metric but what makes me uncomfortable about that is the fact that if we make small regression predictions the fact that we made a misclassification doesn't really matter. I.e., not all misclassifications are the same. I need to work out this bit and will do so after work. 

One problem is that I have to choose when we use the abundance model vs when we don't. I.e. I have to choose a probability at which point we choose to invoke the abundance model. As I increase that threshold the number of false positives will of course go down but the number of true positives will go down too. So as I raise this threshold my performance over the zeros is going to improve and as I reduce it the performance over my "ones". The question I think is how to measure performance over zeros and how to measure performance over ones and then come back around to the choice of threshold ('cause we can select it to maximize some overall score across the two over the training set)

Over the ones it is obvious - we just want to reduce unexplained variance. I think the more interesting question is what we care about over the zeros. More or less the closer to zero we are the better (and we can think about this in terms of some kind of average). If we're very very far from zero that's a very bad thing. However whereas the explained % variance is going to be between zero and one here we've got something quite different... 

One way of looking at this is that the best case is we generate _no_ false positives. This would represent a score of 1. Then the worst is where we have the maximum number of false positives. This isn't useful though because these two are not comparable at all. 

However thinking about sweeping this... as I create more and more false positives I'm going to create a worse and worse explained variance score as I'm going to create a load of false positives that effectively create residuals that shouldn't be there. But if I create more and more true positives I have the opportunity to explain variance away as well. If I add a very small amount of new variance across loads and loads of samples but a huge amount of variance is explained away in a few then that would balance out. So I think this actually makes quite a lot of sense. I.e. I can just use % explained variance as my metric. It's going to prioritize the classifier in cases where we have loads and loads of zeros (we can only incur very small amounts of new variance because there's not many samples to explain). This actually feels relatively helpful. If a species is very rare, knowing where it is is more important than knowing how much of it is in a place. 

Okay so the argument is this. We will have a classifier and a regression. As we increase the threshold for the classifier we get more true positives and more false positives. The true positives then allow us to reduce the residuals (based on an average model) but it will also create new residuals. The sum of the residuals / (sum of original residuals) then gives us a sense of whether we are reducing the overall uncertainty. 

What we'll do then is build the regressor and the classifier and then pick a threshold based on the training data before applying to the test data. 

I think just working with explained variance works nicely here as well. 

If some species is not getting a good score then I think it becomes more about why (is it a classification issue or a regression issue). 

I think just splitting this into two cases actually makes a lot of sense. (1) Try and sort out which species co-occur together and how much that tells you. And then find species that correlate when they occur. Then you have explained variance in both cases. 

Let's bullet out this whole proposal before we head to dinner. 

## Outline

### Background

- Fish (and crustaceans) coexist together, therefore it would seem likely that groups of them covary both in terms of their range and their magnitude across space and time. 
- Monitoring of these species usually consists of taking samples at specific places and times in order to build up models of overall abundance. 
- Monitoring costs money and takes time. Even if you are pulling everything up in the same trawl, sorting takes more time if there has to be clear attention paid to every single species.
- Therefore a natural question is whether the covariance in groups exists to such an extent that you could use samples of some subset of the species to the predict the samples that would have been drawn for the remaining species.
- This problem typically splits into two parts:
	- Occurrence: where do the species occur (regardless of abundance)?
	- Abundance: where they do occur how abundant are they? 
- In the first case we are looking for groups of species who occur in the same place but not necessarily at the same densities
- In the second we are interested in species that, when they occur together, occur in ways that covary. 
- The first step in approaching this problem is finding species that covary together. This is our first question. 
- The second would then be, for each group, to understand how the removal of species from the "monitored" pool into the "predicted" pool effects the amount of "information" gained from the monitoring. 
- What does information mean here? Well complete information would be actual monitoring, so to the extent that we can predict the monitored samples would determine the extent of information we have captured. Measuring the prediction power becomes the measurement of information. 
	- In the occurrence case we have a slightly more complicated problem because in addition the model we must determine a level of confidence we'd need from our model to declare a positive:
		- This would largely be a practical matter dependent upon the application in question as lower thresholds would increase recall while decreasing precision whereas increasing the threshold would do the opposite
		- We can get around having to make a decision ourselves by looking at ROC curves. And then the remaining area above the curve would be the information still remaining. 
	- In the abundance case this is as simple as the explained variance. 
- Finally to ground this usefully we'd want to compare all of this to models that don't include any monitored species at all if we really want to know how much the monitoring of species is telling us. 
- For this we want a relatively large and comprehensive dataset over the course of many different years. This makes the bottom trawl survey in the EBS and GOA perfect.
### Problem Statement

- In order to understand the extent to which a subset of species can be used to inform the range and abundance of a superset of species we will use the Bottom Trawl Survey to
	- Find groups of species that meaningfully covary together 
	- Identify how much information remains as species are moved from a "monitored" to a "predicted" status in each of these groups
### Data

- Alaska Fisheries Science Center’s Groundfish Assessment Program conducts a yearly bottom trawl survey with the help of several other organizations including the ADF&G and the International Pacific Halibut Commission
- The purpose of these surveys is to produce biomass and count estimates for commercially important fish and crab species. 
- The EBS is monitored every year whereas the Aleutian Islands and GOA are monitored every other year (opposite one another). There is also a biennial survey of the northern bering sea NBS. There is also intermittent surveys of the Eastern Bering Sea Slope.
- These surveys occur between May–September and corresponds to a trawl vessel making its way to a variety of set stations (locations) and hauling a bottom trawl at 5-6 km/h for typically 15 or 30 minutes. The catch is then sorted by species and weights and counts are recorded for each species. 
- The species sorting does not always lead to the same degree of certainty and so species come along with indications of the taxon confidence as well as may be grouped into larger taxonomic groupings (for example genus). 
- In addition to counts and weights in most cases bottom and surface temperatures are recorded and in all cases the depth fished is recorded as well. 
- These surveys have been carried out year over year since 1982 with the once exception being 2020 due to covid issues. 
- This data is then uploaded for public access and can be pulled down in a variety of ways including an online data portal, an R package, and a Python package (which we used). 
- Finally recorded with each haul is the stratum (an enum) in which the haul was conducted - these stratum are indicative of the environment are meant to aid with stratified sampling estimates. 

### Data Checking and Preliminary Analysis

- There are a large number of columns available through the Python API which cover taxonomic, cruise, station, year, survey, weight, haul, count, environmental, and cpue data. We will describe the features used and provide brief explanations for columns omitted. 
- First each haul is keyed by the `year`, `srvy`, `station`, `stratum`, and `haul` columns which are integer, string, string, integer, and integer types respectively. With the exception of the year column these are all identifiers (categorical) with year being ordinal. 
- There were several columns on cpue (depending on the measure of effort) - we selected cpue_kgha or kilos per hectare of area swept. This is a continuous variable with a large number of zeros. We selected cpue in order to standardize across different degrees of effort (thereby removing some features that would be required in the model).
- Associated with each of these hauls is information on the bottom depth and surface depth (continuous in Celsius), the depth of the haul itself (continuous in meters), the width and height of the net (in meters, continuous), the duration of the haul (in hours continuous), and the distance fished (km continuous). In earlier years the net height was not recorded and so we left it out of the analysis. Given the consistent 5-6 km/h speed across the data the duration fished was kept and the distance fish discarded as they virtually capture the same data. The width of the net was excluded as it is more or less captured in the area swept during the haul if one knows the distance fished. 
- Scientific name was a string designating the taxon chosen (although it could be a list of species or a genus) and taxon confidence an enum of levels 'High', nan, 'Moderate', 'Low', 'Unassessed' where nan corresponded to 0 values of abundance. 
- Finally there were columns indicating position and datetime but these were excluded as we're not interested in make spatio-temporal predictions beyond what the covariance of species tells us. 

- In total the data spanned 33,958 hauls over 42 distinct years and 7861 stations with 975 distinct taxonomic designations. 
- Many of those species had low taxonomic confidence or actually represented genuses or groups of species. After removing the species that had less than 95% of the non-zero abundance hauls with moderate or high levels of confidence we were left with 339 distinct taxonomic designations. After removing any multispecies designations we were left with 273 species. Finally removing any species that showed up in fewer than 5% of hauls left us with 66 species in total. 

- This left us with the columns
	- 'year', 'haul', 'station', # identifies the haul
	- 'srvy', 'stratum', # identifies the survey area
	- 'duration_hr', # haul distance information
	- 'surface_temperature_c', 'bottom_temperature_c', # temperature information,
	- 'depth_m', # depth information
- With an additional column per species indicating its cpue_kgha for that haul
- duration_hr follows a biomodal distribution with peaks at 15 and 30 minutes
- surface temperature follows a single mode, slightly right skewed distribution centered at ~7c whereas bottom temperature follows a left skewed single mode distribution centered at ~4c
- Depth is single mode and highly right skewed with srvy stratum, station and haul all being unorderable categorical variables. year is ordinal. 
- The species distributions are typically left skewed 

### Issues

-  4.7% of hauls were missing bottom temperature data and 2.5% missing surface temperature data
- Most of the cpue data is zeros but this shouldn't be an issue given we are dividing the problem into occurrence and abundance problems 
- None of these distributions are normal and there will definitely need to be normalizing of the cpue data 
- The largest challenge is just going to be how many different species there are even after the filtering and determining useful methods for removing outliers and the like programmatically as I won't be able to comb through each and every species on its own. 

And we've got a draft!

Next steps are to edit everything I've got there and then add a section explaining why this isn't actually a massive project... but I've got something I could submit if I suddenly got ill or something :) 