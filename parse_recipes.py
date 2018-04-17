import os
from os import path
from glob import glob
import json
import re
import pickle
import argparse
import numpy as np
from scipy import ndimage, misc
from config import cfg
from parse_ingredients import preprocess_ingredients

def load_recipe(filename):
	"""Load a single recipe file
	"""
	with open(filename, 'r') as f:
		recipes = json.load(f)
	print('Loaded {:,} recipes from {}'.format(len(recipes), filename))
	return recipes

def clean_recipe_ingredients(recipes):
	"""Clean and parse recipe ingedients
	"""
	recipes_clean = {}
	for key, value in recipes.items():
		
		if "ingredients" not in value.keys():
			continue 
		value['ingredients_clean'] = preprocess_ingredients(value['ingredients'])
		recipes_clean[key] = value
	return recipes_clean

def load_recipes():
	"""Load all raw recipes and combine to single dataset (json format)
	"""
	recipes = {}
	print(path.join(cfg.DATA.RAW_DATA_DIR, 'recipes_raw*.json'))
	for filename in glob(path.join(cfg.DATA.RAW_DATA_DIR, 'recipes_raw*.json')):
		
		print (filename)
		recipes.update(load_recipe(filename))
	print('Loaded {:,} recipes in total'.format(len(recipes)))
	return clean_recipe_ingredients(recipes)
