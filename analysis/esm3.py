from esm.models.esmc import ESMC
from esm.sdk.api import ESMProtein, LogitsConfig
import torch
import re
import os
import pandas as pd
from esm.models.esm3 import ESM3
from esm.sdk.api import ESMProtein, SamplingConfig
from esm.utils.constants.models import ESM3_OPEN_SMALL

from huggingface_hub import login

# CUDA setup
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
cuda = True
DEVICE = torch.device("cuda" if cuda else "cpu")
device = DEVICE #torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# prepare your protein sequences/structures as a list.
# Amino acid sequences are expected to be upper-case ("PRTEINO" below)
# while 3Di-sequences need to be lower-case ("strctr" below).
import numpy as np
from tqdm import tqdm 

# Will instruct you how to get an API key from huggingface hub, make one with "Read" permission.
login()

client = ESM3.from_pretrained("esm3-open").to("cuda") # or "cpu"
    
def run(df):
    sequence_examples = list(df[seq_col].values)
    # replace all rare/ambiguous amino acids by X (3Di sequences do not have those) and introduce white-space between all sequences (AAs and 3Di)
        # if you want to derive a single representation (per-protein embedding) for the whole protein
    means = []
    lasts = []
    for id, seq in tqdm(df[[id_col, seq_col]].values):
        protein = ESMProtein(
            sequence=(
                seq
            )
        )
        protein_tensor = client.encode(protein)
        output = client.forward_and_sample(
            protein_tensor, SamplingConfig(return_per_residue_embeddings=True)
        )
        torch.save(output.per_residue_embedding, f'esm3/{id}.pt')
        means.append(np.array(output.per_residue_embedding.mean(dim=0).cpu()))
    df['esm3_mean']  = means
    return df
    
train_df = pd.read_csv('DF4_parents.csv')
id_col = 'id'
seq_col = 'parent_aa'
df = run(train_df)
df.to_pickle('esm3_DF4_parents.pkl')