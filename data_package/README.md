# Intake Example Package

A very simply python package structure showing how to
"install data" using only setuptools / pip and
*not* requiring `conda`. 

This is done using the `entrypoints` keys in `setup.py`:

```python
    entry_points={
        'intake.catalogs': [
            'sea_cat = intake_example_package:cat',
            'sea_data = intake_example_package:data'
        ]
    }
```

### Explanations

- `entry_points`: this key is required, states that this
  information is to be accessible using the 
  [entrypoints](https://entrypoints.readthedocs.io/en/latest/)
  package. This is a dependency of Intake, you should not need
  to install it separately.
- `'intake.catalogs'`: marks the list that follows as a set of
  installed catalogs
- 'sea_cat = intake_example_package:cat': the first identifier is
  the name to give in the builtin catalog, and the second part is a reference to
  the catalog object, as `module:object` .
- 'sea_data = intake_example_package:data': very similar to the previous
  line, but this time referencing a data source rather than a catalog. Remember
  that, in Intake, a catalog is just another data source.

Effectively, this does the following once the package is installed: 
set the "sea_cat" entry in
`intake.cat` to reference the "cat" catalog object in `intake_example_package`,
and "sea_data" to reference the "data" data source.


## Try it:

In this directory, run install, one of
- `python setup.py develop`
- `python setup.py install`
- `pip install -e .`
- `pip install .`
(the "develop" or "-e" versions use links rather than copying files; you may also need to add
options for "user" installs if you don't have write permissions in your environment)

Or if you don't want to download and extract,
- `pip install git+https://github.com/intake/intake-examples#egg=intake_example_package&subdirectory=data_package`

Following that, you can try in python, and see both entries in action:
```
>>> import intake
>>> list(intake.cat)  # may have more entries here
['sea_cat', 'sea_data']
>>> list(intake.cat.sea_cat)  # this is a catalog
['sea_ice']
>>> intake.cat.sea_cat.sea_ice.read().head()
      Time  Arctic  Antarctica
0  1990M01   12.72        3.27
1  1990M02   13.33        2.15
2  1990M03   13.44        2.71
3  1990M04   12.16        5.10
4  1990M05   10.84        7.37
>>> intake.cat.sea_data.read().head()
      Time  Arctic  Antarctica
0  1990M01   12.72        3.27
1  1990M02   13.33        2.15
2  1990M03   13.44        2.71
3  1990M04   12.16        5.10
4  1990M05   10.84        7.37
```

The data source also comes with a predefined plot, so you can visualise that (in a notebook
or via the viz server) or run the interactive dataframe viz GUI. Enjoy!

### Notes

- Intake does not import the module, unless a user uses the entry
- In this example, the two data sources created in the init
  of a package, but it could have been a single module, or conversely,
  within a sub-package
- the `package.module:object` should refer to the original definition
  of the object, where it is instantiated; i.e., if you have a
  package init with a statement like `from .data import mycat`,
  you should reference `package.data:mycat` and *not* 
  `package:mycat`
- The catalog object here is created with `intake.open_catalog`,
  but any method for creating `Catalog` of any other data source object would do.

## Distribute

### To PyPI

Since this directory forms a complete python package, you could upload it to
[pypi](https://pypi.org/). For example, the following commands would do the
job

```bash
> python setup.py sdist bdist_wheel
> twine upload dist/*
```
(this assumes you have `twine` installed and have a valid account on PyPI).

If you were to try the above command, you would find that the package name is already taken
by the Intake authors, but you can use this pattern to upload your own package names
for your own data/catalogs. In this case, it make it possible for anyone else to then
install the data package using
```bash
> pip install intake_example_package
```
(instead of the installation lines in the "Try it" section, above)

Note that it would be good practice to modify `setup.py` to include further information
such as a detailed description/readme, all dependencies and their required versions,
licencing, etc., before building and uploading anything.
Note that `setup.py` specifically includes YAML file. You could, in theory,
include data files directly in such packages, but in practice, PyPI packages should be small,
and the data referenced remotely.

### Build your own conda package

The folder `conda/` contains a simple recipe for conda. Assuming you have `conda-build`
installed, you can run

```bash
conda build conda/
```

and either share the resultant file directly, or upload the file to your channel (the command
will be printed to the console when the package build is done).

This example can be found on [anaconda cloud](https://anaconda.org/intake/intake_example_package)
and installed using
```bash
> conda install -c intake intake_example_package
```

Of course, here you would substitute the name and channel appropriate for your data package.

### Using conda-forge

`conda-forge` provides an automated and uniform way to build and upload conda packages, which
will appear on the popular `conda-forge` channel. It will notice when new version are uploaded
to PyPI, and automatically build new versions.

Full instructions on how to submit a package for inclusion in `conda-forge` can be
found in [their documentation](https://conda-forge.org/docs/maintainer/adding_pkgs.html).
The eventual installation line would look something like

```bash
> conda install -c conda-forge newdatapackage
```
