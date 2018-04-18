import json
import numpy as np
from emoji2recipe import find_recipe 
from config import cfg
import os
import pickle

def init():
    # load pre-processed recipe data
    global recipes
    with open(cfg.DATA.DATA_PATH, 'r', encoding='utf-8', errors='ignore') as fp: 
	    recipes = json.load(fp)

    # Load model
    global model
    f = open(cfg.DATA.MODEL_PATH,'rb')
    model = pickle.load(f)

def run(doc_text):
    """
        Runs the recipe prediction model
    """
    result = find_recipe(doc_text, recipes, model)
    return result
	
def main():
    # Test the init and run functions using test data
    init()

    test_doc_text = "cookie" 
    print (run(test_doc_text))  

if __name__ == "__main__":
    main()