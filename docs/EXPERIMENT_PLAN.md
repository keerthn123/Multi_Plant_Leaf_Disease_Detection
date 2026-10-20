# Experiment Plan

## Research Question

How do handcrafted features, unsupervised clustering, CNNs and foundation-model
representations compare for multi-class plant leaf disease classification?

## 1. Supervised Learning

- Extract HOG image features.
- Train an SVM.
- Train a Random Forest.
- Tune using validation data.
- Report accuracy, macro-F1 and confusion matrices.

## 2. Unsupervised Learning

- Extract features without using labels for cluster formation.
- Visualize with PCA.
- Apply K-means.
- Evaluate silhouette score and post-hoc ARI.

## 3. Deep Learning

- MobileNetV3Small.
- A comparison CNN such as VGG16.
- Compare performance and computational cost.

## 4. Foundation Models

- Extract frozen DINOv2 features.
- Optionally investigate CLIP.
- Compare representation quality and downstream classification.

## 5. Adaptation and Comparison

- Compare frozen features, linear probing and fine-tuning.
- Select models using validation results.
- Evaluate on the test set only after final decisions are made.

## Reproducibility

Record random seeds, software versions, hyperparameters, metrics and runtime.
