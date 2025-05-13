import os
from pathlib import Path

BASE_DIR = Path("Wallpapers")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}


def main():
    categories = [d for d in BASE_DIR.iterdir() if d.is_dir()]

    for category in categories:
        files = list(category.iterdir())

        for file in files:
            if file.is_file() and file.suffix.lower() not in IMAGE_EXTENSIONS:
                print(f"Deleting Non-Image File : {file}")
                file.unlink()

        image_files = sorted(
            [
                f
                for f in category.iterdir()
                if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
            ]
        )

        for idx, file in enumerate(image_files, 1):
            new_name = category / f"{idx}{file.suffix.lower()}"
            print(f"Renaming {file.name} → {new_name.name}")
            file.rename(new_name)


if __name__ == "__main__":
    main()
