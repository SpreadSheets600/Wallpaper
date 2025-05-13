import os
from pathlib import Path

BASE_DIR = Path("Wallpapers")


def generate_main_index(base_dir, categories):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallpapers | Simple Wallpaper Collection</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/jetbrains-mono@4.5.0/index.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Wallpapers</h1>
        <p>Simple Wallpaper Collection</p>
    </header>
    
    <main>
        <section class="categories">
"""

    for cat in categories:
        html += f"""
            <a href="Wallpapers/{cat}/index.html" class="category-button">
                {cat.title()}
            </a>
"""

    html += """
        </section>
    </main>

    <footer>
        <p>&copy; 2025 <a href="https://github.com/SpreadSheets600" target="_blank" style="color: inherit; text-decoration: underline;">SpreadSheets</a></p>
    </footer>
</body>
</html>"""

    css = """body {
    font-family: 'JetBrains Mono', monospace;
    margin: 0;
    padding: 20px;
    line-height: 1.6;
}

header {
    text-align: center;
    margin-bottom: 40px;
}

h1 {
    font-size: 2.5em;
    margin: 0;
}

main {
    max-width: 1200px;
    margin: 0 auto;
}

.categories {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    padding: 20px;
}

.category-button {
    display: block;
    padding: 15px 20px;
    background: #f0f0f0;
    border: 1px solid #ddd;
    text-align: center;
    text-decoration: none;
    color: #000;
    border-radius: 4px;
    transition: background-color 0.2s;
}

.category-button:hover {
    background: #e0e0e0;
}

.image-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
}

.image-card {
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 4px;
}

.image-card .thumbnail {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 2px;
    cursor: pointer;
}

.image-card .title {
    margin: 10px 0;
    font-size: 0.9em;
    text-align: center;
}

footer {
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    font-size: 0.9em;
}

.back-link {
    display: inline-block;
    margin-bottom: 20px;
    color: #000;
    text-decoration: none;
    padding: 5px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.back-link:hover {
    background: #f0f0f0;
}"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(css)

    print("Gemerated Main Site")


def generate_category_page(base_dir, category, image_files):
    category_dir = base_dir / category

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{category.title()} - Wallpapers</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/jetbrains-mono@4.5.0/index.css">
    <link rel="stylesheet" href="../../styles.css">
</head>
<body>
    <header>
        <a href="../../index.html" class="back-link">← Back to Categories</a>
        <h1>{category.title()}</h1>
    </header>

    <main>
        <div class="image-grid">
"""

    for img in image_files:
        html += f"""
            <div class="image-card">
                <a href="{img}" target="_blank">
                    <img src="{img}" alt="{img}" class="thumbnail" loading="lazy">
                </a>
                <div class="title">{img}</div>
            </div>
"""

    html += """
        </div>
    </main>

    <footer>
        <p>&copy; 2025 <a href="https://github.com/SpreadSheets600" target="_blank" style="color: inherit; text-decoration: underline;">SpreadSheets</a></p>
    </footer>
</body>
</html>"""

    with open(category_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated Site For {category_dir}")


def main():
    categories = [d.name for d in BASE_DIR.iterdir() if d.is_dir()]
    generate_main_index(BASE_DIR, categories)

    for cat in categories:
        cat_path = BASE_DIR / cat
        images = [
            img
            for img in os.listdir(cat_path)
            if img.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp"))
        ]
        generate_category_page(BASE_DIR, cat, images)


if __name__ == "__main__":
    main()
