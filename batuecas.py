# -*- coding: utf-8 -*-
"""
Created on Sat May  6 09:40:29 2023

@author: Batuecas & Rey
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.axis import Axis 




#definir datos animales
perro1=np.deg2rad([120,124,110,10,120,122,125,160,130,134,110]);
perro2=np.deg2rad([260,2550,235,245,267,310,290,260,265.260,210]);
perro3=np.deg2rad([270,280,280,275,260,300,280,270,255,240,200,199,177,174,1,]);
perro4=np.deg2rad([10,300,200,150,20,350,250,100,270,50,80,280]);
perro5=np.deg2rad([300,305,300,320,310,290,310,305,300,10,300,303,305,320,310,300,302,120,305]);
perro6=np.deg2rad([201,201,201,201,210,201,201,201,210,201,210,201,201,201]);

#definir nombres de animales
nombres=["Coco","Lisa","Tambo","Thor","Stanley","Kubrick"];

#definir mediciones de cada animal (añadir según numero de animales)
medidasP1 = np.linspace(1, len(perro1),len(perro1));
medidasP2 = np.linspace(1, len(perro2),len(perro2));
medidasP3 = np.linspace(1, len(perro3),len(perro3));
medidasP4 = np.linspace(1, len(perro4),len(perro4));
medidasP5 = np.linspace(1, len(perro5),len(perro5));
medidasP6 = np.linspace(1, len(perro6),len(perro6));








#definir opacidad, tamaño puntos y si los ejes son como brujula o no
opacidad = 0.8;
escalaColor = 'hsv';
tamaño = 80; 
puntosCardinales = False;

#graficos
fig = plt.figure(dpi=300,figsize=(5,5));

#subrafico, uno por animal, añadir si es necesario
graf = fig.add_subplot(projection='polar');
graf.scatter(perro1,medidasP1,label=nombres[0],alpha = opacidad, s = tamaño);
graf.scatter(perro2,medidasP2,label=nombres[1],alpha = opacidad, s = tamaño);
graf.scatter(perro3,medidasP3,label=nombres[2],alpha = opacidad, s = tamaño);
graf.scatter(perro4,medidasP4,label=nombres[3],alpha = opacidad, s = tamaño);
graf.scatter(perro5,medidasP5,label=nombres[4],alpha = opacidad, s = tamaño);
graf.scatter(perro6,medidasP6,label=nombres[5],alpha = opacidad, s = tamaño);

#formato del gráfico
graf.legend(loc='center right', shadow=True, bbox_to_anchor=(1.4, 0.5));
graf.set_theta_zero_location("N");
if puntosCardinales :
    graf.set_thetagrids(range(0,360,int((360/8))),('N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE'));
graf.plot
formatter = ticker.FormatStrFormatter('%1.0f');
Axis.set_major_formatter(graf.yaxis, formatter);


#Titulo, cambiar según se precise
plt.title('Localización por perro',fontsize=14);
plt.show();
