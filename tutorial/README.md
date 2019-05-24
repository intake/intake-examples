# Announcing: Intake

#### *Taking the pain out of data access*

We are pleased to release Intake, a simple data access layer and cataloging system.

This article contains code executable with Binder: 
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/martindurant/intake-release-blog/master)

## Introduction

Defining and loading data-sets costs time and effort.
The data scientist needs to know what data are available,
and the characteristics of each data-set, before going to the effort of loading
and beginning to analyse some specific data-set. Furthermore, they might need
to learn the API of some Python package specific to the target format. The code
to do such data loading often makes up the first block of every notebook or script,
propagated by copy&paste.

Intake has been designed as a simple layer over other Python libraries to
- provide a consistent API, so that you can investigate and load all of your data with
the same commands, without knowing the details of the backend library
- a simple cataloging system using YAML syntax, enabling, for every data-set,
a description of 
  - which plugin is to load it
  - arguments to pass
  - arbitrary metadata to associate with the data
- transparent access to remote catalogs and data, for most formats
- a minimalist plugin system, so that new loaders, remote containers, and many other
components can be contributed to Intake with a minimum of fuss.
- an optional server-client infrastructure, so that you can serve a set of catalogs and
stream data that the client doesn't have direct access to.

For a simple design and relatively small code-base, there are lots of features. We
will describe the main ones here from three points of view in the sections that follow.
However, Intake is *very new*, and its design and implementation are up for discussion
and change in the true spirit of open source. Please refer to the 
[documentation](https://intake.readthedocs.io/en/latest/), and post problems, questions
and comments to the [issue tracker](https://github.com/ContinuumIO/intake/issues).

#### Installation

The easiest method is to use `conda`:

```bash
conda install -c intake intake
```

Several additional packages are available with plugins for various formats. See the
[informal directory](https://intake.readthedocs.io/en/latest/plugin-directory.html).

## Usage Scenarios

### Data Scientist

Intake provides an easy way to find your data, locally, in a cloud service, or
on an Intake server.

```Python
import intake
intake.cat         # set of installed data-sets
cat = intake.open_catalog('directory/catalog.yaml')      # some local catalog file
cat = intake.open_catalog('s3://bucket/data/cat*.yaml')  # remote set of catalog files
cat = intake.open_catalog('intake://host:5000')          # an Intake server
```

In each case, `list(cat)` will provide the set of available data-sets in a
catalog, and you can access the entries using attribute dot-notation to either
interrogate the entry (e.g., read the text description), or to directly load the data.
In general, a catalog can contain any number of entries, and can also reference
other catalogs, local or remote, in a hierarchical manner.

```Python
list(cat)                 # set of entries
cat.us_crime.describe()   # basic description of an entry
cat.us_crime.plot()       # quick-look plotting
df = cat.us_crime.read()  # get all of the data in one shot
```

The output of `read()` will be one of a small number of python containers appropriate
to the data, in this case a Pandas data-frame. The two other built-in containers are
numpy n-dimensional arrays and list-of objects. Each of these also has an out-of-core,
parallelised version available with the `.to_dask()` method. 
 
The linked notebook shows an example workflow for a data scientist.
 
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/martindurant/intake-release-blog/master?filepath=data_scientist.ipynb)

### Data Engineer

Intake allows the separation of the definition of data sources from their use
and analysis. This allows the data engineer to get on with deciding where data
should be stored, in which format, and which package is best suited to load each
data-set, so long as the data scientist, above, gets the data-frame they need
(or other data object!).

Consider, for instance, maintaining a catalog file on a cloud service, and pointing
users to it. It may be that, originally, the data was in CSV format, with the
problems of data volume and parsing load this entails. The engineer could swap out
the catalog entry definition for an optimized binary version, without the end user
noticing the difference. In a project or institutional setting, the catalog can
be the "point of truth" about the current best data-sets that should be in use.
Data-sets and catalogs can also be packaged, for version control and dependency
tracking.

Catalogs also provide a natural place to *describe* each data-set, with text and
arbitrary metadata. Such information can be for the users' benefit to help them
choose the right data-set for their problem, for analysis of the set of entries
themselves, or as a way to pass parameters to downstream tools that work with Intake
(e.g., the [plotting](https://intake.readthedocs.io/en/latest/plotting.html#persisting-metadata)
system).

Finally, catalogs can also encode user parameters, giving either natural choices
to the end user (e.g., to filter a data set, or choose between version A and B),
or for getting information required for data access from the user's environment
(e.g., credentials defined in environment variables).

The linked notebook shows an example workflow for a data engineer.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/martindurant/intake-release-blog/master?filepath=data_engineer.ipynb)

### Developer

The Intake codebase is intended to be approachable and very pluggable. It should
be easy to to create new data loader plugins (see the [CSV](https://github.com/ContinuumIO/intake/blob/master/intake/source/csv.py#L7)
and [textfiles](https://github.com/ContinuumIO/intake/blob/master/intake/source/textfiles.py#L4)
prototypes classes). Even writing new auth mechanisms (beyond the [very simplistic](https://github.com/ContinuumIO/intake/blob/master/intake/auth/secret.py#L8)
one) or replacing the Intake server with a whole new implementation is very
doable. These do not need to exist within the Intake repo, and creating complementary
packages is very much encouraged. We hope to cover not just the main data formats
already loadable by the likes of Pandas, but to catalog and access *all* data
such as fitted machine learning models, REST APIs and video formats. 

Such code can be distributed along the usual channels, and an entry in a
catalog can specify which module it requires to be installed, in order to be able to
load. Indeed, if distributing catalogs, then the appropriate dependency on the
plugin package can be declared.

Some suggestions of [plugin ideas](https://github.com/ContinuumIO/intake/issues/58) are
listed in a GitHub issue - please discuss and add your own!

The linked notebook shows an example workflow for a developer.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/martindurant/intake-release-blog/master?filepath=dev.ipynb)


## Summary

Intake provides a very simple yet useful division between the users of data, and
the maintainers of data source catalogs. Intake has approachable code and is extensible
in many places, and so hopefully can progress to become an all-inclusive data ecosystem
for numerical python.


--

This work was supported by Anaconda. Please note that the effort is still in the early
stages, so expect some rough edges!