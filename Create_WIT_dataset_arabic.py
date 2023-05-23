#%%
from google.cloud import translate_v2 as translate

# %%
# Instantiates a client
translate_client = translate.Client()

# %%
# https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to
# https://cloud.google.com/sdk/docs/install#deb

#%%
# The text to translate
text = 'مرحبا بالعالم'

# The target language
target = 'en'

# Translates some text into English
translation = translate_client.translate(text, target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
# %%
# import pandas as pd

# # %%
# Translated_Dataset = pd.read_csv("Translated_Dataset.csv", encoding="utf-8")

# #%%
# from tqdm.notebook import tqdm
# # %%
# # read the scentence column named "sentences" and extract the raw text from it

# for i in tqdm(range(1,6)):
#     Translated_Dataset[f"sentence_{i}"] = ' '
#     Translated_Dataset[f"ar_sentence_{i}"] = ' '
# Translated_Dataset.head()

#%%
import pandas as pd
from datasets import load_dataset

# Load dataset
dataset = load_dataset('ArImT/WIT_test')

# Get the data as a list of dictionaries
data = dataset['test']

#%%
# Convert to pandas DataFrame
data = pd.DataFrame(data)

# Display the resulting DataFrame
print(data.columns)
# %%
for i, item in enumerate(data["caption_reference_description"]):
    print(item)
    # print(data["test"]["image_url"][i])
    # print(data["test"]["caption_reference_description"][i])
    # print(data["test"]["meta"][i])
    # print(data["test"]["image"][i])
    if i ==3:
        break
#%%
data["en_translation"] = ' '
# %%
data.columns

#%%
data.head

#%%
data.drop(columns=["image"], inplace=True)
#%%# %%

from tqdm.notebook import tqdm

#%%

errors = []
#%%                             
for i, item in tqdm(enumerate(data["caption_reference_description"])):

    # import ast
    # # convert the string to a list of dictionaries
    # try:
    #     lst = ast.literal_eval(Translated_Dataset["sentences"][i])
    # except SyntaxError:
    #     print(i)
    #     print("Syntax Error")
        
    # extract the raw values from each dictionary

    # for j, d in enumerate(lst):
    #     # print(d['raw'])
    #     Translated_Dataset.loc[i, f"sentence_{j+1}"] = d['raw']
    #     # print(j+1)
    #     # print(Translated_Dataset.loc[i, f"sentence_{j+1}"])

    # for j, d in enumerate(lst):
    # print(d['raw'])
    # Translates some text into English
    # print(item)
    try:
        translation = translate_client.translate(item, target_language=target)
        data.loc[i, "en_translation"] = translation['translatedText']
    except:
        print(f"Error in translation of {i}") 
        errors.append(i)

    if i%100==0:
        data.to_csv("WIT_test.csv", encoding="utf-8")
        print(i)


data.to_csv("WIT_test.csv", encoding="utf-8")

# %%
# %%
data.to_csv("WIT_test.csv", encoding="utf-8")

#%%
errors
# %%
# for i, item in tqdm(enumerate(Translated_Dataset["sentences"][38208:], start=38208)):
#     print(i)
# %%
import pandas as pd

updated_data = pd.read_csv("WIT_test.csv", encoding="utf-8")
# %%
updated_data.drop(columns=["Unnamed: 0", "meta", "en_translation"], inplace=True)
# %%
updated_data
# %%
updated_data["image_url"][0]
# # %%
# import requests
# import pandas as pd
# import os
# # Read the CSV file into a pandas DataFrame
# # df = pd.read_csv('data.csv')
# # Set the User-Agent header to a valid value
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }


# Images_not_downloaded = []
# # Loop through the rows of the DataFrame and download each image

# for index, row in updated_data.iterrows():
#     image_url = row['image_url']
#     try:
#         response = requests.get(image_url, headers=headers)
#         response.raise_for_status()  # check if the response was successful
#         filename = f"{index}.jpg"  # generate a unique filename
#         with open(os.path.join("images", filename), 'wb') as f:
#             f.write(response.content)
#         print(f"Downloaded {filename}")
#     except requests.exceptions.HTTPError as e:
#         print(f"Error downloading {image_url}: {e}")
#         Images_not_downloaded.append(index)
    
#     # if index ==5:
#     #     break

# %%
# Images_not_downloaded
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

for index, row in tqdm(updated_data.iterrows()):
    
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
            image_dict["caption"] = updated_data["caption_reference_description"][index]
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
#%%
# Remove the images that were not downloaded
# # updated_data.drop(Images_not_downloaded, inplace=True)
# #%%
# Images_not_downloaded
# # %%
# len(Images_not_downloaded)
# # %%


# import json

# annotations = []


# for index, row in updated_data.iterrows():
#     image_url = row['image_url']


#     extension = image_url.split(".")[-1]
#     filename = f"{index}.{extension}"
#     if index in Images_not_downloaded:
#         print("not downloaded")
#     else:

#         image = dict()
        
#         image["image_id"] = index
#         image["id"] =  index
#         image["caption"] = updated_data["caption_reference_description"][index]
#         image["image_name"] = filename
#         print("image", image)

#         annotations.append(image)


# #%%
# import json

# json_data = json.dumps({"annotations": annotations}, ensure_ascii = False, indent=3)

# print(json_data) 

# with open("WIT_test_dataset.json", "w",  encoding="utf-8") as f:
#     f.write(json_data)
# %%
