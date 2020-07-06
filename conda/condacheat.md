# Conda cheat sheet
--

##### List all environments

```
$ conda info -e
```

##### Adding channels
>via .condarc

```
$ cat ~/.condarc
ssl_verify: true
channels:
  - conda-forge
  - bioconda
  - defaults
```

##### Create a new environment

```
$ conda create --name <myenv> <package>=<version>
```

##### Activating and Deactivating environments

```
$ conda activate <myenv> 
$ conda deactiavte <myenv>
```

##### Updateing an environment from environment.yml file
```
$ conda env update --prefix ./env --file environment.yml  --prune
```
>The prune option removes any no longer needed dependencies

##### Removing an environment

```
$ conda remove --name <myenv> --all
```

##### To clean unnecessary cached files, tarballs, and stuff

```
$ conda clean --all
```

##### Export the environment

```
#Freeze the current environment into requirements.txt:
$ conda list --export > requirements.txt
#Freeze the current environment into environment.yml:
$ conda env export > environment.yml

```

--

####Example of environment.yml file

```
name: Environment name
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python=3.8
  - sample-sheet=0.12.0
```