import os
import random as rd
import csv
from copy import *
from numpy import *




def ListeClasse():
    path = os.getcwd()
    os.chdir("Svg Prog")
    with open("ListeClasse.csv", "r") as file:
        cr = csv.reader(file)
        for row in cr:
            ListeClasse = row
    os.chdir(path)
    return ListeClasse




def dossier():
    import os
    os.chdir("Google Drive//Python//Effectif de Classe V4")

dossier()

ListeOptim = []
class Eleve:
    def __init__(self):
        self.nom =  "Babar"
        self.prenom = "Bobor"
        self.genre  = "Adolescent"
        self.voeux = []
        
    def Voeux(self,L):
        #print(L)
        if L[0] == "H":
            self.genre = "Homme"
            #print("Homme")
        else :
            self.genre = "Femme"
            #print("Femme")
        if L[1] == "1":
            self.voeux.append("HLP")
            #print("HLP")
        if L[2] == "1":
            self.voeux.append("Géopol")
            #print("Geopol")
        if L[3] == "1":
            self.voeux.append("LCE")
            #print("LCE")
        if L[4] == "1":
            self.voeux.append("SES")
            #print("SES")
        if L[5] == "1":
            self.voeux.append("Math")
            #print("Math")
        if L[6] == "1":
            self.voeux.append("Phy")
            #print("Phy")
        if L[7] == "1":
            self.voeux.append("SVT")
            #print("SVT")
        if L[8] == "1":
            self.voeux.append("SI")
            #print("SI")
        if L[9] == "1":
            self.voeux.append("NSI")
            #print("NSI")
        self.voeux.sort()


def CSV_Vers_DicoSeconde():
    # On va charger toutes les listes de toutes les classes.
    DicoSeconde = {}
    DicoSave = {}
    try:
        cr = csv.reader(open("Fichier.csv","r"))
        for row in cr:
            DicoSeconde[row[0]] = Eleve()
            DicoSeconde[row[0]].nom = row[0]
            DicoSeconde[row[0]].prenom = row[1]
            DicoSeconde[row[0]].Voeux(row[2:12])
            DicoSave[row[0]] = row[0:12]
            
    except IOError:
        print ("Erreur! Le fichier n' pas pu être ouvert")
    #ListeSeconde.append(TempListeSeconde)
    return [DicoSeconde,DicoSave]


class Classe:
    def __init__(self):
        self.Homme = 0
        self.Femme = 0
        self.N = 0
        self.DicoSpe = {"HLP":0,"Géopol":0,"LCE":0,"SES":0,"Math":0,"Phy":0,"SVT":0,"SI":0,"NSI":0}
        self.DispersionSL = self.DicoSpe["HLP"] + self.DicoSpe["Géopol"] + self.DicoSpe["LCE"] + self.DicoSpe["SES"] - self.DicoSpe["Math"] - self.DicoSpe["Phy"] -self.DicoSpe["SVT"] - self.DicoSpe["SI"] - self.DicoSpe["NSI"]
        self.DicoEleve = {}
    def update(self):
        self.Homme = 0
        self.Femme = 0
        self.N = 0
        self.DicoSpe = {"HLP":0,"Géopol":0,"LCE":0,"SES":0,"Math":0,"Phy":0,"SVT":0,"SI":0,"NSI":0}
        for eleve in self.DicoEleve:
            self.Homme = self.Homme + 1*(self.DicoEleve[eleve].genre == "Homme")
            self.Femme = self.Femme + 1*(self.DicoEleve[eleve].genre == "Femme")
            self.N = self.N + 1
            for matiere in self.DicoSpe:
                self.DicoSpe[matiere] += self.DicoEleve[eleve].voeux.count(matiere)
        self.DispersionSL = self.DicoSpe["HLP"] + self.DicoSpe["Géopol"] + self.DicoSpe["LCE"] + self.DicoSpe["SES"] - self.DicoSpe["Math"] - self.DicoSpe["Phy"] -self.DicoSpe["SVT"] - self.DicoSpe["SI"] - self.DicoSpe["NSI"]
    
    def AjoutEleve(self,Eleve):
        self.DicoEleve[Eleve.nom] = Eleve
        


#Test1.DeplacerEleve(Test1.DicoClasse["Première Géné 1"].DicoEleve,1)

class GroupeDeClasses:
    
    def __init__(self,DicoSeconde):
        self.DicoSeconde = DicoSeconde
        self.DicoSave = DicoSave
        self.DicoClasse = {}
        self.Energie = 1000000
        self.n = 6
        self.EffectifTotal = 0
        
    def FaireClasseGene(self):
        self.DicoClasse.clear()
        for i in range(1,self.n+1):
            nom = "Première Géné " + str(i)
            #print(nom)
            self.DicoClasse[nom] = Classe()
        for eleve in DicoSeconde:
            u = rd.randint(1,self.n)
            #print(u)
            nom = "Première Géné " + str(u)
            #print(nom)
            self.DicoClasse[nom].AjoutEleve(DicoSeconde[eleve])
        for classe in self.DicoClasse:
            self.DicoClasse[classe].update()
            
    def Svg(self):
        path = os.getcwd()
        os.chdir("Svg Prog")
        with open("Energie.txt","w") as file:
            file.write(str(self.Energie))
        with open("n.txt","w") as file:
            file.write(str(self.n))
        with open("ListeClasse.csv","w") as file:
            ListeClasse = ""
            for classe in list(self.DicoClasse.keys()):
                ListeClasse += str(classe) + ","
                ListeEleve = ""
                with open(str(classe) + ".csv","w") as fiile:
                    for eleve in list(self.DicoClasse[classe].DicoEleve.keys()):
                        ListeEleve += str(eleve) + ","
                    ListeEleve = ListeEleve[:len(ListeEleve) - 1]
                    fiile.write(ListeEleve)
            ListeClasse = ListeClasse[:len(ListeClasse)-1]
            file.write(ListeClasse)
        os.chdir(path)

    def RecupSvg(self):
        path = os.getcwd()
        os.chdir("Svg Prog")
        self.DicoClasse.clear()
        with open("n.txt","r") as file:
            self.n = int(file.read())
        with open("Energie.txt","r") as file:
            self.Energie = float(file.read())
        with open("ListeClasse.csv","r") as file: 
            cr = csv.reader(file)
            for row in cr:
                ListeClasse = row
        for classe in ListeClasse:
            self.DicoClasse[classe] = Classe()
            with open(classe + ".csv","r") as file:
                cr = csv.reader(file)
                for row in cr:
                    ListeEleve = row
                for name in ListeEleve:
                    TempEleve = Eleve()
                    TempEleve.nom = name
                    TempEleve.prenom = DicoSave[name][1]
                    Listedename = DicoSave[name][2:]
                    TempEleve.Voeux(Listedename)
                    self.DicoClasse[classe].AjoutEleve(TempEleve)
            self.DicoClasse[classe].update()
        self.Energie = self.CalculEnergie()
        
        os.chdir(path)

    def DeplacerEleve(self,nomClasse,p):
        L = []
        ListeClasse = list(self.DicoClasse.keys())
        for nomEleve in self.DicoClasse[nomClasse].DicoEleve:
            if rd.random() < p:
                L.append(nomEleve)
                tempEleve = self.DicoClasse[nomClasse].DicoEleve[nomEleve]
                u = rd.randint(0,len(ListeClasse)-1)
                #print(nomEleve)
                #print(u+1)
                self.DicoClasse[ListeClasse[u]].AjoutEleve(tempEleve)
        Classe = self.DicoClasse[nomClasse]
        for l in L:
            del Classe.DicoEleve[l]

    def Optim(self,ite):
        m = 0
        #print(m)
        ListeOptim.clear()
        Backup = deepcopy(self)
        EnCours = deepcopy(self)
        EnergieRef = Backup.Energie
        ListeClasse = list(EnCours.DicoClasse.keys())
        print(EnergieRef)
        while m<ite and self.Energie > 30:
            m +=1
            pp=0.3
            for classe in ListeClasse:
                if rd.random()<pp:
                    p = 0.3
                    EnCours.DeplacerEleve(classe,p)
            for classe in ListeClasse:
                EnCours.DicoClasse[classe].update()
            NRJ = EnCours.CalculEnergie()
            ListeOptim.append(NRJ)
            if (m%100 == 0): print(m)
            #print("A m = {1} La Nouvelle Energie est {0}".format(NRJ,m))
            if NRJ < EnergieRef and EnCours.EffectifTotal == Backup.EffectifTotal:
                Backup = deepcopy(EnCours)
                EnergieRef = Backup.Energie
                EnCours.Svg()
                FaireClasseur(EnCours)
            else:
                EnCours = deepcopy(Backup)
        print(EnergieRef)
        self.DicoClasse = EnCours.DicoClasse
        self.Energie = EnCours.Energie
    
    def Recupcsv(self,str):
        self.DicoClasse.clear()
        path = os.getcwd()
        os.chdir(str)
        for name in os.listdir():
            nom = name[:len(name)-4]
            self.DicoClasse[nom] = Classe()
            try:
                cr = csv.reader(open(name,"r"))
                for row in cr:
                    TempEleve = Eleve()
                    TempEleve.nom = row[0]
                    TempEleve.Voeux(row[2:12])
                    TempEleve.Sexe = row[1]
                    self.DicoSave[row[0]] = row[0:12]
                    self.DicoClasse[nom].AjoutEleve(TempEleve)
            except IOError:
                print ("Erreur! Le fichier n' pas pu être ouvert")
            self.DicoClasse[nom].update()
        os.chdir(path)
        self.CalculEnergie()

    def CalculEnergie(self):
        NRJ = 0
        L = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for classe in self.DicoClasse:
            for v in self.DicoClasse[classe].DicoSpe.values():
                if v!=0:
                    L[v] += 1
        for i in range(0,len(L)):
            NRJ += 10*L[i]*exp(-i/5) + 10000*(L[i]>30)
        Effectif = []
        DiffHF = []
        DiffSL = []
        for classe in self.DicoClasse:
            Effectif.append(self.DicoClasse[classe].N)
            DiffHF.append((self.DicoClasse[classe].Homme - self.DicoClasse[classe].Femme))
            DiffSL.append((self.DicoClasse[classe].DispersionSL))
        #print("Energie Alignement {0}      Energie Effectif {1}       Energie Diff Sexe {2}".format(NRJ,std(Effectif),std(DiffHF)))
        self.Energie = 3*NRJ + 10*std(Effectif) + Std0(DiffHF) + Std0(DiffSL)
        self.EffectifTotal = sum(Effectif)
        return self.Energie

        
        
def Std0(L):
    V = 0
    for l in L:
        V += l**2
    return sqrt(V)
        

        
        
        
        
        
        

[DicoSeconde,DicoSave] = CSV_Vers_DicoSeconde()


Test1 = GroupeDeClasses(DicoSeconde)
Test1.RecupSvg()
Test1.CalculEnergie()




import xlrd
from xlwt import Workbook, Formula


def FaireClasseur(GroupeDeClasses):
    classeur = Workbook()
    for classe in Test1.DicoClasse:
        #print(classe)
        feuille = classeur.add_sheet(classe)
        Liste = ["Total","Nom", "Prénom", "Genre","Art","HLP","Géopol","LCE","SES","Math","Phy","SVT","SI","NSI"]
        j= 0
        for l in Liste:
            feuille.write(0,j,l)
            j+=1
        i = 1
        for eleve in Test1.DicoClasse[classe].DicoEleve:
            #print(eleve)
            k = 0
            u = 0
            feuille.write(i,u,1)
            u = 1
            for char in DicoSave[eleve]:
                #print(char)
                text = DicoSave[eleve][k]
                if text == "F":
                    text = "-1"
                if text == "H":
                    text = "1"
                feuille.write(i,u,text)
                k = k + 1 
                u = u + 1
            i = i+1
    classeur.save("test.xls")











       




def Fin():
    a = input("Optimisation : Entrer le nombre d'itération voulue, Mettre autre chose pour avoir le tableau Recap \n")
    try : 
        a = int(a)
        if int(a)>0:
            Test1.Optim(a)
            Test1.Energie
            Fin()
    except:
        from kivy.app import App
        from kivy.core.window import Window
        from kivy.uix.screenmanager import ScreenManager, Screen
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.gridlayout import GridLayout
        from kivy.uix.button import Button
        from kivy.uix.label import Label
        from kivy.properties import ObjectProperty, ListProperty, StringProperty
        from kivy.uix.scrollview import ScrollView
        from kivy.lang import Builder
        from kivy.uix.textinput import TextInput
        
        EnergieLabel = Label(text="Energie = ")
        LL = ["HLP", "Géopol", "LCE", "SES", "Math", "Phy", "SVT", "SI", "NSI"]
        DicoLabel = {}
        Compteur = Label()
        Compteur.size_hint_x = 0.4
        for i in ListeClasse():
            nom = i
            DicoLabel[nom + "N"] = Label()
            DicoLabel[nom + "HF"] = Label()
            for j in LL:
                DicoLabel[nom + j] = Label()
        
        
        sm = ScreenManager()
        
        class MenuScreen(Screen):
            def build(self, n, GroupeDeClasses):
                # Le nom de l'ecran
                self.name = 'Menu'
                self.GroupeDeClasses = GroupeDeClasses
                self.GroupeDeClasses.CalculEnergie()
                # On cree le contenu:
                MenuLayout = BoxLayout(spacing=10, orientation="vertical")

                IndicationLayout = BoxLayout(spacing=10, orientation="horizontal")
                IndicationLayout.size_hint_y = 0.1

                EnergieLabel.text = "Energie = " + str(int(self.GroupeDeClasses.Energie))
                EnergieLabel.size_hint_x = 0.4

                Boutton1 = Button(text="[b] Optimisation, Nombre Itération -----> [/b]", markup=True)
                Boutton1.bind(on_press=self.Optim)

                Boutton2 = Button(text="[b] Récupérer la Classe [/b]", markup=True)
                Boutton2.bind(on_press=self.Recup)
                Boutton2.size_hint_x = 0.4

                self.Ite = TextInput(text=str(1000))
                self.Ite.size_hint_x = 0.3
                IndicationLayout.add_widget(EnergieLabel)

                IndicationLayout.add_widget(Boutton1)

                IndicationLayout.add_widget(self.Ite)

                IndicationLayout.add_widget(Boutton2)

                MenuLayout.add_widget(IndicationLayout)

                Tableau_Layout = GridLayout(padding=20, spacing=10, cols=12)
                L = ["Classe", "Effectif", "Sexe", "HLP", "Géopol", "LCE", "SES", "Math", "Phy", "SVT", "SI", "NSI"]
                LL = ["HLP", "Géopol", "LCE", "SES", "Math", "Phy", "SVT", "SI", "NSI"]
                for j in range(0, 12):
                    Tableau_Layout.add_widget(Label(text="[b]" + L[j] + "[/b]", markup=True))
                for i in list(self.GroupeDeClasses.DicoClasse.keys()):
                    nom = i
                    Tableau_Layout.add_widget(Label(text="[b]" + nom + "[/b]", markup=True))
                    DicoLabel[nom + "N"].text = str(self.GroupeDeClasses.DicoClasse[nom].N)
                    Tableau_Layout.add_widget(DicoLabel[nom + "N"])
                    HF = self.GroupeDeClasses.DicoClasse[nom].Homme - self.GroupeDeClasses.DicoClasse[nom].Femme
                    DicoLabel[nom + "HF"].text = str(HF)
                    Tableau_Layout.add_widget(DicoLabel[nom + "HF"])
                    for j in LL:
                        DicoLabel[nom + j].text = str(self.GroupeDeClasses.DicoClasse[nom].DicoSpe[j])
                        Tableau_Layout.add_widget(DicoLabel[nom + j])  # Mettre Les nombres des Spé
                MenuLayout.add_widget(Tableau_Layout)
                self.add_widget(MenuLayout)
                sm.add_widget(self)

            def Optim(self, instance):
                EnergieLabel.text = "[b] Cela ne bug pas [/b]"
                self.GroupeDeClasses.Optim(int(self.Ite.text))
                EnergieLabel.text = "Energie = " + str(int(self.GroupeDeClasses.Energie))
                L = ["Classe", "Effectif", "Sexe", "HLP", "Géopol", "LCE", "SES", "Math", "Phy", "SVT", "SI", "NSI"]
                LL = ["HLP", "Géopol", "LCE", "SES", "Math", "Phy", "SVT", "SI", "NSI"]
                for i in list(self.GroupeDeClasses.DicoClasse.keys()):
                    nom = i
                    DicoLabel[nom + "N"].text = str(self.GroupeDeClasses.DicoClasse[nom].N)
                    HF = self.GroupeDeClasses.DicoClasse[nom].Homme - self.GroupeDeClasses.DicoClasse[nom].Femme
                    DicoLabel[nom + "HF"].text = str(HF)
                    for j in LL:
                        DicoLabel[nom + j].text = str(self.GroupeDeClasses.DicoClasse[nom].DicoSpe[j])

            def Recup(self, instance):
                FaireClasseur(self)

        class ScreenApp(App):
            def build(self):
                Menu = MenuScreen()  # On definit l'ecran menu
                Menu.build(6, Test1)  # On le construit
                sm.current = 'Menu'  # On envoie en premier l'ecran du menu grace a son nom
                return sm
        ScreenApp().run()

#Fin()