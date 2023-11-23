# PubChem Bioassay Data Processing & Prediction Model Pipeline

## Introduction

This project aims to streamline the process of downloading and processing bioassay data from PubChem, focusing on target bioassays. The project uses the D(2) dopamine receptor as an example, utilizing the file `pubchem_protacxn_P14416_bioactivity_protein`. This README details the steps and scripts for parsing bioassay data, extracting molecular descriptors, and organizing information based on activity types such as IC50, EC50, and Ki.

This is a simple pipeline for downloading, processing, and analyzing bioassay data from PubChem. I focused on the D(2) dopamine receptor, utilizing the file `pubchem_protacxn_P14416_bioactivity_protein.csv` as downloaded from [PubChem](https://pubchem.ncbi.nlm.nih.gov/protein/P14416#section=BioAssays) for this example. It includes scripts for data parsing, molecular descriptor extraction, and data organization based on activity types (IC50, EC50, Ki). It also features a Jupyter Notebook equipped with machine learning models (Random Forest, XGBoost) for visualizing features and predicting bioactivity, using evolutionary algorithms for model optimization. 


## Steps and Scripts

### 1. Download Bioassay Data
- **Script**: None
- **Description**: Manually download target bioassays from PubChem in CSV format.

### 2. Initial Parsing of Data
- **Scripts**: `parse1.py`, `parse2.py`
- **Function**: Parse the initial CSV file to format and prepare the data.
- **Output**: Intermediate files (output1.csv, output2.csv).

### 3. Retrieving SDFs of Molecules
- **Script**: `getSDFromCID.py`
- **Function**: Fetches the SDF format of molecules from bioassays using PubChem IDs.
- **Output**: SDF files.

### 4. Collecting Molecular Descriptors
- **Script**: `getMolecDescriptorsFromSDF.py`
- **Function**: Extracts molecular descriptors from SDF files.
- **Output**: Descriptors (output3.csv).

### 5. Merging Data
- **Script**: `mergeData.py`
- **Function**: Merges various data files.
- **Output**: A consolidated data file. (output4.csv)

### 6. Sorting by Activity Types
- **Script**: `sortActivityTypes.py`
- **Function**: Organizes data by activity types (IC50, EC50, Ki).
- **Output**: Sorted files in the Activity_Types folder.

## Running the Models for Visualization and Prediction

### Prerequisites
- Install necessary packages:

```bash
!pip install requests scikit-learn pubchempy xgboost deap seaborn
```

### Model Functionality
- Uses machine learning models, including Random Forest and XGBoost, for predicting activity from compound data.
- Includes functions for fetching compound data, running evolutionary algorithms for model optimization, and visualizing feature importance.
- Demonstrates the prediction of bioactivity for new compounds.

### Example Usage
- Load the processed data as described above, and use the jupyter notbooks to do the following.
- Run the evolutionary algorithm to find the best hyperparameters for the XGBoost regressor.
- Train the regressor and evaluate its performance using metrics like Mean Squared Error, Mean Absolute Error, and R^2 Score.
- Visualize the feature importance to understand which features contribute most to the model's predictions.
- Predict the activity type and value for new compounds.

## Usage Instructions

Follow the scripts in the order presented to ensure smooth data processing. Each script must be run individually, with the output from one script generally serving as the input for the next. For model visualization and prediction, run the provided Jupyter Notebook, following the example usage steps.

## Feature Analysis Visualization Examples
Descriptor importance for IC50:
![image](https://github.com/DaltonPayne/PubChem-Bioassay-Data-Processing-Prediction-Model/assets/67125850/dcea9599-e64a-422a-a042-2dc2f6e1612b)

Descriptor importance for EC50:
![image](https://github.com/DaltonPayne/PubChem-Bioassay-Data-Processing-Prediction-Model/assets/67125850/ad32ea38-5569-404a-a56e-52dbc5007aad)

Descriptor importance for Ki:
![image](https://github.com/DaltonPayne/PubChem-Bioassay-Data-Processing-Prediction-Model/assets/67125850/a1bdd367-f6d4-4685-b882-ab1732ecd5a8)


