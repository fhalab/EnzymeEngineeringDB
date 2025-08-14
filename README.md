# EnzEngDB

A comprehensive database and analysis pipeline for studying directed evolution of enzymes performing new-to-nature reactions.

## Overview  

DirectedEvolutionDB curates and analyzes data from directed evolution experiments documented in scientific literature, focusing on engineered enzymes that catalyze reactions not found in nature. The project creates molecular embeddings for both protein sequences and chemical reactions to enable machine learning applications and comparative analyses.

## Features 

- **Data Curation**: Systematic collection of enzyme-reaction pairs from 36+ research papers
- **Molecular Embeddings**: State-of-the-art embeddings for proteins (ESM3) and reactions (ChemBERTa2, RxnFP)
- **Chemical Space Analysis**: Visualization and comparison of engineered vs natural enzyme reaction space
- **Standardized Format**: Conversion to LevSeq format for broader accessibility
- **Comprehensive Pipeline**: End-to-end processing from raw data to analysis-ready datasets

## Dataset Statistics  

- 1,341 enzyme-reaction pairs
- 640 unique reactions
- 367 unique protein variants
- 36 research papers included

## Installation  

### Prerequisites  

- Python 3.8+
- PyTorch (for ESM models)
- RDKit (for chemistry operations)

### Install via pip  


```
# Clone the repository
git clone https://github.com/yourusername/DirectedEvolutionDB.git
cd DirectedEvolutionDB

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies  

The project requires the following main packages:
- Core: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
- Chemistry: `rdkit`, `pubchempy`, `biopython`
- Deep Learning: `torch`, `esm`, `huggingface-hub`
- Specialized: `enzymetk`, `sciutil`, `sciviso`

See `requirements.txt` for complete list with versions.

## Usage  

The analysis pipeline consists of four main notebooks that should be run in sequence:

### 1. Clean Reaction Data  
```
jupyter notebook analysis/N1_CleanReactionData.ipynb
```
- Validates and canonicalizes reaction SMILES
- Creates reaction embeddings using ChemBERTa2 and RxnFP
- Outputs: `cannoical_smiles.pkl`, `rxn_chemberta.pkl`, `rxn_rxnfp.pkl`

### 2. Clean Enzyme Data 

```
jupyter notebook analysis/N2_CleanEnzymeData.ipynb
```

- Processes enzyme sequences and mutations
- Generates protein embeddings using ESM3
- Outputs: `protein-evolution-database_V4_embedded_proteins.pkl`, `variant_df_no_errors.pkl`

### 3. Analyze Combined Data  

```
jupyter notebook analysis/N3_AnalyseEnzymeReactionData.ipynb
```

- Combines protein and reaction data
- Performs PCA analysis and visualization
- Compares engineered enzymes to natural enzyme space

### 4. Convert to Standard Format  

```
jupyter notebook analysis/N4_ConvertFormatToLevSeq.ipynb
```
- Converts data to LevSeq format
- Organizes by experiment/paper
- Creates metadata files

## Project Structure  


```
DirectedEvolutionDB/
---  README.md
---  requirements.txt
---  LICENSE
---  data/                    # Raw data files
---  nalysis/
------   N1_CleanReactionData.ipynb
------ N2_CleanEnzymeData.ipynb
------ N3_AnalyseEnzymeReactionData.ipynb
------ N4_ConvertFormatToLevSeq.ipynb
------  scripts/
------ esm3.py         # ESM3 embedding utilities
------ output/             # Processed data outputs
------ Archive/            # Previous notebook versions
```

## Output Files  


- `cannoical_smiles.pkl`: Standardized reaction SMILES
- `rxn_chemberta.pkl`: ChemBERTa2 reaction embeddings
- `rxn_rxnfp.pkl`: RxnFP reaction fingerprints
- `protein-evolution-database_V4_embedded_proteins.pkl`: ESM3 protein embeddings
- `variant_df_no_errors.pkl`: Cleaned variant data with yields

## Key Findings  


1. Directed evolution has successfully expanded enzyme function into previously unexplored chemical space
2. Engineered enzymes cluster in distinct regions when visualized using dimensionality reduction
3. Different research groups tend to explore different regions of chemical/sequence space
4. The database captures the diversity of new-to-nature enzymatic reactions

## Contributing  


We welcome contributions! Please feel free to submit issues or pull requests.

## Citation

Coming soon!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or collaborations, please open an issue on GitHub.
