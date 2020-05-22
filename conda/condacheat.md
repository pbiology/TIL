# Conda cheat sheet
--

List all environments:

```
$ conda info -e
```

Adding channels - via .condarc

```
$ cat ~/.condarc
ssl_verify: true
channels:
  - conda-forge
  - bioconda
  - defaults
```

Create a new environment:

```
$ conda create --name <myenv> <package>=<version>
```

Activating/Deactivating environments

```
$ conda activate <myenv> 
$ conda deactiavte <myenv>
```

Removing an environment:

```
$ conda remove --name <myenv> --all
```

To clean unnecessary cached files, tarballs, and stuff:

```
$ conda clean --all
```

Export the environment

```
#Freeze the current environment into requirements.txt:
$ conda list --export > requirements.txt
#Freeze the current environment into environment.yml:
$ conda env export > environment.yml

```