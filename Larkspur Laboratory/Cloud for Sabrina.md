- [ ] Run through her current workflow
	- [ ] What kinds of data are you using? What format, how large? Is it protected data in some way?
	- [ ] How often does the data change?
	- [ ] What are you configuring with each run? How often does configuration change?
		- [ ] Is this even configurable? 
	- [ ] What outputs are you retrieving? Is that sensitive data in any way?
	- [ ] What parts of the process are taking the longest? 
	- [ ] What does your feedback loop look like? 
- [ ] How many models are you actually building out?
- [ ] How long does convergence take at the moment? 

Options:
- EC2 with lots of cores
- Batch 
	- R script runner
	- Configure a model fit