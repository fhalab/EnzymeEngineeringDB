import sys
sys.path.append('/disk1/ariane/vscode/enzyme-tk')

from enzymetk.dock_chai_step import Chai
from enzymetk.save_step import Save
import pandas as pd
import os
os.environ['MKL_THREADING_LAYER'] = 'GNU'

output_dir = 'structures/'
num_threads = 4
id_col = 'id'
seq_col = 'parent_aa'
substrate_col = 'substrate_smiles'
df = pd.read_csv('DF4_parents.csv')
done_entries = os.listdir('structures')
print(len(df))

#print(len(df))
to_do = []
done = []

import sys
from docko.boltz import *

base_dir = 'boltz'

for entry, seq, substrate in df[[id_col, seq_col, substrate_col]].values:
    run_boltz(entry, 
         seq, 
         substrate + ".CC1=C(C2=CC3=C(C(=C([N-]3)C=C4C(=C(C(=N4)C=C5C(=C(C(=N5)C=C1[N-]2)C)C=C)C)C=C)C)CCC(=O)[O-])CCC(=O)[O-].[Fe]",
         base_dir
        )
# for f in done_entries:
#     try:
#         # Check if there are files in chai
#         files = os.listdir(f'structures/{f}/chai')
#         if len(files) < 10:
#             to_do.append(f)
#             #os.system(f'rm -r structures/{f}')
#         else:
#             done.append(f)
#     except:
#         print(f)
# # Run initially with chai_lab-0.5.2 then also with chai_lab-0.6.1
# df = df[df[id_col].isin(to_do)]
# print(len(df))




#df << (Chai(id_col, seq_col, substrate_col, f'{output_dir}', num_threads) >> Save(f'{output_dir}DF4_parents_chai.pkl'))
