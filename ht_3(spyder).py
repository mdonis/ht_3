# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:01:44 2021

@author: mdonis
"""
import os
# Definiendo directorio para descarga
os.chdir('C:/Users/mdonis/Documents/Maestría Data Science/Ciencia de Datos en Python/ht_3')





class my_regression():
    pass
    def __init__(self, x, y):
        #%% asignación de listas
        self.x = x 
        self.y = y
        
        #%% cálculo y asignación de b0 y b1
        a,b,c,d = 0,0,0,0
        n = len(x)        
        
        for i in range(0, n):
            a = a + x[i]*y[i]
            b = b + x[i]
            c = c + y[i]
            d = d + x[i]**2
        
        self.b0 = (d*c - b*a) / (n*d - b**2)
        self.b1 = (n*a - b*c) / (n*d - b**2)
        
        #%% cálculo de R2 y R (evitando duplicar este cálculo en
        ### los métodos R2 y R)
        y_m = sum(y)/len(y)
        y_h = []
        for i in y:
            y_hi = self.b0 + (self.b1)*i
            y_h.append(y_hi)
    
        e,m = 0,0
        for i, j in zip(y, y_h):
           e = e + (i-j)**2
           m = m + (i-y_m)**2
           
        self.r2 = 1-e/m
        self.r = (self.r2)**(1/2)
    
    def predict(self, val):
        #%% asignación de valor x y cálculo de predicción
        self.val = val
        y_h = self.b0 + (self.b1)*val
        return y_h
        
    def predictN(self, vals):
        #%% asinación de lista "vals" y cálculo de predicciones
        self.vals = vals
        y_h = []
        for i in vals:
            y_hi = self.b0 + (self.b1)*i
            y_h.append(y_hi)
        return y_h
    
        #%% para los métodos R2 y R únicamente se llaman las variables
        ### (esto evita que se deba calcular R2 antes que R)
    def R2(self):
        return self.r2
    
    def R(self):
        return self.r
    
        #%% se crea un diccionario con las variables del constructor principal
    def getAllParams(self):
        getall = {'b0':self.b0,'b1':self.b1,'r2':self.r2,'r':self.r}
        return getall
        
    @classmethod
    def from_file(cls, path):
        x = []
        y = []
        
        #%% se abre el archivo csv, se divide por coma cada linea y cada sección
        ### del resultado se deposita iterativamente en dos listas vacías
        with open('C:/Users/mdonis/Documents/Maestría Data Science/Ciencia de Datos en Python/ht_3/{}.csv'.format(path)) as dataset:
            next(dataset)
            for i in dataset:
                l = i.split(',')
                y.append(float(l[0]))
                x.append(float(l[1]))
        
        #%% se crea un objeto en la clase principal cuyos parámetros son las listas
        ### provenientes del archivo csv
        obj_from_csv = my_regression(x, y)
        
        #%% aprovechando los métodos ya creados para este tipo de objetos, se obtiene
        ### todos los parámetros de la regresión lineal
        return obj_from_csv.getAllParams()
        
#%% listas para calcular regresión       
x = [1,2,3,4,5,6,7,8,9]
y = [1.2,2.10,3.5,4,5,6.3,5,8,20]

#%% se define un objeto adentro de la clase con las listas como parámetros
obj = my_regression(x,y)

#%% esta sección permite probar los métodos
obj.predict(10)
obj.predictN([1,2,8])
obj.R2()
obj.R()
obj.getAllParams()

#%% finalmente se aplica el método de regresión lineal desde un archivo
### con el nombre de archivo como parámetro
my_regression.from_file('Advertising')









    