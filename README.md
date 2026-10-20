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
- [ ] HOG + SVM
- [ ] Random Forest
- [ ] PCA + K-means
- [ ] Deep learning
- [ ] Foundation models
- [ ] Adaptation and final comparison

## Dataset Attribution

Please consult the Kaggle dataset page for its current licence and attribution
requirements before redistributing dataset images.
