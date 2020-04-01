import intake
import os
here = os.path.abspath(os.path.dirname(__file__))

cat = intake.open_catalog(os.path.join(here, 'sea.yaml'))

# after installation, this will be available as intake.cat.sea, with one entry, sea_ice
