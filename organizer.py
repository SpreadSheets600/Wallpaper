import re
import os
from pathlib import Path

BASE_DIR = Path("Wallpapers")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}


def is_numbered(filename):
    return filename.isdigit()


def extract_number(filename):
    try:
        return int(filename)
    except ValueError:
        return -1


def main():
    print("🔍 Scanning Categories...\n")

    categories = [d for d in BASE_DIR.iterdir() if d.is_dir()]

    for category in categories:
        print(f"\n📁 Category: {category.name}")
        files = list(category.iterdir())

        for file in files:
            if file.is_file() and file.suffix.lower() not in IMAGE_EXTENSIONS:
                print(f"🗑️ Deleting Non Image File: {file.name}")
                file.unlink()

        image_files = sorted(
            [
                f
                for f in category.iterdir()
                if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
            ]
        )

        max_number = 0
        for file in image_files:
            name = file.stem
            if is_numbered(name):
                num = extract_number(name)
                if num > max_number:
                    max_number = num

        new_index = max_number + 1
        renamed_count = 0
        skipped_count = 0

        for file in image_files:
            name = file.stem
            if not is_numbered(name):
                new_name = category / f"{new_index}{file.suffix.lower()}"
                print(f"✏️ Renaming: {file.name} → {new_name.name}")
                file.rename(new_name)
                new_index += 1
                renamed_count += 1
            else:
                skipped_count += 1

        print(f"✅ Done: {renamed_count} Renamed, {skipped_count} Kept")

    print("\n🎉 Finished Processing All Categories")


if __name__ == "__main__":
    main()
