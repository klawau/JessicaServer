# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Title List For Forum Title
# Credits:     SevenOPS(hαcφεƦπøυα™) 
# Version:     0.1 RC3 (31/1/2014)
# Copyright:   (c) Dev-TR 2012-2014
#-------------------------------------------------------------------------------
import ConfigParser
import sqlite3

config = ConfigParser.ConfigParser()
config.read("config.ini")

Database = sqlite3.connect("dbfile.sqlite", check_same_thread = False)
Database.isolation_level = None
Cursor = Database.cursor()
Database.row_factory = sqlite3.Row
Database.text_factory = str


###Title.sql To PY Title List###

##a=open("title.sql","r").readlines()
##title=[]
##for b in a:
##    b=b.replace("\n","")
##    c=b.split(",")
##    no=c[0][1:]
##    isim=((c[1].replace(" '","")).split("')")[0])
##    title.append([no,isim])
##print title

###End###



titlelist=[['5', 'A\xe7g\xf6zl\xfc Fare'], ['6', 'Ahanda ! Peynir !'], ['7', 'Eveeeet Peynir ^^'], ['8', 'Peynirrrrrr *-*'], ['35', 'Eylemci Fare'], ['36', 'Sendikali Fare'], ['37', 'Fare Grevde'], ['26', 'Obur Fare'], ['27', '\xd6g\xfct\xfcc\xfc'], ['28', 'Sisko Fare'], ['29', 'G\xf6bekli Fare'], ['30', 'Tombik Fare'], ['31', 'Pofuduk Fare'], ['32', 'Duba Fare'], ['33', 'Tombis'], ['34', 'Puf'], ['38', 'Peynir Talebesi'], ['39', 'Peynir \xdcstadi'], ['40', 'Peynir Rahibi'], ['41', 'Bi\xe7erd\xf6ver'], ['72', 'Peynir Kasifi'], ['73', 'Peynir S\xf6valyesi'], ['74', 'Peynir Kurdu'], ['75', 'Dobis'], ['76', 'Tiknaz Fare'], ['77', 'Peynir Sever'], ['78', 'Camembert'], ['79', "Pont-L''\xc9v\xeaque"], ['80', 'Peynir Avcisi'], ['81', "It''s Over 9000"], ['82', 'Koleksiyoncu'], ['83', 'Peynir Sefi'], ['84', 'Peynir Hirsizi'], ['85', 'Peynir Yaraticisi'], ['86', 'Peynirli Pizza'], ['87', 'Peynir Bakani'], ['88', 'Olagan\xfcst\xfc Fare'], ['89', 'Princess of Transformice'], ['90', 'Peynirkolik'], ['91', 'Se\xe7ilmis Peynir'], ['92', 'Denizci Fare'], ['234', 'Om Nom Nom'], ['235', '*-*'], ['236', 'Peynir Bagimlisi'], ['237', 'Cheesus'], ['238', 'Peynir Krali\xe7esi'], ['93', 'BENIM PEYNIRIM!'], ['9', 'Hizli Fare'], ['10', 'Atik Fare'], ['11', 'Korsan Fare'], ['12', 'Ninja Fare'], ['42', 'Serseri Fare'], ['43', 'Yagmaci'], ['44', 'Takip\xe7i'], ['45', 'K\xf6p\xfckl\xfc Fare'], ['46', 'Suskun'], ['47', 'Sahin Fare'], ['48', 'Kobra Fare'], ['49', '\xd6r\xfcmcek Fare'], ['50', 'Quick Silver'], ['51', 'Atletik Fare'], ['52', 'Aceleci Fare'], ['53', 'Roket Fare'], ['54', 'Fare Sonic'], ['55', 'Pingsiz'], ['56', 'Kamikaze'], ['57', 'Savas\xe7i Fare'], ['58', 'Mach 1'], ['59', 'Avci'], ['60', 'Birinci!'], ['61', 'Nisanci'], ['62', 'Flas'], ['63', 'S\xfcperfare'], ['64', 'Isik Hizi'], ['65', 'Zaman Yolcusu'], ['66', 'Hizli R\xfczgar'], ['67', 'E=MouseC\xb2'], ['68', 'Atlayici'], ['69', 'Dokunulmaz'], ['231', 'Dinamit'], ['232', 'Hiz Ustasi'], ['233', 'Kasirga'], ['70', 'Wall-Jumper'], ['224', 'Kosucu'], ['225', 'Yarasa Fare'], ['226', 'G\xf6r\xfcnmeyen'], ['227', 'Durdurulamaz'], ['202', 'R\xfczgarin Efendisi'], ['228', '\xa1\xc1ndale! \xa1\xc1ndale!'], ['229', 'Torpido'], ['230', 'Hizli Gonzales'], ['71', 'YILDIRIM'], ['1', '\xd6grenci Saman'], ['2', 'Basarili Saman'], ['3', 'Saman'], ['4', 'Usta Saman'], ['13', 'Ilhamli Saman'], ['14', 'Sampiyon Saman'], ['15', 'Sanli Saman'], ['16', 'D\xfcses Saman'], ['17', 'Prenses Saman'], ['18', 'Imparatori\xe7e Saman'], ['19', 'Efsanevi Saman'], ['20', '\xd6l\xfcms\xfcz Saman'], ['21', 'Se\xe7ilmis Saman'], ['22', 'Kutsal Saman'], ['23', 'K\xe2hin Saman'], ['24', 'El\xe7i Saman'], ['25', 'Samuhtesem'], ['94', 'Kadim Saman'], ['95', 'Korkusuz Saman'], ['96', 'Her Seye K\xe2dir'], ['97', 'Mimar Saman'], ['98', 'Matmazel'], ['99', 'Samaniye'], ['100', 'Sevilen'], ['101', 'Sihirbaz'], ['102', 'Farelerin Kahramani'], ['103', 'Melek Saman'], ['104', 'Yaratici'], ['105', 'Mutlak Saman'], ['106', 'Mucizevi Saman'], ['107', 'Kurtarici'], ['108', 'Troll Saman'], ['109', 'Hayalet Saman'], ['110', 'Ruh'], ['111', 'Kahraman Saman'], ['112', 'Son Umut'], ['113', 'Mesih'], ['200', 'Ilahe Saman'], ['114', 'Alpha & Omega'], ['213', 'Dekorat\xf6r'], ['214', 'M\xfcteahhit'], ['215', 'Fabrikat\xf6r'], ['216', 'Tekniker'], ['217', 'Makinist'], ['218', 'Uzman'], ['219', 'Mucit'], ['220', 'M\xfchendis'], ['221', 'Yaratici Fare'], ['222', 'Marifetli Fare'], ['223', '\xdcst\xe2t'], ['256', 'Rookie'], ['257', 'Neophyte'], ['258', 'Private'], ['259', 'Deft Mouse'], ['260', 'Solo Artist'], ['261', 'Corporal'], ['262', 'Accurate Mouse'], ['263', 'Bootcampeur'], ['264', 'Sergeant'], ['265', 'Corner Jumper'], ['266', 'Skilled Mouse'], ['267', 'Lieutenant'], ['268', 'Longjumper'], ['269', 'Incredimouse'], ['270', 'Bootcamp Addict'], ['271', 'Captain'], ['272', 'Dexterous Mouse'], ['273', 'Maniac'], ['274', 'Major'], ['275', 'Cheese Artist'], ['276', 'Acrobat'], ['277', 'Colonel'], ['278', 'Shortcutter'], ['279', 'Tarzan'], ['280', 'General'], ['281', 'Living Legend'], ['282', 'Stuntmouse'], ['283', 'Pro'], ['284', 'Chuck Souris'], ['285', 'Queen of Bootcamp'], ['286', 'Gravity Master'], ['246', 'Dauphine'], ['247', 'Foxy'], ['248', 'Miss Transformice'], ['252', 'Souris Lilloise'], ['253', 'Tonnerre de Brest'], ['254', 'Chocovore'], ['255', 'Chocobunny'], ['295', 'Chicken'], ['440', 'Fromadmin'], ['442', 'Sourigami'], ['444', 'La Belette'], ['445', 'El Pinolero'], ['447', 'Kikoo Admin'], ['448', 'Queijadinha'], ['446', 'Dehset Admin'], ['115', 'Hos Fare'], ['116', 'Sevimli Fare'], ['117', '\xc7ekici Fare'], ['118', 'G\xfczel Fare'], ['119', 'Tatli Fare'], ['120', 'Fingirdek Fare'], ['121', 'Z\xfcppe Fare'], ['122', 'Havali Fare'], ['123', 'Artist Fare'], ['124', 'Modaci Fare'], ['125', 'Seksi'], ['126', 'S\xfcperstar'], ['287', 'Vampire'], ['127', 'Minik Kar Tanesi'], ['128', 'Noel Ruhu'], ['129', 'K\xfc\xe7\xfck Peri'], ['130', 'Noel Baba'], ['240', 'Cookies'], ['241', 'Christmas Cake'], ['242', 'Whitebeard'], ['243', 'Generous'], ['244', 'Snowy'], ['245', 'Snowstorm'], ['288', 'Snowball'], ['289', 'I\x92m cold'], ['290', 'Grilled Chestnut'], ['291', 'Chaussette'], ['292', 'Souris Sapin'], ['293', 'Cookies Eater'], ['210', 'Alimli Fare'], ['211', 'Bastan \xc7ikaran'], ['212', 'Latin Asik'], ['249', 'Omelettovore'], ['250', 'My Cutie Pie'], ['251', 'Fianc\xe9e'], ['294', 'I Cheese You']]
###Special Titles###
titlelist.append(["777","<font color='#EB1D51'>Uchiha Itachi</font>"])
titlelist
def getTitle(isim,titles):
    f=True
    for t in titles:
        if t[0]==isim:
            to=t[1]
            for tl in titlelist:
                if tl[0]==str(to):
                    f=False
                    return tl[1]
                    break
    if f:
        print f
        return "Minik Fare"
def getDbTitle(isim):
    Cursor.execute('select currenttitle from users where name = ?', [isim])
    rrf = Cursor.fetchone()
    if rrf is None:
        return "0"
    else:
        return str(rrf[0])
def checkTitle(isim,titles):
    f=True
    for t in titles:
        if t[0]==isim:
            f=False
            return titles
            break
    titles.append([isim,getDbTitle(isim)])
    if f:return titles

