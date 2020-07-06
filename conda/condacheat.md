# Conda cheat sheet
--

### Managing environments
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
*OR*
conda env create -f environment.yml
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

### Example of environment.yml file

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
--

### Set what to show on the command line prompt
These settings are made in the .condarc file, most often located in the home folder

```
changeps1 (bool)  
# When set to 'True', will change the command prompt ($PS1) to 
# include the activated environment.

env_prompt: '({default_env})'
# Template for prompt modification based on the active environment.
# Currently supported template variables are '{prefix}', '{name}', and
# '{default_env}'. '{prefix}' is the absolute path to the active
# environment. '{name}' is the basename of the active environment
# prefix. '{default_env}' holds the value of '{name}' if the active
# environment is a conda named environment ('-n' flag), or otherwise
# holds the value of '{prefix}'. Templating uses python's str.format()
# method.
```