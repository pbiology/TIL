# git cheat sheet
--

##### Change the message of the last commit

```
$ git commit --amend -m "New commit message."
```

##### Working with issues connected to progress kanban board
>These requires the GitHub cli 

1 - Make a ToDo item into an issue (which gets auto added to projects ToDo)

```
$ gh issuecreate --title "Title text here" --body "Body text here" -l "label, for instance enhancement" -p "project name"
```

_For ease of use the following function can be used:_

```
function ghni() {
    gh issue create -t $1 -b $2 -l enhancement -p $3
}
```

2 - Progress ToDo to In Progress (by closing and reopening issue)

```
$ gh issue close <issue num>
$ gh issue open <issue num>

```

_For ease of use the following function can be used. 
This will also auto make a new breanch to work on_

```
function ghpi() {
    if  [[ "$#" == 0 ]]; then
        echo >&2 "Usage: ghpi issue_num issue_name"
        exit 0
    fi
    gh issue close $1
    gh issue reopen $1
    git checkout -b issue/${1}/$2
}
```

3 - To finish the work, after the new branch has been merged with the master/dev branch, close the issue

```
$ gh issue close <issue num>
```