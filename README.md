# opendata
Python-client-library to fetch data from opendata-sources via DKAN-REST-API.

## install 
```bash
git clone 
python -m pip install .
```

## usage
```py
import pandas as pd

braunschweig = DKANClient(city="braunschweig", apiversion=3)

datasets = braunschweig.get_available_datasets()

df = pd.DataFrame(data=datasets)
```

## run tests
```bash
python -m unittest tests.test_interface
```

