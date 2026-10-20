# Dataset Audit Summary

Dataset: Plant Leaf Disease Dataset

Working folder: Plant_Diseases_Leakage_Reduced

| Split | Images | Classes |
|---|---:|---:|
| Train | 24,630 | 19 |
| Validation | 5,278 | 19 |
| Test | 5,273 | 19 |
| Total | 35,181 | 19 per split |

Recorded checks:
- Earlier integrity scan: zero unreadable images.
- Unique SHA-256 hashes: 35,181.
- Exact duplicate hashes crossing splits: zero.
- Seven high-similarity candidate images moved outside the split folders.

Exact-hash checks do not rule out every visually similar or transformed image.
Re-run the audit after changing the dataset.
