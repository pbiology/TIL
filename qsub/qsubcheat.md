# qsub cheat sheet
--

### Show stats

##### Show all jobs for all users:
`$ qstat -f -u "*"`

##### Show load on all queues:
`$ qstat -g c`

### Start and stop jobs

##### Kill a job
`$ qdel <JOB ID>`

##### Kill a jobs in a range
`$ qdel {18280..18285}`

##### Kill all jobs from a user
`$ qdel -u <USER ID>`

### Q-login
One can login to a node and reserve slots. And then start jobs inside the node
`$ qlogin -q wgs.q@kuat.medair.lcl -pe mpi 120`
