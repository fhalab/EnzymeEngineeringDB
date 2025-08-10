import sys
from docko.chai import run_chai
import pandas as pd
import os
os.environ['MKL_THREADING_LAYER'] = 'GNU'

output_dir = 'DEDB_Chai_LLM/'
num_threads = 1
id_col = 'id'
seq_col = 'aa_sequence'
substrate_col = 'substrate'
intermediate_col = 'intermediate'
# rows = [
#     ['parLQcis', 'C=CC1=CC=C(OC)C=C1', 'C=CC1=CC=C(OC)C=C1.O=C(OCC)C=[N+]=[N-]>>O=C(OCC)[C@H](C2)[C@H]2C3=CC=C(OC)C=C3', 'MAVPGYDFGKVPDAPISDADFESLKKTVMWGEEDEKYRKMACEALKGQVEDILDLWYGLQGSNQHLIYYFGDKSGRPIPQYLEAVRKRFGLWIIDTLCKPLDRQWLNYMYEIGLRHHRTKKGKTDGVDTVEHIPLRYMIAFIAPIGLTIKPILEKSGHPPEAVERMWAAWVKLVVLQVAIWSYPYAKTGEWLE'],
#      ['parLQtrans', 'C=CC1=CC=C(OC)C=C1', 'C=CC1=CC=C(OC)C=C1.O=C(OCC)C=[N+]=[N-]>>O=C(OCC)[C@@H](C2)[C@H]2C3=CC=C(OC)C=C3', 'MAVPGYDFGKVPDAPISDADFESLKKTVMWGEEDEKYRKMACEALKGQVEDILDLWYGLQGSNQHLIYYFGDKSGRPIPQYLEAVRKRFGLWIIDTLCKPLDRQWLNYMYEIGLRHHRTKKGKTDGVDTVEHIPLRYMIAFIAPIGLTIKPILEKSGHPPEAVERMWAAWVKLVVLQVAIWSYPYAKTGEWLE']
#         ]
# rows = [
#      ['Q06174', 'O=P(OC1=CC=CC=C1)(OC2=CC=CC=C2)OC3=CC=CC=C3', 'O=P(O)(OC4=CC=CC=C4)OC5=CC=CC=C5', 'MKIVPPKPFFFEAGERAVLLLHGFTGNSADVRMLGRFLESKGYTCHAPIYKGHGVPPEELVHTGPDDWWQDVMNGYEFLKNKGYEKIAVAGLSLGGVFSLKLGYTVPIEGIVTMCAPMYIKSEETMYEGVLEYAREYKKREGKSEEQIEQEMEKFKQTPMKTLKALQELIADVRDHLDLIYAPTFVVQARHDEMINPDSANIIYNEIESPVKQIKWYEQSGHVITLDQEKDQLHEDIYAFLESLDW']
#         ]
# df = pd.DataFrame(rows, columns=['id', 'substrate', 'smiles', 'seq'])
# df = pd.read_csv('../data/DEDB_structures.csv')
# df.dropna(subset=['smiles'], inplace=True)
df = pd.read_csv('output/parents_LLM_extraction.csv')
df['intermediate'] = ['.'.join(s.split('>>')[0].split('.')[1:]) for s in df['smiles_reaction'].values]
df['substrate'] = [s.split('>>')[0].split('.')[0] for s in df['smiles_reaction'].values]
df['id'] = [f'chai{i}' for i in range(0, len(df))]
df.to_csv('output/parents_LLM_extraction_annot.csv', index=False)
print(df)
for label, seq, substrate, cofactor in df[['id', seq_col, substrate_col, intermediate_col]].values:
        try:
                cofactor = cofactor.split('.')
                run_chai(label, seq, substrate, output_dir, cofactor)
        except:
                print(label)
        #df << (Chai(id_col, seq_col, substrate_col, intermediate_col, f'{output_dir}', num_threads) >> Save(f'{output_dir}LLM_df.pkl'))
