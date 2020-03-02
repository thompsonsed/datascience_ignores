# Datascience defaults for .gitignore

Based on the set of default gitignores from [Equinor](https://github.com/equinor/data-science-template/blob/master/.gitignore).

Running the python script will either create a new gitignore in the provided directory (or current directory by default) from the *default_ignores.txt* file, or append the contents of *default_ignores.txt* to the provided text file.

## Usage

Run `python create_gitignore.py -d path/to/dir` to create a *.gitignore* at the given path or directory. If `-d` is not supplied, uses the current directory.

Add the following to your `.bash_profile` or `.zshrc` to use the function from anywhere.

If you have already added the defaults to the .gitinore file, the defaults will not be added a second time.

`alias create_gitignore="python3 /path/to/datascience_ignores/create_gitignore.py"`

## Contact

thompsonsed@gmail.com