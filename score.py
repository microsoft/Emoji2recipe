# This script generates the scoring and schema files
# necessary to operationalize your model
from azureml.api.schema.dataTypes import DataTypes
from azureml.api.schema.sampleDefinition import SampleDefinition
from azureml.api.realtime.services import generate_schema

import json
import numpy as np
import nltk.tokenize as tk
import gensim.models as gsm
from sklearn.metrics.pairwise import cosine_similarity
import phrase2vec as p2v
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

    w2v = gsm.KeyedVectors.load_word2vec_format(cfg.DATA.W2V_PATH, binary=True)
    e2v = gsm.KeyedVectors.load_word2vec_format(cfg.DATA.E2V_PATH, binary=True)

    # Load model
    global model
    model = p2v.Phrase2Vec(cfg.MODEL_PARAMS.DIM, w2v, e2v=e2v)

def run(doc_text):
    """
        Runs the recipe prediction model
    """
    result = find_recipe(doc_text.encode('utf-8'), recipes, model)
    return result

def main():
    # Test the init and run functions using test data
    init()

    test_doc_text = "🍪" 
    category = run(test_doc_text)
    print(category)

    test_doc_text = "tomato pizza"
    
    # Generate the schema file (schema.json) needed for AML operationalization
    inputs = {"doc_text": SampleDefinition(DataTypes.STANDARD, test_doc_text)}
    generate_schema(run_func=run, inputs=inputs, filepath='./outputs/schema.json')
    block_blob_service.create_blob_from_path('embeddings', 'schema.json', './outputs/schema.json')

if __name__ == "__main__":
    main()