import json
import numpy as np
from emoji2recipe import find_recipe 
from config import cfg
import os
from azure.storage.blob import BlockBlobService

block_blob_service = BlockBlobService(account_name= cfg.AZURE.ACCOUNT_NAME, account_key=cfg.AZURE.ACCOUNT_KEY)

model = None

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
        First tries to find approximate nearest neighbors and if no result returned
        falls back to an exhaustive search
    """
    result = find_recipe(doc_text, recipes, model)
    return result
	
def main():
    # Test the init and run functions using test data
    init()

    test_doc_text = "sandwich" 
    print (run(test_doc_text))  

if __name__ == "__main__":
    main()