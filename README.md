# uk-rail-stations

A JSON list that (should) contain every Rail station in the UK, along with its TIPLOC, CRS, Station name, Latitude and Longitude coordinates, sourced from the DFT's National Public Transport Access Nodes (NaPTAN) list.

## Building the JSON file
To build the JSON file, you'll need to download a copy of the dataset in XML from the DFT [here](https://www.data.gov.uk/dataset/ff93ffc1-6656-47d8-9155-85ea0b8f2251/naptan) (note the file is about 560MB).

Once done, drop the XML file into the repo's folder, and install ``xmltodict``, either by running ``pip install xmltodict`` or ``pip install -r requirements.txt``. When you run ``generateList.py`` about 2 minutes later you should have a finished stations.json file.

### Some shortfalls to be aware of
- The NaPTAN XML file does not include lat/long positions for Elizabeth Line (Crossrail) stations in the Central Operating Section, and as such they are (currently) not in the generated JSON file.
- "Aberdare Platform 2" is technically considered a separate station by Network/National Rail, and has its own TIPLOC and CRS, but **not** by NaPTAN, so does not appear in the XML file. It has been manually added into this repo's stations.json however.

There might be other shortfalls I'm not aware of that are present too, though I'm yet to come accross them while using this dataset in another project I'm working on.

## Attribution
Contains public sector information licensed under the Open Government Licence v3.0.