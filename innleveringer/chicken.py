

import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
import numpy as np


def demand_curve(c,Q,y,pb):
    #Programmer ligning 14 her. Bruk c.log() for å regne ut logaritmen.
    
    return demand

def supply_curve_long_run(c,Q,N,X,pf,t):
    #Programmer ligning 15 her. Bruk c.log() for å regne ut logaritmen.
    
    return supply


def supply_curve_short_run(c,Q,N,X,pf,t,Q_fitted):
    #Programmer ligning 16 her. Bruk c.log() for å regne ut logaritmen.
    
    return supply


def equate_q(y,pb,N,X,pf,t):
    #Finn verdien for Q som gør at demand_curve og supply_curve_long_run returnerer samme verdi. 
    #Bruk sp.Eq, og la første argument i funksjonene over være sp
    
    return float(sol)


def plot_year(df,year):


    #obtaining the relevant variables for year:
    d=df[df['YEAR']==year].to_dict(orient='records')[0]
    
    cpi=d['CPI']
    y=np.log(d['Y'])
    pb=np.log(d['PBEEF']/cpi)
    N=d['POP']
    X=d['MEATEX']
    pf=np.log(d['PF']/cpi)
    t=d['TIME']
    

    
    #obtaining equilibrium quantity:
    Q_fitted=equate_q(y,pb,N,X,pf,t) 
    

    #plotting the functions:
    
    #plot alle tre funksjonene her. 
    #Husk at 
    #1. funksjonene skal opphøyes i eksponenten (dvs. du bruker np.exp(<funksjon>)) for å uttrykkes i nivå
    #2. så skal de multipliseres med cpi
    #3. første argument er np her, ikke sp. 
    

    
    plt.show()