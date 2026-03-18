# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:03:03 2024

@author: theof
"""

# coding: utf-8
 
import tkinter as tk
from tkinter import simpledialog
from fractions import Fraction
import math
import matplotlib.pyplot as plt
from segments_v1 import segment
# Créer une instance de la classe Tk

root=tk.Tk()

stop_clicked = False
# Fonction pour demander à l'utilisateur d'entrer un entier
def ask_integer():
   result = simpledialog.askinteger("Entrer un entier", "Veuillez entrer un nombre entier : ")
   while result is None or result<2:
            print("Entrer une taille correcte")
            result = simpledialog.askinteger("Entrer un entier", "Veuillez entrer un nombre entier : ")
   print("La taille du tableau est de"+str(result))
   return result

def ppcmbas(a, b):
    return abs(a * b) // math.gcd(a, b)

def ppcm(tab):
    ppcm=1
    for i in range (len(tab)):
        ppcm=(ppcmbas(ppcm,tab[i].denominator))
    return ppcm

#_____________________________Lengths_Normalization__________________________

def normalisation(tab1,tab2):
    tabtemp1=tab1[:]
    tabtemp2=tab2[:]
    a=ppcmbas(ppcm(tab1),ppcm(tab2))
    for i in range(len(tab1)):
        tabtemp1[i]=a*tab1[i]
        tabtemp2[i]=a*tab2[i]
    return tabtemp1, tabtemp2
#___________________________________________________________________________


def ask_perm(taille,tb):
    tab=[0]*taille
    chaine= " in "
    if tb:
        chaine=chaine+"top"
    else:
        chaine=chaine+"bottom"
    for i in range (taille):
        tab[i]=simpledialog.askinteger("Permutations", "Entrer the image of the interval" +str(i)+chaine)
        if tab[i]>taille-1:
            tab[i]=simpledialog.askinteger("Be carefull", "The value has to lie between 0 and" + str(taille-1))
        for j in range (i):
            while tab[i]==tab[j] and j!=i:
                tab[i]=simpledialog.askinteger("Be carefull", "the intervall "+ str(j) +" is already sent onto it ! \nEnter the image of the interval "+str(i))
            
    return tab

    
def ask_long(tab,tb):
    ltab=[0]*len(tab)
    chaine= " in "
    if tb:
        chaine=chaine+"top"
    else:
        chaine=chaine+"bottom"
    for i in range (len(tab)):
        ltab[i]=simpledialog.askinteger("Length", "Enter length of interval "+str(i)+chaine)
        while ltab[i]<=0: 
            ltab[i]=simpledialog.askinteger("Length", "Length has to be stricly postive ! \nEnter length of interval"+str(tab[i])+chaine)
        ltab[i]=Fraction(ltab[i],1)
    return ltab

        
def somme(tab,p):
    somme=0
    for i in range (p):
        somme=somme+tab[i]
    return somme

def alpha(tab):
    a=0
    while (tab[a]!=len(tab)-1):
        a=a+1
    return a

def affiche(tab):
    for i in range (len(tab)):
            print(tab[i])
            
def getcoef(ptab1, ptab2,tab1,tab2):
    tab=[0]*len(tab1)
    for i in range (len(tab1)):
        tab[ptab1[i]]=Fraction(tab2[ptab2[i]],tab1[ptab1[i]])
    return tab
        
def compare(tab1,tab2):
    for i in range (len(tab1)):
        if(tab1[i]!=tab2[i]):
            return False
    return True

#_____________ONE STEP RAUZY-VEECH INDUCTION__________________________   

"""Entries: take 5 arrays as entries: 2 for the combinatorics of the permutations"; 2 for the lengths of each 
of the top and bottom intervals, and one last for the slope of the piecewise affine map corresponding *

*this last slop tab could be deduced by taking the correspondings rations but it was more convenient to put
it also as a parameter"""      

def renorm(ttab,btab,lttab,lbtab,pente):
    alphat=alpha(ttab)
    alphab=alpha(btab)
    newttab=ttab[:]
    newbtab=btab[:]
    newlttab=lttab[:]
    newlbtab=lbtab[:]
    
    for k in range(len(ttab)-1):
        if somme(lttab,k)==somme(lbtab,k):
            newttab=[0]*(len(ttab))
            return newttab, newbtab, newlttab, newlbtab
    
    if somme(lttab,len(ttab)-1)<somme(lbtab,len(ttab-1)):
        newlbtab[btab[alphat]]=(lttab[len(ttab)-1]-lbtab[len(ttab)-1])*pente[len(ttab)-1]
        newlbtab[btab[alphat]+1]=lbtab[len(ttab)-1]*pente[len(ttab)-1]
        newlttab[len(ttab)-1]=lttab[len(ttab)-1]-lbtab[len(ttab)-1]
        for i in range (len(ttab)):
            if btab[i]<=btab[alphat]:
                 newbtab[i]=btab[i]
            if btab[alphat]<btab[i] and btab[i]<len(ttab)-1:
                newbtab[i]=btab[i]+1
            if btab[i]==len(ttab)-1:
                newbtab[i]=btab[alphat]+1
        for i in range (len(ttab)):
            if i>btab[alphat]+1:
                newlbtab[i]=lbtab[i-1]
    elif somme(lttab,len(ttab)-1)>somme(lbtab,len(ttab)-1):
        newlttab[ttab[alphab]]=(lbtab[len(ttab)-1]-lttab[len(ttab)-1])*1/pente[ttab[alphab]]
        newlttab[ttab[alphab]+1]=lttab[len(ttab)-1]*1/pente[ttab[alphab]]
        newlbtab[len(ttab)-1]=lbtab[len(ttab)-1]-lttab[len(ttab)-1]
        for i in range(len(ttab)):
            if ttab[i]<=ttab[alphab]:
                newttab[i]=ttab[i]
            if ttab[alphab]<ttab[i] and ttab[i]<len(ttab)-1:
                newttab[i]=ttab[i]+1
            if ttab[i]==len(ttab)-1:
                newttab[i]=ttab[alphab]+1
        for i in range (len(ttab)):
            if i>ttab[alphab]+1:
                newlttab[i]=lttab[i-1]

    newlttab,newlbtab=normalisation(newlttab, newlbtab)           
    return newttab, newbtab, newlttab, newlbtab

#_______________________________________________________________________________________
    
ttab=ask_integer()
iteration = 1
toptab=ask_perm(ttab, True)
ltoptab=ask_long(toptab, True)
bottab=ask_perm(ttab, False)
lbottab=ask_long(toptab, False)

init_toptab=toptab[:]
init_bottab=bottab[:]
init_ltoptab=ltoptab[:]
init_lbottab=lbottab[:]

segment(toptab, bottab, ltoptab, lbottab,0)
coef=getcoef(toptab, bottab, ltoptab, lbottab)  
toptab, bottab, ltoptab, lbottab =renorm(toptab, bottab, ltoptab, lbottab, coef) 

segment(toptab, bottab, ltoptab, lbottab,iteration)
print("After renormalisation, top is equal to : ")
affiche(toptab)
print(" et bottom is equal to ")
affiche(bottab)

#__________________________________________________________________________________________________

"""Detecting a periodic step in the Rauzy-Veech induction (irrational rotation number) 

or a connection (periodic orbit)"""

while((not compare(toptab, init_toptab) and not compare(bottab,init_bottab) and not compare(ltoptab,init_ltoptab) or not compare(lbottab,init_lbottab)) and toptab!=[0]*len(toptab)):
   coef=getcoef(toptab, bottab, ltoptab, lbottab)  
   toptab, bottab, ltoptab, lbottab =renorm(toptab, bottab, ltoptab, lbottab, coef)
   iteration=iteration +1
   segment(toptab,bottab,ltoptab,lbottab,iteration)


if(toptab==[0]*ttab):
    print("There exists a periodic orbit")
else:
    print("The rotation number is irrational")
print("Detected after "+str(iteration)+" iterations")

#________________________________________________________________________________________________________


"""

print("Avant renormalisation, top vaut : ")
affiche(init_toptab)
print(" et bottom vaut ")
affiche(init_bottab)
print("Les longueurs de top sont dans l'ordre: ")
affiche(init_ltoptab)
print(" et les longueurs de bot sont dans l'ordre: ")
affiche(init_lbottab)
print("les coef sont: ")
print("Après renormalisation, top vaut : ")
affiche(toptab)
print(" et bottom vaut ")
affiche(bottab)
print("Les longueurs de top sont dans l'ordre: ")
affiche(ltoptab)
print(" et les longueurs de bot sont dans l'ordre: ")
affiche(lbottab)
    
   """


root.mainloop()


