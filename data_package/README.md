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
```python
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

## Notes

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
  but any method for creating `Catalog` object would do.

