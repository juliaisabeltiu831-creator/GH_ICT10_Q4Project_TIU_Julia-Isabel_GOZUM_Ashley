from pyscript import document

# IMAGE DATA (easy to edit)
images = [
    {"src": "first.jpg", "caption": "First Day of School"},
    {"src": "intrams.jpg", "caption": "Intramurals"},
    {"src": "xmas.jpg", "caption": "Group Photo"},
    {"src": "food.jpg", "caption": "School Event"},
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
