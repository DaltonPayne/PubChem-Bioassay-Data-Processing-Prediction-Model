import os
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import PandasTools
from rdkit.Chem import Lipinski

def get_descriptors(molecule):
    """Calculate descriptors for a single molecule"""
    descriptors = {
        "MolWt": Descriptors.MolWt(molecule),
        "MolLogP": Descriptors.MolLogP(molecule),
        "NumHDonors": Descriptors.NumHDonors(molecule),
        "NumHAcceptors": Descriptors.NumHAcceptors(molecule),
        "RingCount": Descriptors.RingCount(molecule),
        "TPSA": Descriptors.TPSA(molecule),
        "NumRotatableBonds": Descriptors.NumRotatableBonds(molecule),
        "NumAromaticRings": Descriptors.NumAromaticRings(molecule),
        "NumSaturatedRings": Descriptors.NumSaturatedRings(molecule),
        "NumAliphaticRings": Descriptors.NumAliphaticRings(molecule),
        "NumAromaticHeterocycles": Lipinski.NumAromaticHeterocycles(molecule),
        "NumAliphaticHeterocycles": Lipinski.NumAliphaticHeterocycles(molecule),
        "NumAromaticCarbocycles": Lipinski.NumAromaticCarbocycles(molecule),
        "NumAliphaticCarbocycles": Lipinski.NumAliphaticCarbocycles(molecule),
        "NumHeteroatoms": Descriptors.NumHeteroatoms(molecule),
        "FractionCSP3": Descriptors.FractionCSP3(molecule),
        "HallKierAlpha": Descriptors.HallKierAlpha(molecule),
        "Kappa3": Descriptors.Kappa3(molecule),
        "LabuteASA": Descriptors.LabuteASA(molecule),
        "BalabanJ": Descriptors.BalabanJ(molecule) if Descriptors.BalabanJ(molecule) is not None else 0,  # Handle None values
        "BCUT2D_MWHI": Descriptors.BCUT2D_MWHI(molecule),
        "BCUT2D_MWLOW": Descriptors.BCUT2D_MWLOW(molecule),
        "EState_VSA1": Descriptors.EState_VSA1(molecule),
        "EState_VSA2": Descriptors.EState_VSA2(molecule)
    }
    return descriptors

def main():
    sdf_dir = 'sdf'
    sdf_files = [f for f in os.listdir(sdf_dir) if f.endswith('.sdf')]

    all_descriptors = []

    for sdf_file in sdf_files:
        sdf_path = os.path.join(sdf_dir, sdf_file)
        # Load the SDF file into a DataFrame
        df = PandasTools.LoadSDF(sdf_path)
        for index, row in df.iterrows():
            molecule = row['ROMol']  # RDKit molecule object
            descriptors = get_descriptors(molecule)
            descriptors['CID'] = int(sdf_file.split('_')[1].split('.')[0])  # Extract CID from filename
            all_descriptors.append(descriptors)

    # Convert to DataFrame and save to CSV
    df_descriptors = pd.DataFrame(all_descriptors)
    df_descriptors.to_csv('output_3.csv', index=False)

if __name__ == "__main__":
    main()
