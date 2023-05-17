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
