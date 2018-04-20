import os
from easydict import EasyDict as edict
import time

_C = edict()
cfg = _C


#AZURE parameters
_C.AZURE = edict()
if 'STORAGE_ACCOUNT_NAME' in os.environ:
    _C.AZURE.ACCOUNT_NAME = os.environ['STORAGE_ACCOUNT_NAME']
else:
    _C.AZURE.ACCOUNT_NAME = <"ADD YOUR AZURE STORAGE ACCOUNT NAME HERE">
if 'STORAGE_ACCOUNT_KEY' in os.environ:
    _C.AZURE.ACCOUNT_KEY = os.environ['STORAGE_ACCOUNT_KEY']
else:
    _C.AZURE.ACCOUNT_KEY = <"ADD YOUR AZURE STORAGE ACCOUNT KEY HERE">

#DATA DIRECTORIES
_C.DATA =edict()
_C.DATA.BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

_C.DATA.W2V_FILE = 'google_w2v_without_emoji.bin' 
_C.DATA.W2V_DIR = _C.DATA.BASE_FOLDER 
_C.DATA.W2V_PATH = os.path.join(cfg.DATA.W2V_DIR, cfg.DATA.W2V_FILE) 

_C.DATA.E2V_FILE = 'emoji2vec.bin' 
_C.DATA.E2V_DIR = _C.DATA.BASE_FOLDER 
_C.DATA.E2V_PATH = os.path.join(cfg.DATA.E2V_DIR, cfg.DATA.E2V_FILE) 

_C.DATA.DATA_FILE = 'recipes.json' 
_C.DATA.DATA_DIR = _C.DATA.BASE_FOLDER 
_C.DATA.DATA_PATH = os.path.join(cfg.DATA.DATA_DIR, cfg.DATA.DATA_FILE) 

_C.DATA.RAW_DATA_DIR = os.path.join(cfg.DATA.BASE_FOLDER, "recipes_raw")

_C.DATA.MODEL_PATH = os.path.join(cfg.DATA.BASE_FOLDER,"model.pkl")

#Model parameters
_C.MODEL_PARAMS = edict()
_C.MODEL_PARAMS.DIM = 300
