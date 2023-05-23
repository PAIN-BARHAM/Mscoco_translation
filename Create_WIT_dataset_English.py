#%%
import pandas as pd
from datasets import load_dataset
from tqdm.notebook import tqdm


# %%
import pandas as pd

updated_data = pd.read_csv("WIT_test.csv", encoding="utf-8")
#%%
updated_data.columns
#%%
updated_data.head()
# %%
updated_data.drop(columns=["Unnamed: 0", "meta", "caption_reference_description"], inplace=True)
# %%
updated_data
# %%
updated_data["image_url"][0]

# %%
#Check the extensions for the dataset
#Create a dictionary to store extensions and their counts
extensions = {}

for index, row in updated_data.iterrows():
    image_url = row['image_url']
    print(image_url)
    print(image_url.split(".")[-1])
    extension = image_url.split(".")[-1]
    if extension in extensions:
        extensions[extension] +=1
    else:
        extensions[extension] = 1


extensions
#%%
# We have the following extensions:
{'jpg': 770,
 'gif': 10,
 'png': 107,
 'JPG': 106,
 'PNG': 10,
 'svg': 46,
 'jpeg': 9,
 'GIF': 2,
 'JPEG': 2
 }
#%%
# We will only keep the jpg, JPG, png, PNG, jpeg, and JPEG images
# We will remove the rest
# We will also remove the gif and svg images

import pandas as pd
import os


Images_not_downloaded = []
# Loop through the rows of the DataFrame and download each image

for index, row in updated_data.iterrows():
    
    image_url = row['image_url']

    extension = image_url.split(".")[-1]
    print(extension)
    if extension in ["jpg", "JPG", "png", "PNG", "jpeg", "JPEG"]:

        # image_url = row['image_url']
        try:
            response = requests.get(image_url, headers=headers)
            response.raise_for_status()  # check if the response was successful
            filename = f"{index}.{extension}"  # generate a unique filename
            with open(os.path.join("images", filename), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
        except requests.exceptions.HTTPError as e:
            print(f"Error downloading {image_url}: {e}")
            Images_not_downloaded.append(index)
    
    else:
        print("not downloaded")
        Images_not_downloaded.append(index)
    # if index ==5:
    #     break

#%%
# We will only keep the jpg, JPG, png, PNG, jpeg, and JPEG images
# We will remove the rest
# We will also remove the gif and svg images

#%%

!pip install ipywidgets

#%%
import requests
import pandas as pd
import os
from tqdm.notebook import tqdm
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

Images_not_downloaded = []
annotations = []

counter = 0
# Loop through the rows of the DataFrame and download each image

for index, row in tqdm(updated_data.iterrows(), total=len(updated_data)):
    
    image_url = row['image_url']

    extension = image_url.split(".")[-1]
    # print(extension)
    if extension in ["jpg", "JPG", "png", "PNG", "jpeg", "JPEG"]:

        # image_url = row['image_url']
        try:
            response = requests.get(image_url, headers=headers)
            response.raise_for_status()  # check if the response was successful
            filename = f"{counter}.{extension}"  # generate a unique filename
            with open(os.path.join("images", filename), 'wb') as f:
                f.write(response.content)
            # print(f"Downloaded {filename}")
            
            image_dict = dict()
            
            image_dict["image_id"] = counter
            image_dict["id"] =  counter
            image_dict["caption"] = updated_data["en_translation"][index]
            image_dict["image_name"] = filename
            #print("image", image_dict)

            annotations.append(image_dict)

            counter+=1

        except requests.exceptions.HTTPError as e:
            print(f"Error downloading {image_url}: {e}")
            Images_not_downloaded.append(index)
    
    else:
        # print("not downloaded")
        Images_not_downloaded.append(index)

    # print(annotations)
    # if index ==5:
    #     break
#%%
print(annotations)

#%%
import json


pd.DataFrame(Images_not_downloaded).to_csv("Images_not_downloaded.csv", encoding="utf-8")
json_data = json.dumps({"annotations": annotations}, ensure_ascii = False, indent=3)

print(json_data) 

with open("WIT_test_dataset.json", "w",  encoding="utf-8") as f:
    f.write(json_data)