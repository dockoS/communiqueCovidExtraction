import cv2 
import pytesseract
from collections import OrderedDict
img1=cv2.imread("/Users/macbook/Desktop/projetMbacke/photos/EyM9hvkWQAEemyA.jpeg")
text1=pytesseract.image_to_string(img1,lang="eng")
print(text1)
month={"JANVIER":1,"FEVRIER":2,"MARS":3,"AVRIL":4,"MAI":5,"JUIN":6,"JUILLET":7,"AOUT":8,"SEPTEMBRE":9,"OCTOBRE":10,"NOVEMBRE":11,"DECEMBRE":12}
class DataAcquisition():
    def __init__(self):
        self.num_communique=0;
        self.date_communique=OrderedDict();
        self.date_extraction=OrderedDict();
        self.nombre_tests=OrderedDict();
        self.nombre_positifs=OrderedDict();
        self.nombre_cas_contacts=OrderedDict();
        self.nombre_cas_importes=OrderedDict();
        self.nombre_cas_communautaire=OrderedDict();
        self.nombre_deces=OrderedDict();
        self.nombre_gueris=OrderedDict();
        self.nombre_cas_grave=OrderedDict();
        self.nombre_vaccines=OrderedDict();
        self.nombre_cas_communautaire_par_region=OrderedDict();
        self.nombre_cas_communautaire_par_localite_Dakar=OrderedDict();
        
    def get_num_communique(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="COMMUNIQUE":
                self.num_communique=int(tab_texte[i+1])
                return self.num_communique
    def get_date_communique(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="Dakar,":
                #La date vient apres le "le" car le format est Dakar, le ... 
                return tab_texte[i+2]
    def get_nombre_tests(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="tests" or tab_texte[i]=="test":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="realisés" or tab_texte[i+1]=="realisé":  
                     if (tab_texte[i-1].lower()=="aucun"):
                            tab_texte[i-1]="0"
                     return int(tab_texte[i-1])
                   
    def get_nombre_positifs(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="sont" or tab_texte[i]=="est":
                #La nombre vient apre le premier mot "Sur"
                 if tab_texte[i+1]=="revenus" or tab_texte[i+1]=="revenu":    
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nombre_cas_contacts(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas" :
                if tab_texte[i+1]=="contact" or tab_texte[i+1]=="contacts":  
                #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nombre_cas_communautaire(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas":
                 if tab_texte[i+1]=="issus" or tab_texte[i+1]=="issu":  
                #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1])
    def get_nombre_cas_importes(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="importé" or tab_texte[i+1]=="importés":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nombre_gueris(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="patients" or tab_texte[i].lower()=="patient":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="suivis" or tab_texte[i+1]=="suivi":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nombre_deces(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="décés":
                #La nombre vient apre le premier mot "Sur"
                if (tab_texte[i-1].lower()=="aucun"):
                    tab_texte[i-1]="0"
                return int(tab_texte[i-1]) 
    def get_nombre_cas_graves(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="graves" or tab_texte[i+1]=="grave":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nombre_vaccines(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="personnes" or tab_texte[i].lower()=="personne":
                if "vaccinées" or "vaccinée" in tab_texte[i:i+6]:
                    #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
        
        
dA=DataAcquisition()
print(dA.get_nombre_vaccines(text1))
print(dA.get_nombre_gueris(text1))
print(dA.get_nombre_cas_contacts(text1))

            