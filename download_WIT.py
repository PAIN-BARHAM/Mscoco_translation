#%%
from datasets import load_dataset
dataset = load_dataset('ArImT/WIT_test')

#%%
data = dataset.data
# %%
data["test"].column_names
# %%
len(data["test"])
# %%
for i, item in enumerate(data["test"]["caption_reference_description"]):
    print(item)
    # print(data["test"]["image_url"][i])
    # print(data["test"]["caption_reference_description"][i])
    # print(data["test"]["meta"][i])
    # print(data["test"]["image"][i])
    if i ==3:
        break
# %%
data["test"]["image_url"]
# %%
type(data)
data
# %%
import pandas as pd

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data, columns = ['image_url', 'caption_reference_description', 'meta', 'image'])


# Display the resulting DataFrame
print(df)
# %%
import json

# Example dictionary
# data = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Convert dictionary to JSON and write to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=3, ensure_ascii=True)
# %%
import pandas as pd
from datasets import load_dataset

# Load dataset
dataset = load_dataset('ArImT/WIT_test')

# Get the data as a list of dictionaries
data = dataset['test']

#%%
# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Display the resulting DataFrame
print(df.head())
# %%
print(df.head())

# %%# %%
