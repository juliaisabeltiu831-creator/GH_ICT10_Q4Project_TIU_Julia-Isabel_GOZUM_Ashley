from pyscript import document, display, when
import numpy as np

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib
matplotlib.set_loglevel("error")

import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
absences = np.array([0, 0, 0, 0, 0])

def display_graph():
    document.getElementById("graph").innerHTML = ""

    fig, ax = plt.subplots(figsize=(9, 5))

    x = np.arange(len(days))

    ax.plot(x, absences, marker='o', linewidth=3)
    ax.fill_between(x, absences, alpha=0.2)

    ax.set_xticks(x)
    ax.set_xticklabels(days)
    ax.set_ylabel('Number of Absences')
    ax.set_xlabel('Day')
    ax.set_title('Weekly Attendance (Absences)')
    ax.set_ylim(bottom=0)

    display(fig, target="graph")


def update_absences(event):
    day = document.getElementById('day-select').value
    value = document.getElementById('absence-input').value

    if value == "":
        return

    abs_num = int(value)
    index = days.index(day)

    absences[index] = abs_num

    display_graph()


@when("click", "#update-btn")
def handle_click(event):
    update_absences(event)


display_graph()
