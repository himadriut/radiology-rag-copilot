# Dataset

This project uses a curated subset of the **MIMIC-CXR dataset**, available through PhysioNet.

Dataset source:

https://physionet.org/content/mimic-cxr/

The MIMIC-CXR dataset was created by MIT and Beth Israel Deaconess Medical Center.

## Dataset Overview

The full dataset contains:

- 377,110 chest X-ray images
- 227,827 radiographic studies
- approximately 65,000 patients

Each study includes:

- Chest X-ray image
- Radiology report
- CheXpert disease labels

## Subset Used in This Project

For experimentation, a subset of studies was created.

| Stage | Rows |
|------|------|
| Initial sampled studies | 2000 |
| DICOM rows | 3301 |
| Images available | 3149 |
| Rows with impression text | 2696 |
| Final clean dataset | 2696 studies |

Each dataset row contains:

- subject_id
- study_id
- dicom_id
- image_path
- ViewPosition
- impression

## Labels

Labels were derived using the CheXpert labeling pipeline.

Example labels include:

- Atelectasis
- Cardiomegaly
- Pneumonia
- Pneumothorax
- Pleural Effusion
- No Finding

From the processed dataset:

**839 studies contained at least one positive finding.**

## Data Availability

Due to licensing restrictions, the MIMIC-CXR dataset cannot be redistributed in this repository.

Researchers can request access through PhysioNet.

After obtaining access, place the dataset files in:

```
data/
   images/
   clean_dataset_2696.csv
```
