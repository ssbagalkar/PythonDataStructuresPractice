"""Given an array of jobs where every job has a deadline 
and associated profit if the job is finished before the deadline. 
It is also given that every job takes single unit of time, so the
 minimum possible deadline for any job is 1. How to maximize 
 total profit if only one job can be scheduled at a time."""

## https://www.geeksforgeeks.org/job-sequencing-problem-set-1-greedy-algorithm/

def jobs_scheduling(jobs):
	# Sort all jobs according to profits
	sorted_jobs = sorted(jobs,key=lambda x:x[2], reverse = True)
	
	# take max deadline
	max_deadline = max(sorted_jobs,key=lambda x:x[1])[1]
	
	#None array to store jobs sequence
	output_sequence = [None]*max_deadline
	
	for ii in range(len(jobs)):
		# Check if deadline is available in array and fill it
		current_deadline = sorted_jobs[ii][1]
		for jj in range(current_deadline-1,-1,-1):
			if output_sequence[jj] is None:
				output_sequence[jj] = sorted_jobs[ii][0]
				break
				
	return output_sequence			
	
	



## Format- [job--> string, deadline(say hours)--> int, profit(say $$)--> int]
jobs = [['j1',2, 100], ['j2', 1, 19], ['j3', 2, 27], ['j4', 1, 25], ['j5', 3, 15]]
## output--> job schedule --> strings like in this case 'j1' 'j3' 'j5'
print(jobs_scheduling(jobs))