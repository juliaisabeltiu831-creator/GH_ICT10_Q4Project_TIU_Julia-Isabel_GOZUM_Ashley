from pyscript import document

# IMAGE DATA (easy to edit)
images = [
    {"src": "images/pic1.jpg", "caption": "First Day of School"},
    {"src": "images/pic2.jpg", "caption": "Class Activity"},
    {"src": "images/pic3.jpg", "caption": "Group Photo"},
    {"src": "images/pic4.jpg", "caption": "School Event"},
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