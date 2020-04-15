import intake
import os
here = os.path.abspath(os.path.dirname(__file__))

# the catalog is a YAML file in the same directory as this init file
cat = intake.open_catalog(os.path.join(here, 'sea.yaml'))
data = cat.sea_ice()  # <- note the parentheses

# after installation, this will be available as intake.cat.sea_cat, with one entry, sea_ice
# and intake.cat.sea_data, which is a data source.
# intake.cat.sea_cat.sea_ice and intake.cat.sea_data are identical.
