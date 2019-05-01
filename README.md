Intake Examples
===============

This repository includes example notebooks and data packages for intake.

They should run locally if you download this repository. They are also available in a running environment on the cloud by clicking on the link below:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/intake/intake-examples/master)


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

## Other examples

The following example is an online data-set listing automatically generated from an Intake
catalog:

* [pangeo catalog](http://pangeo.io/catalog.html) - List of earth science products for the Pangeo project
