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
import pandas as pd

# %%
Translated_Dataset = pd.read_csv("Translated_Dataset.csv", encoding="utf-8")

#%%
from tqdm.notebook import tqdm
# %%
# read the scentence column named "sentences" and extract the raw text from it

for i in tqdm(range(1,6)):
    Translated_Dataset[f"sentence_{i}"] = ' '
    Translated_Dataset[f"ar_sentence_{i}"] = ' '
Translated_Dataset.head()

#%%                             
for i, item in tqdm(enumerate(Translated_Dataset["sentences"][83002:], start=83002)):
    # if i==5:
    #     break
    import ast
    # convert the string to a list of dictionaries
    try:
        lst = ast.literal_eval(Translated_Dataset["sentences"][i])
    except SyntaxError:
        print(i)
        print("Syntax Error")
        
    # extract the raw values from each dictionary

    for j, d in enumerate(lst):
        # print(d['raw'])
        Translated_Dataset.loc[i, f"sentence_{j+1}"] = d['raw']
        # print(j+1)
        # print(Translated_Dataset.loc[i, f"sentence_{j+1}"])

    for j, d in enumerate(lst):
        # print(d['raw'])
        # Translates some text into English
        translation = translate_client.translate(d['raw'], target_language=target)
        Translated_Dataset.loc[i, f"ar_sentence_{j+1}"] = translation['translatedText']
        # print(j+1)
        # print(Translated_Dataset.loc[i, f"ar_sentence_{j+1}"])

    if i%1000==0:
        Translated_Dataset.to_csv("Translated_Dataset_new_2.csv", encoding="utf-8")
        print(i)

# %%
Translated_Dataset
# %%
Translated_Dataset.to_csv("Translated_Dataset_new_2.csv", encoding="utf-8")

# %%
# for i, item in tqdm(enumerate(Translated_Dataset["sentences"][38208:], start=38208)):
#     print(i)
# %%
