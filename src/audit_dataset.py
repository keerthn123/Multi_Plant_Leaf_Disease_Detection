import argparse
import hashlib
from collections import defaultdict
from pathlib import Path

import pandas as pd
from PIL import Image, UnidentifiedImageError

SPLITS = ("train", "valid", "test")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff"}


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True,
                        help="Dataset root containing train/valid/test")
    parser.add_argument("--output", default="dataset_audit_inventory.csv")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        raise FileNotFoundError(f"Dataset folder not found: {root}")

    rows, errors = [], []
    hashes = defaultdict(list)

    for split in SPLITS:
        split_dir = root / split
        if not split_dir.is_dir():
            print(f"WARNING: Missing split: {split_dir}")
            continue

        for class_dir in sorted(p for p in split_dir.iterdir() if p.is_dir()):
            for path in sorted(class_dir.rglob("*")):
                if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
                    continue
                try:
                    with Image.open(path) as image:
                        image.verify()
                    with Image.open(path) as image:
                        width, height, image_format = (
                            image.width, image.height, image.format
                        )

                    row = {
                        "split": split,
                        "class": class_dir.name,
                        "path": str(path),
                        "width": width,
                        "height": height,
                        "format": image_format,
                        "sha256": sha256_file(path),
                    }
                    rows.append(row)
                    hashes[row["sha256"]].append(row)
                except (OSError, ValueError, UnidentifiedImageError) as exc:
                    errors.append({
                        "split": split,
                        "class": class_dir.name,
                        "path": str(path),
                        "error": str(exc),
                    })

    inventory = pd.DataFrame(rows)
    inventory.to_csv(args.output, index=False)

    print("\\nImages by split:")
    if not inventory.empty:
        print(inventory.groupby("split").size().reindex(
            SPLITS, fill_value=0
        ).to_string())
        print("\\nClasses by split:")
        print(inventory.groupby("split")["class"].nunique().to_string())

    duplicate_groups = [items for items in hashes.values() if len(items) > 1]
    cross_split = [
        items for items in duplicate_groups
        if len({item["split"] for item in items}) > 1
    ]

    print(f"\\nReadable images: {len(inventory)}")
    print(f"Unreadable images: {len(errors)}")
    print(f"Unique SHA-256 hashes: {len(hashes)}")
    print(f"Exact duplicate groups anywhere: {len(duplicate_groups)}")
    print(f"Exact duplicate groups crossing splits: {len(cross_split)}")
    print(f"Inventory saved to: {Path(args.output).resolve()}")

    if errors:
        error_file = Path(args.output).with_name("dataset_audit_errors.csv")
        pd.DataFrame(errors).to_csv(error_file, index=False)
        print(f"Error report saved to: {error_file.resolve()}")


if __name__ == "__main__":
    main()
