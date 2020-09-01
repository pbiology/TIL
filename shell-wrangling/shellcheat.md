# Shell wrangling cheat sheet

>Different small tools or shell oneliners to manipulate or view stuff

--

### Datamash
##### Transposing a file

```
$ cat <file> | datamash transpose
$ cat <file> | datamash transpose -t " " #Use whitespace instead of tab
```

##### Getting sum of a column 
> (column 1 in this case)

```
$ seq 3 | datamash sum 1 
6
```

### Paste
##### Making output into columns

```
$ seq 10 | paste - -
1	3	5	7	9
2	4	6	8	10 
```

### Column
##### Make nice columns in csv files and others

```
$ column -s "\t" <file> | less -S
```
> Added as function "cls"

### Disown foreground processes

```
# Stop process using ctrl-z
$ bg 1 #Starts in background
$ disown -h 

``` 

### Screen 
Starting screen with a name, for easier identification of the session

```
$ screen -S <session name>
```
