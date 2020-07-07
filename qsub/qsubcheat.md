# qsub cheat sheet
--

### Show stats

##### Show all jobs:
`$ qstat -f`

##### Show load on all queues:
`$ qstat -g c`

### Start and stop jobs

##### Kill a job
`$ qdel <JOB ID>`

##### Kill a jobs in a range
`$ qdel {18280..18285}`

##### Kill all jobs from a user
`$ qdel -u <USER ID>`