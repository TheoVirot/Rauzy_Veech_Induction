# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:01:33 2024

@author: theof
"""

import matplotlib.pyplot as plt

# Coordonnées des points de départ et d'arrivée des segments
def hsl_to_rgb(h, s, l):
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h * 6) % 2 - 1))
    m = l - c / 2
    r, g, b = 0, 0, 0
    if 0 <= h < 1/6:
        r, g, b = c, x, 0
    elif 1/6 <= h < 1/3:
        r, g, b = x, c, 0
    elif 1/3 <= h < 1/2:
        r, g, b = 0, c, x
    elif 1/2 <= h < 2/3:
        r, g, b = 0, x, c
    elif 2/3 <= h < 5/6:
        r, g, b = x, 0, c
    elif 5/6 <= h < 1:
        r, g, b = c, 0, x
    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)
    return r, g, b

def get_colors(n):
    colors = []
    for i in range(n):
        hue = i / n
        lightness = 0.5
        saturation = 0.9
        rgb = hsl_to_rgb(hue, saturation, lightness)
        colors.append('#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2]))
    return colors

def segment(ttab,btab,lttab,lbtab,k):
    couleurs=get_colors(len(ttab))
    toplong = 0
    botlong = 0
    fig, ax = plt.subplots()
    for i in range (len(ttab)):
        x1, y1=[toplong,toplong+lttab[i]], [1,1]      
        x2, y2 =[botlong,botlong+lbtab[i]], [0, 0]
        toplong=toplong + lttab[i]
        botlong=botlong + lbtab[i]
        

        # Dessin des segments avec des couleurs spécifiques
        for j in range(len(ttab)):
            if(i==ttab[j]):
                ax.plot(x1, y1, color=couleurs[j], linewidth=2)
            if(i==btab[j]):
                ax.plot(x2, y2, color=couleurs[j], linewidth=2)
        plt.title("Étape "+ str(k))
        # Personnalisation de l'affichage
    plt.axis('equal')
        # Affichage du graphique
    plt.show()

