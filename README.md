# Multi-Plant Leaf Disease Detection

## Project Overview

This MSc project investigates plant leaf disease classification and
representation analysis using machine learning and computer vision.

The experiments follow this sequence:

1. Supervised Learning
2. Unsupervised Learning
3. Deep Learning
4. Foundation Models
5. Adaptation and Comparative Analysis

## Dataset Information

- **Dataset:** Plant Leaf Disease Dataset
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/keerthanreddy123/plant-leaf-disease-dataset)
- **Number of classes:** 19
- **Final recorded image count:** 35,181

### Dataset splits

| Split | Images |
|---|---:|
| Training | 24,630 |
| Validation | 5,278 |
| Testing | 5,273 |
| Total | 35,181 |

The dataset contains groundnut, potato, and tomato leaf categories.

### Local dataset path

`C:\Intro_TO_AI_Project\Plant_Diseases_Leakage_Reduced`

The dataset images are not included in this repository.

## Methodology

### Stage 1: Supervised Learning
- HOG feature extraction
- Support Vector Machine (SVM)
- Random Forest
- Accuracy, precision, recall, macro-F1 and confusion matrix

### Stage 2: Unsupervised Learning
- Principal Component Analysis (PCA)
- K-means clustering
- Silhouette score
- Adjusted Rand Index (ARI)

Disease labels will not be used to form the clusters.

### Stage 3: Deep Learning
- MobileNetV3Small
- VGG16 or another justified comparison CNN
- Training and validation performance comparison

### Stage 4: Foundation Models
- DINOv2 feature extraction
- Optional CLIP feature extraction
- Representation and classification comparison

### Stage 5: Adaptation
- Frozen feature extraction
- Linear probing
- Fine-tuning
- Final model comparison

## Dataset Quality Checks

The latest recorded audit reported:

- 35,181 images
- 19 classes in each split
- Zero unreadable images in the earlier integrity scan
- 35,181 unique SHA-256 hashes
- Zero exact duplicate hashes crossing splits

Seven highly similar cross-split candidate images were moved to quarantine.
This does not prove that all visual near-duplicates have been eliminated.

## Repository Structure

```text
Multi_Plant_Leaf_Disease_Detection/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── docs/
│   └── EXPERIMENT_PLAN.md
├── notebooks/
│   └── README.md
├── reports/
│   └── DATASET_AUDIT_SUMMARY.md
└── src/
    └── audit_dataset.py
```

## Setup

Recommended Python version: 3.10 or 3.11.

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dataset audit:

```bash
python src/audit_dataset.py --root "C:\Intro_TO_AI_Project\Plant_Diseases_Leakage_Reduced"
```

## Evaluation Rules

- Use training data to fit models.
- Use validation data for model selection.
- Keep the test set untouched until final evaluation.
- Record random seeds, metrics, configurations and training time.
- Do not report experimental results before running the experiments.

## Current Progress

- [x] Dataset preparation and splitting
- [x] Dataset integrity checks
- [x] Exact-hash separation check
- [x] HOG + HSV + LBP
- [x] SVM
- [x] Random Forest
- [x] Light GBM
- [x] PCA + K-means + GMM
- [ ] Deep learning
- [ ] Foundation models
- [ ] Adaptation and final comparison

## Dataset Attribution

## Thanya, I want to make something clear regarding this project.

So far, I have completed almost everything on my own. The supervised learning and unsupervised learning parts are completed, and I have already started working on the deep learning models. You haven't contributed to the project so far.

I shared the GitHub link with you almost a month ago, but it seems you haven't even opened it or taken the time to check the code, understand the workflow, or see what progress has been made.

At the very least, I expected you to open the GitHub repository, go through the implementation, and understand what is happening in the project. I cannot be expected to handle the entire project alone while it is supposed to be a collaborative effort.

Please go through the GitHub repository and contact me so we can discuss the current progress and your contribution to the remaining work. of foundation model.

Note if you don't want to work with me you are free to leave the group and join in another group you can contact prof Joseph.

