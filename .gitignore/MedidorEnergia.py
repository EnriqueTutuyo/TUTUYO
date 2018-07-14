#!/usr/bin/python
# python 2.7.14
from Tkinter import *
import tkFont
import MedidorSPI
################################################################
ROOT = Tk()
ROOT.title('Medidor de Energia* Trifasica ADE7758A')
ROOT.configure(bg ='#333333')
font01= tkFont.Font(family="Helvetica", size=20, weight="bold")
font02= tkFont.Font(family="Helvetica", size=12, weight="bold")
################################################################
cl01="#c8f945" #color letra
cl02="#FFFFFF" #color letra
cf01="#4D4D4D" #color fondo
texto01=["FASE A","FASE B","FASE C","MEDIDORES"]
texto02= ['Vrms =','Irms =','P [ W ] =','Q [ VAR ] =','S [ VA ] =','f.p.=','F [ Hz ] =']
texto03=["MEDIDOR 01","MEDIDOR 02","MEDIDOR 03","MEDIDOR 04","MEDIDOR 05","MEDIDOR 06","SALIR"]
#################################################################
def FMD01():
	b=3*texto02
	a=MedidorSPI.funcion01()
	j=0
	for i in b:
		VctEntry[j].delete(0,END)
		VctEntry[j].insert(0,a[j])
		j=j+1
	print "Medidor 01"
	
def FMD02():
	b=3*texto02
	a=MedidorSPI.funcion02()
	j=0
	for i in b:
		VctEntry[j].delete(0,END)
		VctEntry[j].insert(0,a[j])
		j=j+1
	print "Medidor 02"

def FMD03():
	b=3*texto02
	a=MedidorSPI.funcion03()
	j=0
	for i in b:
		VctEntry[j].delete(0,END)
		VctEntry[j].insert(0,a[j])
		j=j+1
	print "Medidor 03"
	
def FMD04():
	b=3*texto02
	a=MedidorSPI.funcion04()
	j=0
	for i in b:
		VctEntry[j].delete(0,END)
		VctEntry[j].insert(0,a[j])
		j=j+1
	print "Medidor 04"
	
def FMD05():
	b=3*texto02
	a=MedidorSPI.funcion05()
	j=0
	for i in b:
		VctEntry[j].delete(0,END)
		VctEntry[j].insert(0,a[j])
		j=j+1
	print "Medidor 05"
	

def FMD06():
	b=3*texto02
	a=MedidorSPI.funcion06()
	j=0
	for i in b:
		VctEntry[j].delete(0,END)
		VctEntry[j].insert(0,a[j])
		j=j+1
	print "Medidor 06"

def FSLR():
	ROOT.destroy()
#################################################################
VctFMD=[FMD01,FMD02,FMD03,FMD04,FMD05,FMD06,FSLR]
VctLblFrm=[]# vector label frame
VctEntry=[]# vector Entry
cl=0 # columna
for i in texto01:
	fl=0# fila
	LF= LabelFrame(ROOT, text=i,font=font01,bg=cf01,fg=cl01)
	LF.grid(row=fl,column=cl,padx=10,pady=10)
	VctLblFrm.append(LF)
	if (cl<3):
		for j in texto02:
			LB=Label(VctLblFrm[cl], text=j,font=font02,bg=cf01,fg=cl02)
			LB.grid(row=fl,column=0,padx=10,pady=10)
			EN01=Entry(VctLblFrm[cl],width=10,font=font02,bg=cf01,fg=cl02)
			EN01.grid(row=fl,column=1,padx=10,pady=10)
			EN01.insert(0,0.0)
			VctEntry.append(EN01)
			fl=fl+1
	else:
		BTN=texto03
		for j in texto03:
			BTN[fl]=Button(VctLblFrm[cl], text=j,font=font02,bg=cf01,fg=cl02,command=VctFMD[fl])
			BTN[fl].grid(column=0,row=fl,padx=10,pady=5,ipadx=40)
			fl=fl+1
	cl=cl+1
	
ROOT.mainloop()
