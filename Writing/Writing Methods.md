- There will be a section per objective.
- Methods are phrased as to achieve X we did Y because of Z
- If Y is not precise enough we will then break down Y into sub-objectives
- Paragraphs here are elaborative or evidential 
- Written so there is no longer any "we did" in the rest of the paper

Turning now to the architecture of methods. Surprisingly the book I read had very little to say about methods except one thing - to use a lead/development structure where you summarize the goal and the method and then follow along with details. Something like:

In order to provide likelihoods per depth bin we applied probabilistic deep learning to classify fish into bins as deep learning has proven very capable of learning non-linear, combinatorial patterns (...). Specifically, each training example corresponded to one fish at a specific location and time. Then a fish's "classification" was defined as the depth bin it occupied at that moment and features were the environmental and/or temporal covariates associated with each depth bin at that position in space and time. Finally, we used categorical cross entropy as the loss function. This combination of choices results in a classifier that predicts the likelihood of depth bin occupancy per fish using the features provided. While deep learning was selected for its learning flexibility, that same flexibility means that deep learning is prone to overfitting (...). 

To deal with overfitting... 

In this example I've added some structure beyond the book:
-  I added a "why" to my lead which gives me a "to do X we did Y because of Z" as opposed to the book which suggests a to "do X we did Y". 
- After my "lead", my details immediately goes into elaborating on how the method was applied
- Followed by some new problems/objectives that need to be resolved for this method to work

The idea is that I can very naturally form a hierarchy in this way starting from a specific objective and then working my way down into the details. But as I drive into the details I'm making it clear why these details matter at each step. 

This leads me think that my methods section should parallel my objectives and work into detail as needed. However I more often see methods start with a "data" section and then follow that with what is more or less a linear list of instructions without a whole lot of explanation as to why those steps were taken. 

#### Follow-up

The purpose of a methods section is to provide a recipe so clear that folks totally get it and could follow it to the tee. 

It's organized first by objective where we explain to achieve X we did Y because of Z. The rest of the paragraph elaborates on this to provide elaboration and justification. From there a following paragraphs lays out the steps (sub-objectives) required to apply Y. These steps should be small enough they deal with one outcome at a time but not so small that you're splitting hairs. 

Then you go through each of the steps and provide elaboration and evidence to both justify the step and make it as clear as humanely possible. 

And that's your recipe! 


- Did you provide a sense of where the data is from and how voluminous it is? 
