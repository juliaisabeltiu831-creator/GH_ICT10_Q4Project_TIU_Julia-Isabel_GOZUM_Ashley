from pyscript import document, window

class Classmate:
    def __init__(person, name, section, favorite_subject):
        person.name = name
        person.section = section
        person.favorite_subject = favorite_subject

    def introduce(person):
        return f"Hi! I am {person.name.title()} from {person.section}. My favorite subject is {person.favorite_subject}."


classmates = [
    Classmate("abayon", "Emerald", "Math"),
    Classmate("antes", "Emerald", "Math"),
    Classmate("apostol", "Emerald", "Math"),
    Classmate("banaag", "Emerald", "Math"),
    Classmate("barrientos", "Emerald", "Math"),
    Classmate("casal", "Emerald", "Math"),
    Classmate("coeli", "Emerald", "Math"),
    Classmate("david", "Emerald", "Math"),
    Classmate("de mata", "Emerald", "Math"),
    Classmate("dela cruz f", "Emerald", "Math"),
    Classmate("dela cruz j", "Emerald", "Math"),
    Classmate("dellejero", "Emerald", "Math"),
    Classmate("fukuda", "Emerald", "Philosophy"),
    Classmate("gozum", "Emerald", "Philosophy"),
    Classmate("ibay", "Emerald", "Philosophy"),
    Classmate("lim", "Emerald", "Philosophy"),
    Classmate("lozano", "Emerald", "Philosophy"),
    Classmate("mamauag", "Emerald", "Philosophy"),
    Classmate("navarro", "Emerald", "Philosophy"),
    Classmate("precones", "Emerald", "Philosophy"),
    Classmate("ramos", "Emerald", "Philosophy"),
    Classmate("sidhu", "Emerald", "Science"),
    Classmate("tiu", "Emerald", "Science"),
    Classmate("villamayor", "Emerald", "Science"),
    Classmate("zaragoza", "Emerald", "Science"),
]


def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    classmates.append(Classmate(name, section, subject))

    document.getElementById("output").innerHTML = "Classmate added successfully!"


def show_list(e):
    output = ""

    for c in classmates:
        output += c.introduce() + "<br>"

    document.getElementById("output").innerHTML = output


window.add_classmate = add_classmate
window.show_list = show_list