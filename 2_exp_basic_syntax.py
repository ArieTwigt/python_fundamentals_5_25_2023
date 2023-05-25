#%%
flower_list = ['rose', 'tulip', 'lily']
print(type(flower_list))

# %% examples with "strip"
sentence = "   this is a sentence with leading and trailing spaces    "
sentence_clean = (sentence.strip() # strip whitespaces
                          .replace("with", "without") # replace word
                          .capitalize()) # capitalize the sentence
sentence_clean

# %% join, split
sentence_list = sentence_clean.split(" ")
# %%
sentence_list[-1] = "Arie"

# %%
" ".join(sentence_list)
# %%
