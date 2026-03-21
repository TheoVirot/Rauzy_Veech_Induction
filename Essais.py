# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:58:58 2024

@author: theof
"""
from Rauzy_Veech import normalisation, renorm, segment, getcoef, compare, affiche   
from fractions import Fraction
import math

def parametres(beta,pente):
    ptab1=[0,1,2]
    ptab2=[2,0,1]
    ttab1=[beta,Fraction(pente+beta,pente+1)-beta,1-Fraction(pente+beta,pente+1)]
    ttab2=[Fraction(1-beta,pente+1),1-beta-Fraction(1-beta,pente+1),beta]
    ttab1,ttab2 = normalisation(ttab1,ttab2)
    return ptab1, ptab2, ttab1,ttab2

def valide(t,p,q):
    tab=[]
    for k in range (t+1):
        rang=0
        for l in range(t+1):
            j=rang
            a=Fraction(j*(p+q),(p**l)*(q**k))-Fraction(p,q)
            
            while(a<0):
                rang=rang+1
                j=j+1
                a=Fraction(j*(p+q),(p**l)*(q**k))-Fraction(p,q)
            while(a<1):
                tab.append(a)
                j=j+1
                a=Fraction(j*(p+q),(p**l)*(q**k))-Fraction(p,q)
                
           
    return tab


def Try():
    for i in range (len(tab)):
            ttab=3
            iteration = 1
            alpha=tab[i]
            print("Les paramètres sont beta = "+str(alpha)+" et lambda = "+str(dérivée))
            toptab, bottab, ltoptab, lbottab = parametres(alpha, dérivée)
            
        
            init_toptab=toptab[:]
            init_bottab=bottab[:]
            init_ltoptab=ltoptab[:]
            init_lbottab=lbottab[:]
        
           
            coef=getcoef(toptab, bottab, ltoptab, lbottab)  
            toptab, bottab, ltoptab, lbottab =renorm(toptab, bottab, ltoptab, lbottab, coef)
            
            while((not compare(toptab, init_toptab) or not compare(bottab,init_bottab) or not compare(ltoptab,init_ltoptab) or not compare(lbottab,init_lbottab)) and toptab!=[0]*len(toptab) and iteration<51 ):
               coef=getcoef(toptab, bottab, ltoptab, lbottab)  
               toptab, bottab, ltoptab, lbottab =renorm(toptab, bottab, ltoptab, lbottab, coef)
               iteration=iteration +1
               
               
        
            if (iteration <50):
                if(toptab==[0]*ttab):
                   
                    with open('results.txt','a') as fichier:
                        fichier.write("Les paramètres sont beta = "+str(alpha)+" et lambda = "+str(dérivée)+" ")
                        fichier.write("Il y a une orbite périodique \n")
                              
                else:
                    print("Le nombre de rotation est irrationnel pour beta = "+str(alpha))
                    with open('results.txt','a') as fichier:
                        fichier.write("Les paramètres sont beta = "+str(alpha)+" et lambda = "+str(dérivée)+" ")
                        fichier.write("Le nombre de rotation est irrationnel \n")
                
            else:
                with open('results.txt','a') as fichier:
                    fichier.write("Les paramètres sont beta = "+str(alpha)+" et lambda = "+str(dérivée)+" ")
                    fichier.write("Arrêt après "+str(iteration)+" itérations \n")

durée=4

dérivée = Fraction(2,7)    
tab=list(set((valide(durée,dérivée.numerator,dérivée.denominator))))

Try()




