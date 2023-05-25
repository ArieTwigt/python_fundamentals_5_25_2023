#%%
import requests
import pandas as pd

merk = input("Welk merk?:\n")
merk_upper = merk.upper()
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={merk_upper}"

response = requests.get(endpoint)

data = response.json()

#%%
data[0]['kenteken']
# %%
data_df = pd.DataFrame(data)
# %%
data_df.to_csv(f"export_{merk}.csv",sep=";", index=False)


data[1]['merk']