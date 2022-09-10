# return the latest job (in a sorted array) that doesn't conflict with job[i]
def last_nonconflict(jobs, i):
    for j in range(i-1,-1,-1):
        if jobs[j][1] <= jobs[i][0]:
            return j
    return -1

def jobs_scheduling(jobs):
    # sort jobs according to finish time
    jobs.sort(key=lambda x: x[1])

    # store the max profit obtainable taking jobs to or including ith
    a = [0 for _ in range(len(jobs))]
    a[0] = jobs[0][2]

    for i in range(1,len(jobs)):
        p = jobs[i][2] # current job profit

        j = last_nonconflict(jobs, i) # last job before job i
        if j != -1:
            p += a[j] # add the max profit of last job

        # maximum of including or excluding current job
        a[i] = max(p, a[i-1])

    return a[len(jobs)-1]

# Job ~ [start, finish, profit]
jobs = [[3, 10, 20], [1, 2, 50], [6, 19, 100], [2, 100, 200]]
print(jobs_scheduling(jobs))

