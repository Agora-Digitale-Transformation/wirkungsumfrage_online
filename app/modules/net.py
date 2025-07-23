import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def plot_spinne_ex():

    # Kategorien (ein Index + 4 Subindizes)
    labels = ["Wirkungsinde (gesamt)", "Realisierbarkeit und\nRessourcenausstattung", "Wirkugnslogische Planung\nund Zielklarheit", "Wirkungsmessung und\nevidenzbasiertes Lernen", "Stakeholder- und\nZielgruppeneinbindung"]

    # Beispielwerte (0 bis 100 skaliert)
    values = [75, 60, 80, 65, 70]

    # Wiederholen des ersten Wertes, um das Diagramm zu schließen
    values += values[:1]

    # Winkel für die Achsen
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    # Farben definieren
    farben = {
        "hintergrund": "#ebece9",
        "linie": "#3e3bd4",
        "fläche": "#c978e8",
        "punkte": "#caff34",
        "text": "black"
    }

    # Plot vorbereiten
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("white")
    ax.set_facecolor(farben["hintergrund"])

    # Gitterlinien und Achsen anpassen
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)
    plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color=farben["text"])
    plt.ylim(0, 100)

    # Linien zeichnen
    ax.plot(angles, values, color=farben["linie"], linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=farben["fläche"], alpha=0.4)
    ax.scatter(angles, values, color=farben["punkte"], s=100, zorder=5)

    # Beschriftung
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color=farben["text"])

    plt.title("Index und Subindizes", size=14, color=farben["text"], y=1.08)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close()

    return img_base64