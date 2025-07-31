I have these lovely plots of proportion vs time of day across the training, validation, and prediction sets. Problem is that they mean nothing. One cannot take from them that the daily cycle of fish is what is seen there because it is dependent upon the environmental features and depth distributions in each of those sets. If I really wanted to say - this is the daily pattern I'd need to compare it to a pattern that knows nothing of the day - i.e. the proportion from a model trained without that feature but with all of the others. Then I could look at the difference and find out what the expected difference is given all of those features. But this too would be clouded because there could be a non-linear relationship inherent here as well. The only way to truly know what's going on would be to hold everything else constant and then only vary the one feature - something I can do in inference but not necessarily in the data. 

The problem I'm getting at here is this makes it very difficult to make meaningful comparisons between the training and testing data. Well... sort of... 

Suppose I wanted to know whether the diel patterns were correct. I could gather up all of my data, bin it out by the features I do have (environmental and seasonal in my case) and then figure out what the mean would be if I just ignored the day/night piece. Or rather what would be the prediction that would give me the lowest loss. 

In my data I can take a group of samples that more or less represent the same complementary feature space distribution across a series of values of my target feature. I.e. each season, salinity, ... sample there is representation of my whole target feature's range. Now because the complementary features are fixed across these the best my model can do (without diel) is predict a specific proportion itself based on a kind of average. However as my target feature varies we do see changes in the average being taken. The extent to which my model is able to follow those differences indicates the degree to which it is "correct". 

Now my model is actually solving for the geometric mean (the likelihood of the data). 

For each of my complementary samples there would be an associated probability $p_i$. Where we see sample $i$ $n_i$ times. Our model is effectively solving for:

$$\max\prod_i p_i n_i$$ The expectation of this would be:

$$\frac{\sum_i p_i n_i}{\sum_i n_i}$$
If we suppose that there is some probability $p_i$ that is actually represented in the real data associated with that particular sample then, yes, the model should capture that $p_i$ and therefore give us the expectation over the whole set. 

----

What I'm doing here is dividing this into two separate problems. 

1. *Comparing to Actuals*: in this we just want to know whether a single feature's drive of model outcomes is accurately representing the data we have. For this you take all other features and make sure you have sampled the full distribution of the target feature for each underlying sample. Then you note that without the feature it would predict one proportion, but instead it is actually capturing a varying value. However you cannot look to the actuals to tell you how a feature behaves because you would need to hold all features constant which you usually cannot. I.e. you will have the pattern from your feature conditioned on the specific distribution of other features in your data. 
2. *What does the feature do?*: Here you use the model to hold everything constant except your one feature and then you swing it along. 

Okay apparently this is called counterfactual analysis. (Although that is a pretty broad umbrella term)

This counterfactual analysis is really about trying to understand where the model breaks down. We are subsampling things to do so... The model can learn a whole bunch of patterns from the training data that aren't real even if their average is. Is this just equivalent to choosing subsets of the data and then asking about loss?? 

----

Here's the question - a model can learn all sorts of patterns. Which ones are real? I.e., when I see my loss drop, for which subsets of the other features is it dropping? 

Counterfactual analysis is one way of dealing with this. But perhaps searching for where my loss becomes really poor could be another way... 