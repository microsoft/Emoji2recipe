from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial import distance
import numpy as np
from config import cfg
import json

import nltk.tokenize as tk

tokenizer = tk.TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)

def find_recipe(input_text, recipes, p2v_our_emoji):
	"""
		Does an exhaustive search through all rrecipes to find closest vector
	"""
	print(input_text)
	tokens = tokenizer.tokenize(input_text)	
	print(tokens)
	vector = np.sum([p2v_our_emoji[t] for t in tokens], axis=0) / len(tokens)
	
	key, value = min(recipes.items(), key=lambda kv: (distance.euclidean(vector, np.array(kv[1]['recipe vector']))))

	result = {}
	result['title'] = value['title']
	result['instructions'] = value['instructions']

	return json.dumps(result)