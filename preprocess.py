import gensim.models as gsm
from parse_recipes import load_recipes
from config import cfg
import phrase2vec as p2v
import numpy as np
import json
import pickle

import nltk.tokenize as tk

tokenizer = tk.TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)


def create_recipe_vectors(p2v_our_emoji):
    """Create recipe vectors by averaging embeddings of inredients and saving the result
    """
    recipes = load_recipes()
    recipes_clean = {}

    for key, value in recipes.items():
        ingredients_tokens = [tokenizer.tokenize(ingredient) for ingredient in value['ingredients_clean']]
        ingredients_tokens_flat = [ingredient for sublist in ingredients_tokens for ingredient in sublist]

        # No ingredients left after pre-processing
        if len(ingredients_tokens_flat) == 0:
            continue

        recipe_vector = np.sum([p2v_our_emoji[ingredient] for ingredient in ingredients_tokens_flat], axis=0) / len(
            ingredients_tokens_flat)
        value['recipe vector'] = recipe_vector.tolist()
        recipes_clean[key] = value

    with open('recipes.json', 'w') as fp:
        json.dump(recipes_clean, fp)


w2v = gsm.KeyedVectors.load_word2vec_format(cfg.DATA.W2V_PATH, binary=True)
e2v = gsm.KeyedVectors.load_word2vec_format(cfg.DATA.E2V_PATH, binary=True)

# Load model using appropriate library and function
global model
model = p2v.Phrase2Vec(cfg.MODEL_PARAMS.DIM, w2v, e2v=e2v)

with open(cfg.DATA.MODEL_PATH, 'wb') as output:
    pickle.dump(model, output)

create_recipe_vectors(model)
