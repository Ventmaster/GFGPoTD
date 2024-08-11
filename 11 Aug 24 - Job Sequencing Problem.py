# 11th August 2024
# Job Sequencing Problem

class Job:
    
    # Job class which stores profit and deadline.
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        
        # Sorting jobs by decreasing order of profit
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Finding the maximum deadline to create a timeline
        max_deadline = max(job.deadline for job in Jobs)
        
        # Timeline to keep track of free slots (initialized to None)
        timeline = [None] * (max_deadline + 1)
        
        job_count = 0
        max_profit = 0
        
        # Iterating over each job
        for job in Jobs:
            # Try to find a slot from job.deadline to 1
            for t in range(job.deadline, 0, -1):
                if timeline[t] is None:
                    # Slot found, schedule the job
                    timeline[t] = job.id
                    job_count += 1
                    max_profit += job.profit
                    break
        
        return job_count, max_profit
