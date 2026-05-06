from pyscript import document

# IMAGE DATA (easy to edit)
images = [
    {"src": "first.png", "caption": "First Day of School"},
    {"src": "intrams.png", "caption": "Intramurals"},
    {"src": "xmas.png", "caption": "Group Photo"},
    {"src": "food.png", "caption": "School Event"},
]

html = ""

for img in images:
    html += f"""
    <div class="card">
        <img src="{img['src']}">
        <p>{img['caption']}</p>
    </div>
    """

document.getElementById("gallery").innerHTML = html
