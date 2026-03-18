# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:44:10 2024

@author: theof
"""

from Rauzy_Veech import normalisation, renorm, segment, getcoef, compare, affiche   
from fractions import Fraction
from Essais import parametres
ttab=3
alpha=Fraction(3,8)
der=Fraction(3,2)
toptab, bottab, ltoptab, lbottab = parametres(alpha,der)
iteration=1
init_toptab=toptab[:]
init_bottab=bottab[:]
init_ltoptab=ltoptab[:]
init_lbottab=lbottab[:]

segment(toptab, bottab, ltoptab, lbottab, 0, beta=alpha, pente=der)
coef=getcoef(toptab, bottab, ltoptab, lbottab)  
toptab, bottab, ltoptab, lbottab =renorm(toptab, bottab, ltoptab, lbottab, coef)
segment(toptab, bottab, ltoptab, lbottab, iteration, beta=alpha, pente=der)
while((not compare(toptab, init_toptab) or not compare(bottab,init_bottab) or not compare(ltoptab,init_ltoptab) or not compare(lbottab,init_lbottab)) and toptab!=[0]*len(toptab) and iteration<25):
   coef=getcoef(toptab, bottab, ltoptab, lbottab)  
   toptab, bottab, ltoptab, lbottab =renorm(toptab, bottab, ltoptab, lbottab, coef)
   iteration=iteration +1
   segment(toptab, bottab, ltoptab, lbottab, iteration, beta=alpha, pente=der)
   
if (iteration <25):
    if(toptab==[0]*ttab):
        print("Les paramètres sont beta = "+str(alpha)+" et lambda = "+str(der)+" ")
        print("Il y a une orbite périodique \n")
                  
    else:
        print("Le nombre de rotation est irrationnel pour beta = "+str(alpha))
            
        print("Les paramètres sont beta = "+str(alpha)+" et lambda = "+str(der)+" ")
        print("Le nombre de rotation est irrationnel \n")
    
else:
      print("Les paramètres sont beta = "+str(alpha)+" et lambda = "+str(der)+" ")
      print("Arrêt après "+str(iteration)+" itérations \n")

