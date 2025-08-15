import sys
from docko.chai import run_chai
import pandas as pd
import os
os.environ['MKL_THREADING_LAYER'] = 'GNU'

output_dir = 'DEDB_Chai_LLM/'
output_dir = 'DEDB_Chai/'

num_threads = 1
id_col = 'id'
seq_col = 'parent_aa' #'aa_sequence'
substrate_col = 'substrate'
intermediate_col = 'intermediate'
df = pd.read_csv('output/structures_to_do.csv')
for label, seq, substrate, cofactor in df[['id', seq_col, substrate_col, intermediate_col]].values:
        if isinstance(cofactor, str):
                cofactor = cofactor.split('.')
        else:
                cofactor = ''
        run_chai(label, seq, substrate, output_dir, cofactor)
        print(label)

# LLM structures
# df = pd.read_csv('output/parents_LLM_extraction_v2.csv')
# df['intermediate'] = ['.'.join(s.split('>>')[0].split('.')[1:]) for s in df['smiles_reaction'].values]
# df['substrate'] = [s.split('>>')[0].split('.')[0] for s in df['smiles_reaction'].values]
# #df['id'] = [f'chai{i}' for i in range(0, len(df))]
# #df.to_csv('output/parents_LLM_extraction_annot.csv', index=False)
# print(df)
# for label, seq, substrate, cofactor in df[['id', seq_col, substrate_col, intermediate_col]].values:
#         try:
#                 cofactor = cofactor.split('.')
#                 run_chai(label, seq, substrate, output_dir, cofactor)
#         except:
#                 print(label)

# DEDB which were missed
# df = pd.read_csv('output/structures_to_do.csv')
# df['intermediate'] = ['.'.join(s.split('>>')[0].split('.')[1:]) for s in df['reaction_smiles'].values]
# df['substrate'] = [s.split('>>')[0].split('.')[0] for s in df['reaction_smiles'].values]
# print(df)
# for label, seq, substrate, cofactor in df[['id', seq_col, substrate_col, intermediate_col]].values:
#         try:
#                 cofactor = cofactor.split('.')
#                 run_chai(label, seq, substrate, output_dir, cofactor)
#         except:
#                 print(label)

# DEDB structures
# id_col = 'id'
# seq_col = 'parent_aa'
# df = pd.read_csv('output/protein-evolution-database_DF5_proteins_reactions_clean_parents.csv')
# df['intermediate'] = ['.'.join(s.split('>>')[0].split('.')[1:]) for s in df['substrate_smiles'].values]
# df['substrate'] = [s.split('>>')[0].split('.')[0] for s in df['substrate_smiles'].values]
# for label, seq, substrate, cofactor in df[['id', seq_col, substrate_col, intermediate_col]].values:
#         try:
#                 cofactor = cofactor.split('.')
#                 run_chai(label, seq, substrate, output_dir, cofactor)
#         except:
#                 print(label)
