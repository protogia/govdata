from interface import DKANClient
import pandas as pd

braunschweig = DKANClient(city="braunschweig", apiversion=3)

datasets = braunschweig.get_available_datasets()

df = pd.DataFrame(data=datasets)
print(df.head())