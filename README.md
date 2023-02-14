Intake Examples
===============

This repository includes example notebooks and data packages for intake.

They should run locally if you download this repository. They are also available in a running environment on the cloud by clicking on the link below:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/intake/intake-examples/master)

## Tutorial

The subdirectory `tutorial/` contains three notebooks describing work-flows for three different
[roles](https://intake.readthedocs.io/en/latest/index.html) by which you
might interact with Intake. The separation of concerns is important, so that each person can concentrate on the
job that they have in front of them with clear communication paths between each. It may be that in a small
organisation, a person fulfills multiple of these roles, but it is still useful to consider problems from each
vantage in turn:

* [data scientist](tutorial/data_scientist.ipynb) - for the end-user who want to find, load and analyse their data
* [data engineer](tutorial/data_engineer.ipynb) - for the curator of data and catalogues, who decides how best to
  store and expose data
* [developer](tutorial/dev.ipynb) - for authors of new drivers and other extensions to Intake's capabilities. This
  person does not necessarily develop any code for the Intake package itself.

## Data Packages
This directory contains examples of Intake catalogs and scripts:

* [data-us-states](data-us-states/) - Conda data package with embedded data (see docs for more details). Available
  via `conda install -c intake data-us-states`.
* [airline_flights](airline_flights/) - Conda data package with external data and extra dependencies. Available via
  `conda install -c intake airline_flights`.
* [us_crime](us_crime/) - Conda data package used in plotting documentation. Available
  via `conda install -c intake us_crime`.
* [nyc_taxi](nyc_taxi/) - Full cloud-based installable dataset of Taxi trip data in NYC in parquet format. Available
  via `conda install -c intake nyc-taxi`.
* [precip](precip/) - Precipitation data with example notebook
* [data_package](data_package/) - generic/pip-installable package prototype

## Other examples

The following example is an online data-set listing automatically generated from an Intake
catalog:

* [pangeo catalog](http://pangeo.io/catalog.html) - List of earth science products for the Pangeo project
