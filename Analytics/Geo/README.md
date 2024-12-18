# This is a description of the Geo process

This folder contains the notebook related to the geo plots for the dashboard, to properly run this data you may use the following files:
1. In the `geo.ipynb` can be found the process related to the geo maps.
2. In the path geo_data/geo_docs.zip of the instance `grp4_instn_001.unimelb-comp90024-2023-grp-4.cloud.edu.au` are the files asociated to this notebook
3. If is intended to reproduce the notbook outputs it is necesary to:
  a. Clone the git repo
  b. create a python venv and install requirements.txt
  c. Import the geo_docs.zip into the geo folder and see that the Input/Output path match the geo_docs path

The `geo.ipynb` file has 2 sections, the first section was **Create dataframes to use in maps**, in here we applied web scrapping to return the polygons to plot for Melbourne and Sydney:
a. Read json: Read SUDO data from json files 
b. Get SA1 and SA2 codes to scrape polygons from internet resources
c. Set and run WebScrapper to return data polygons
d. Save the polygons in a GeoJSON structure for the maps
e. Join the SA2 convention with the SUDO dataset for the maps
f. Return files in Output folder.

_**Note: This script part shall not be run again since the output files are already generated**_

The second section of the file is related to `Plotting maps`, to run only this section it is necessary to apply the steps in three, but in the geo_docs we will only use the output folder (*These are the only 4 files we need to plot the maps*).
