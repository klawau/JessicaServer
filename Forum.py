# -*- coding: utf_8 -*-
#-------------------------------------------------------------------------------
# Name:        Transformice Forums Start Module
# Purpose:     Jessica server.
#
# Author:      Spaowi ( Devsaider )
# Debug:       SevenOPS(hαcφεƦπøυα™)
# BugFinder:      TheVon
# Created:     01-07-2013
# Copyright:   (c) Dev-TR 2013
#-------------------------------------------------------------------------------
#print repr(ord("("))
import hashlib
import sqlite3
import threading
import random
import StringIO
import sys
import time
from ByteArray import ByteArray
from PIL import Image
import urllib2
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

#import upload
import saat
om = []
update = False
dbcon = sqlite3.connect("./dbfile.sqlite")
dbcon.isolation_level = None
dbcur = dbcon.cursor()
dbcon.row_factory = sqlite3.Row
dbcon.text_factory = str                            
V = "0.1rc4b12"
class TransformiceForums(Protocol):
    def __init__(self, factory):
        self.client = Protocol
        self.factory = factory
        self.forum_id = -1
        self.page = 0
        self.priv = 1
        self.pf = ["10", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "44"]
        self.langue = "br"
        self.thread_id = 0
        self.username = ""
        self.userTypeNeededForPeutModerer = [11, 17, 18, 14, 20]
        self.user_type = 19
        self.version = 13
        self.sentinel = False
        self.sf = []
        self.login = False
        self.ms = 0
        self.versionValidated = False
		
    def connectionMade(self):
        print "Connected", self.transport.getHandle().getpeername()[0]

    def connectionLost(self, reason):
        try:
            nlol.online.remove(self.username)
        except:
            pass

    def RequireLevel(self, levels):
        cant = self.user_type in levels
        if cant:return True
        else:raise Exception('spam', 'eggs')

    def getJoueurType(self, username):
        privilegesForum = {1:(19, ""), 2:(19, ""), 3:(12, ""), 4:(17, "<CJ>"), 5:(17, "<CJ>"), 6:(17, "<CJ>"), 8:(17, "<CJ>"), 9:(18, "<CJ>"), 10:(14, "<CR>"), 11:(20, "<CR>")}
        CheckFail=0
        if len(username)>12:
            self.transport.loseConnection()
            CheckFail=1

        if not username.isalpha():
            self.transport.loseConnection()
            CheckFail=1

        if CheckFail==0:
            username=username.lower()
            username=username.capitalize()
            dbcur.execute('select * from users where name = ?', [username])
            rrf = dbcur.fetchone()
            
            if rrf is None:
                return 0
            else:
                name = rrf[0]
                privlevel = rrf[3]
                return privilegesForum[privlevel][0]
        else:
            pass

    def debug(self, nom):
        pass

    def authenticate(self, username, passwordHash):
        CheckFail=0
        if len(username)>12:
            self.transport.loseConnection()
            CheckFail=1

        if not username.isalpha():
            self.transport.loseConnection()
            CheckFail=1

        if CheckFail==0:
            username=username.lower()
            username=username.capitalize()
            dbcur.execute('select * from users where name = ?', [username])
            rrf = dbcur.fetchone()
            
            if rrf is None:
                return 0, -1, ""
            else:
                name = rrf[0]
                password = rrf[1]
                privlevel = rrf[3]
                self.priv = privlevel
                if passwordHash != password:
                    return 0, -1, name
                    
                else:
                    return 1, self.getJoueurType(name), name
        else:
            pass

    def ForumsList(self):
        p = ByteArray("\x02\x02")
        p.writeUTF(self.langue)
        dbcur.execute("SELECT * FROM forum_forums where id < 1000")
        threads = dbcur.fetchall()
        for thread in threads:
            if str(thread[1]) in self.pf and self.priv < 4:
                
                pass
            else:
                p.writeInt(int(thread[1]))
                p.writeUTF(str(thread[0]))
                p.writeShort(int(thread[2]))
        if self.login:
            dbcur.execute("SELECT tribe FROM users where name = ?", [self.username])
            td = dbcur.fetchone()
            if not td[0] == None:
                tdc = td[0].split("#")[1]
                dbcur.execute("SELECT * FROM tribu where Code = ?", [tdc])
                ntd = dbcur.fetchone()
                p.writeInt(int(tdc)+2000)
                p.writeUTF("xx")
                p.writeShort(9)
                p.writeByte(False)
                p.writeUTF(ntd[1], True)
        
        self.transport.write(p.toPack())

    def message_forum(self, msg):
        p = ByteArray("\x1c\x1c")
        p.writeUTF(msg)
        self.transport.write(p.toPack())

    def online(self):
        p = ByteArray("\x28\x28")
        p.writeInt(len(nlol.online))
        self.transport.write(p.toPack())

    def generateThreadsPage(self, forum_id):
        dbcur.execute("SELECT * FROM forum_threads where forum_id=?", [forum_id])
        comments = dbcur.fetchall()
        return len(comments)/20

    def getcommentsbythread(self, thread_id, forum_id):
        dbcur.execute("SELECT * FROM forum_comments where forum_id=? AND thread_id=?", [forum_id, thread_id])
        comments = dbcur.fetchall()
        return comments

    def openForums(self, forum_id, page):
        if page == -1:page=0
        self.forum_id = forum_id
        if page != 0:limit1, limit2 = page*20, page*40
        else:limit1, limit2 = 0, 20

        p = ByteArray("\x02\x04")
        if forum_id == 1:
            openthread = self.user_type in [17, 18, 14, 20]
        else:
            openthread = True
        if self.username in om:
            openthread = False
        if not self.login:
            openthread = False
        p.writeBoolean(openthread) # peutCreerSujet

        # [FORUM INFO] #

        
        ###Tribe Forums###
        if forum_id > 2000:
            dbcur.execute("SELECT * FROM forum_forums where id = ?", [int(forum_id)])
            td = dbcur.fetchone()
            if not td == None:
                pass
            else:
                dbcur.execute("INSERT INTO forum_forums VALUES (?,?,?)", ["xx", (forum_id), "9"])
            dbcur.execute("SELECT * FROM tribu where Code = ?", [int(forum_id)-2000])
            ntd = dbcur.fetchone()
            p.writeInt(forum_id)
            p.writeUTF("xx")
            p.writeShort(9)
            p.writeByte(False)
            p.writeUTF(ntd[1], True)
            dbcur.execute("SELECT * FROM forum_forums where id=?", [forum_id])
            forum = dbcur.fetchone()
        else:
            dbcur.execute("SELECT * FROM forum_forums where id=?", [forum_id])
            forum = dbcur.fetchone()
            p.writeInt(int(forum[1])) # forumId
            p.writeUTF(str(forum[0])) # forumCountry
            p.writeShort(int(forum[2])) # forumIcon
        p.writeInt(page) # pageCurrent
        p.writeInt(self.generateThreadsPage(forum_id)+1) # pageTotal
        #
        p.writeBoolean(False) # masquerSujetCourrant # публичный форум : boolean

        dbcur.execute("SELECT * FROM forum_threads where forum_id=? ORDER BY sticky DESC, date DESC LIMIT ?, ?", [forum_id, limit1, limit2])
        threads = dbcur.fetchall()
        threadNum = 0
        for row in threads:
            z = row[1]
            # [InfoServeurSujet] #
            dbcur.execute("SELECT * FROM forum_comments where thread_id=? ORDER BY time DESC", [z])
            topicLastMessage = dbcur.fetchall()[0]
            p.writeInt(row[1]) # code
            p.writeUTF(row[2]) # titre
            p.writeInt(int(row[3])) # date
            p.writeUTF(row[4].encode("cp1251")) # auteur
            p.writeByte(self.getJoueurType(row[4].encode("cp1251"))) # typeAuteur
            p.writeUTF(topicLastMessage[3].encode("cp1251")) # last_posteur
            p.writeInt(len(self.getcommentsbythread(row[1], forum[1]))) # numMessage
            typeThread = 0
            if bool(row[7]):typeThread = 2
            p.writeByte(typeThread) # type
            p.writeBoolean(bool(row[6])) # postIt
            p.writeInt(threadNum) # nombreSignalements
            threadNum+=1
        self.transport.write(p.toPack())
    def mc(self):
        dbcur.execute('select * from forum_mute where isim = ?', [self.username])
        rrf = dbcur.fetchone()
        if not rrf is None:
            sd = saat.saat(rrf[7])
            if int(sd.split("NoVa")[0]) < int(rrf[8]) or str(rrf[8]) == "-1":
                if str(rrf[8]) == "-1":
                    self.message_forum("You have unlimited mute :/")
                else:
                    self.ms = sd.split("NoVa")[0]
                    self.ms = int(rrf[8])-int(self.ms)
                        
                    if int(rrf[8]) == 1:
                        self.ms = 0
                        self.message_forum("Mutenizin bitmesine "+str(self.ms)+" saat "+str(60-int(sd.split("NoVa")[1]))+" dakika kaldı.")
                om.append(self.username)
            else:
                if self.username in om:
                    om.remove(self.username)
                dbcur.execute("DELETE FROM forum_mute where isim = ?", [self.username])
                self.message_forum("Mute'niz kaldırılmıştır.")
                
    def openThread(self, thread_id, page):
        if page == -1:page=0
        if page != 0:limit1, limit2 = (page*20)-1, page*40
        else:limit1, limit2 = 0, 20
        dbcur.execute("SELECT * FROM forum_threads where thread_id = ?", [thread_id])
        topicData = dbcur.fetchone()
        dbcur.execute("SELECT * FROM forum_comments where thread_id = ? ORDER BY time  LIMIT ?, ?;", [thread_id, limit1, limit2])
        topicStartMessage = dbcur.fetchall()[0]
        forum_id = topicData[0]
        self.forum_id = forum_id
        self.thread_id = thread_id

        p = ByteArray("\x02\x05")
        # [FORUM INFO] #
        p.writeInt(forum_id) # forumEnCours
        p.writeInt(thread_id) # sujetEnCours
        canEdit = self.user_type in self.userTypeNeededForPeutModerer
        if canEdit: canEdit=10
        elif self.username==topicStartMessage[3]:canEdit=1
        p.writeByte(canEdit) # edition
        p.writeBoolean(self.user_type != 19) # peutSuppr
        peutReponder = self.username != ""
        if bool(topicData[7]): peutReponder = False
        if not self.login:openthread = False
        if self.username in om:peutReponder = False
        p.writeBoolean(peutReponder) # peutRepondre
        p.writeBoolean(bool(topicData[7])) # fin
        p.writeBoolean(self.user_type != 19) # modTribu
        p.writeUTF(topicData[2]) # titre
        p.writeInt(page) # pageEnCours
        p.writeInt(int(len(self.getcommentsbythread(thread_id, forum_id))/20)) # nobrePage
        dbcur.execute("SELECT * FROM forum_comments where thread_id = ? ORDER BY time LIMIT ?, ?", [thread_id, limit1, limit2])
        messages = dbcur.fetchall()
        p.writeByte(len(messages)-1) # message        
        for message in messages:
            p.writeInt(message[2]) # id
            p.writeByte(self.getJoueurType(message[3].encode("cp1251"))) # typeAuteurMessage
            p.writeUTF(message[3]) # auteur
            p.writeByte(self.getJoueurType(message[3].encode("cp1251"))) # typeAuteurCourant
            p.writeInt(10000) # avatar
            p.writeInt(message[6]) # date
            p.writeUTF(message[5]) # texte
            p.writeByte(message[7]) # etat
            p.writeUTF(message[8].encode('utf-8','replace')) # nomModerateur
            p.writeUTF(message[9].encode('utf-8','replace')) # raisonEtat
            p.writeUTF("") # infos
            p.writeBoolean(True) # multiLangues
            p.writeBoolean(False) # etatSignalement
            #p.writeUTF("TEST Title")
        self.transport.write(p.toPack())

    def dataReceived(self, data):      # 446, 44442, 5557, 3726, 6114
        print data
        if data == "<policy-file-request/>\x00":self.transport.write("""<cross-domain-policy><allow-access-from domain="127.0.0.1" to-ports="443,44444,44440,5555,3724,6112" /></cross-domain-policy>\x00""")
                            
        else:
   
            opcode1 = data[4:5]
            opcode2 = data[5:6]
            opcodes = bytes([opcode1, opcode2])
            data = data[6:len(data)]
            print repr(opcodes)
            
            if opcode1 == "\x1c":
                
                if opcode2 == "\x01":
                    #Version
                    p = ByteArray(data)
                    v = p.readInt()
                    print v
                    if v == self.version:
                        #ForaList
                        self.versionValidated = True
                        self.online()
                        self.ForumsList()
                    else:self.transport.connectionLost()
                elif opcode2 == "\x1c":
                        # Moderating Functions
                        self.RequireLevel(self.userTypeNeededForPeutModerer)
                        p = ByteArray(data)
                        params = p.readUTF().split(",")
                        if params[0] == "[E]renommer_sujet":
                            # Thread Rename
                            thread_id, message_id, new_title = params[1], p.readShort(), p.readUTF()
                            dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, message_id, "Konu İsmi", new_title, "Olarak Değiştirildi."])
                            dbcur.execute("UPDATE forum_threads SET topic = ? WHERE thread_id = ?", [new_title, thread_id])
                            self.openThread(int(thread_id), 0)
                        elif params[0] == "[E]mute":
                            # Kullanıcı susturma
                            mm = int(params[1])
                            ms = int(params[3])
                            mn = str(params[2])
                            fi = int(params[4])
                            ki = int(params[5])
                            mi = int(params[6])
                            p = ByteArray(data.split("\x01")[1])
                            sebep = p.readUTF()
                            if ms == 0:
                                if mn in om:
                                    om.remove(mn)
                                dbcur.execute("DELETE FROM forum_mute where isim = ?", [mn])
                                self.message_forum(mn+" Adlı Kullanıcının Mute'si Kaldırıldı.")
                            else:
                                
                                if mm == 1:
                                    dbcur.execute('select * from forum_mute where isim = ?', [mn])
                                    rrf = dbcur.fetchone()
                                    if rrf is None:
                                        
                                        mod = "isim"
                                        
                                        if mn in nlol.online:
                                            md = "Online"
                                            om.append(mn)
                                        else:
                                            md = "Offline"
                                        self.message_forum(mn+" Adlı Kullanıcı "+str(ms)+" Saat Boyunca Mutelendi.")
                                        dbcur.execute("INSERT INTO forum_mute VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.username, mn, fi, ki, mi, sebep, "ip", time.time(), ms, md])
                                    else:
                                        self.message_forum(rrf[1]+" "+rrf[0]+" Tarafından Mutelenmiş Zaten")
                                else:
                                    self.message_forum("Şimdilik Sadece Oyuncu Mutelenebiliyor ^_^")
                            
                
                        elif params[0] == "deplacer_sujet":
                            # Thread Replace
                            thread_id, forum_id = int(params[1]), int(params[2])
                            dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, "", "Konu "+forum_id+" Forumuna Taşındı."])
                            dbcur.execute("UPDATE forum_threads SET forum_id = ? WHERE thread_id = ?", [forum_id, thread_id])
                            dbcur.execute("UPDATE forum_comments SET forum_id = ? WHERE thread_id = ?", [forum_id, thread_id])
                            
                            self.openForums(forum_id, 0)
                            self.openThread(thread_id, 0)

            elif self.versionValidated:
                print opcode1+" - "+opcode2
				
                if opcode1 == "\x02":
                    if opcode2 == "\x03":
                        # REQUEST_FORUMS_LIST
                        self.online()
                        self.ForumsList()
                    elif opcode2 == "\x04":
                        # REQUEST_THREAD_LIST
                        p = ByteArray(data)
                        forum_id = p.readInt()
                        page = p.readInt()
                        self.forum_id = forum_id
                        self.openForums(forum_id, page)
                    elif opcode2 == "\x05":
                        print "rophl"
                        # REQUEST_MESSAGE_LIST
                        p = ByteArray(data)
                        thread_id = p.readInt()
                        page = p.readShort()
                        self.page = page
                        self.thread_id = thread_id
                        self.openThread(thread_id, page)


                elif opcode1 == "\x04":
                    if opcode2 == "\x02":
                        # New Thread
                        p = ByteArray(data)
                        forum_id = p.readInt()
                        self.forum_id = forum_id
                        if self.forum_id == 1:
                            self.RequireLevel(self.userTypeNeededForPeutModerer)
                        threadTitle = str(p.readUTF()).decode('utf-8','replace')
                        message_utf = str(p.readLongString()).decode('utf-8','replace')
                        dbcur.execute("INSERT INTO forum_threads VALUES (?, NULL, ?, ?, ?, ?, 0, 0)", [int(forum_id), threadTitle, str(time.time()).replace('.', '')[:10], self.username, self.username])
                        thread_id = dbcur.lastrowid
                        self.thread_id = thread_id
                        dbcur.execute("INSERT INTO forum_comments VALUES (?, ?, NULL, ?, ?, ?, ?, 0, '', '')", [int(forum_id), thread_id, self.username, threadTitle, message_utf, str(time.time()).replace('.', '')[:10]])
                        self.openForums(self.forum_id, 0)
                        self.openThread(thread_id, 0)
                        
                    elif opcode2 == "\x04":
                        # Repondre Sujet
                        p = ByteArray(data)
                        thread_id = p.readInt()
                        message_utf = str(p.readLongString()).decode('utf-8','replace')
                        dbcur.execute("INSERT INTO forum_comments VALUES (?, ?, NULL, ?, ' ', ?, ?, 0, '', '')", [self.forum_id, thread_id, self.username, message_utf, str(time.time()).replace('.', '')[:10]])
                        
                        self.openThread(thread_id, 0)
                    elif opcode2 == "\x06":
                        # Message Edit
                        # needed edit for long string
                        self.RequireLevel(self.userTypeNeededForPeutModerer)
                        
                        p = ByteArray(data)
                        thread_id = p.readInt()
                        message_id = p.readInt()
                        message_utf = str(p.readLongString()).decode('utf-8','replace')
                        dbcur.execute("SELECT * FROM forum_comments WHERE thread_id = ? AND message_id = ? AND username = ?", [thread_id, message_id, self.username])
                        if len(dbcur.fetchall()) == 0:
                            self.RequireLevel(self.userTypeNeededForPeutModerer)
                        dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, message_id, message_utf])
                        dbcur.execute("UPDATE forum_comments SET message = ? WHERE thread_id = ? AND message_id = ?;", [message_utf, thread_id, message_id])
                        
                        self.openThread(thread_id, 0)
                elif opcode1 == "\x28":
                    if opcode2 == "\x02":
                        # Auth
                        p = ByteArray(data)
                        username, passwordHash = p.readUTF(), p.readUTF()
                        p = ByteArray("\x28\x02")
                        #print passwordHash
                        valid, forumPriv, validUsername = self.authenticate(username, hashlib.sha512(passwordHash).hexdigest())
                        p.writeByte(valid)
                        if valid != 0:
                            username=username.lower()
                            username=username.capitalize()
                            dbcur.execute("SELECT isim FROM forum_sentinel WHERE isim = ?", [username])
                            sd = dbcur.fetchone()
                            try:
                                za = sd[0]
                                self.sentinel = True
                                forumPriv = 11
                            except:
                                pass
                            self.username = str(validUsername)
                            self.user_type = forumPriv
                            p.writeUTF(self.username)
                            p.writeInt(10000)
                            p.writeInt(forumPriv)
                            nlol.online.append(self.username)
                            self.login = True
                            self.mc()#Mute Controller
                        self.transport.write(p.toPack())
                        self.online()
                    
                    elif opcode2 == "\x16":
                        p = ByteArray(data)
                        ri, fa, fi, ti, ci, rml = p.readUTF(), p.readUTF(), p.readInt(), p.readInt(), p.readInt(), p.readUTF()
                        print ri, fa, fi, ti, ci, rml
                        self.message_forum("Raporlama Sistemi Daha Hazır Değil ^_^")
                        #### Bu Kod Rapor Kodudur Ancak Daha Bitmemiştir.####
                    elif opcode2 == "\n":
                      
                        file = open("avatars/"+self.username+".png", 'wb')
                        file.write(data)
                        
                        file = open("avatars/"+self.username+".png", 'rb')
                        img = Image.open(file)
                        img.load()
                        img.thumbnail((100, 100), Image.ANTIALIAS)
                        img.save("./avatars/"+self.username+"_Resize.png")

                        data=open("avatars/"+self.username+"_Resize.png", "rb")
                        upload.upload_file(self.username+".png",data)
                        
                        
                    elif opcode2 == "\x0a":
                        # Avatar Change
                        try:
                            pass
##                            file = open("avatars/"+self.username+".png", 'wb')
##                            file.write(data)
##                            basewidth = 100
##                            img = Image.open(StringIO.StringIO(file))
##                            wpercent = (basewidth/float(img.size[0]))
##                            hsize = int((float(img.size[1])*float(wpercent)))
##                            img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
##                            img.save("avatars/"+self.username+".png")
                        except:
                            pass

                    elif opcode2 == "\x0b":
                        # Close Theme
                        if not self.sentinel:
                            self.RequireLevel(self.userTypeNeededForPeutModerer)
                        else:
                            if not str(self.forum_id) in self.sf:
                                self.RequireLevel(self.userTypeNeededForPeutModerer)
                        p = ByteArray(data)
                        thread_id, closed = p.readInt(), p.readBoolean()
                        dbcur.execute("SELECT closed FROM forum_threads where thread_id=?", [thread_id])
                        if int(dbcur.fetchone()[0]) == 0:
                            dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, "", "Konu Kilitlendi."])                        
                            dbcur.execute("UPDATE forum_threads SET closed=1 WHERE thread_id = ?", [thread_id])
                        else:
                            dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, "", "Konu Kilidi Kaldırıldı."])
                            dbcur.execute("UPDATE forum_threads SET closed=0 WHERE thread_id = ?", [thread_id])
                        if closed:
                            dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, "", "Konu Arşive Taşındı."])
                            dbcur.execute("UPDATE forum_threads SET forum_id = ? WHERE thread_id = ?", [611, thread_id])
                            dbcur.execute("UPDATE forum_comments SET forum_id = ? WHERE thread_id = ?", [611, thread_id])
                            self.forum_id = 611
                            
                        
                        self.openForums(self.forum_id, 0)
                        self.openThread(thread_id, 0)

                    elif opcode2 == "\x0c":
                        # Stick Theme
                        if not self.sentinel:
                            self.RequireLevel(self.userTypeNeededForPeutModerer)
                        else:
                            if not str(self.forum_id) in self.sf:
                                self.RequireLevel(self.userTypeNeededForPeutModerer)
                        p = ByteArray(data)
                        thread_id = p.readInt()
                        dbcur.execute("SELECT sticky FROM forum_threads where thread_id=?", [thread_id])
                        if int(dbcur.fetchone()[0]) == 0:
                            dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, "", "Konu Sabitlendi."])
                            dbcur.execute("UPDATE forum_threads SET sticky=1 WHERE thread_id = ?", [thread_id])
                        else:
                            dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, "", "Konu Sabit'ten Çıkarıldı."])
                            dbcur.execute("UPDATE forum_threads SET sticky=0 WHERE thread_id = ?", [thread_id])
                        self.openForums(self.forum_id, 0)
                        self.openThread(thread_id, 0)

                    elif opcode2 == "\x0f":
                        # Moderate theme
                        self.RequireLevel(self.userTypeNeededForPeutModerer)
                        p = ByteArray(data)
                        thread_id = p.readInt()
                        message_id = p.readInt()
                        type_modere = p.readInt()
                        comment = p.readUTF()

                        dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, thread_id, message_id, comment])
                        
                        if type_modere == 0:
                            # Unsupperme Message
                            dbcur.execute("UPDATE forum_comments SET deleted=0, nomModerateur='', reason='' WHERE thread_id = ? AND message_id = ?", [thread_id, message_id])
                            

                        if type_modere == 1:
                            # Supperme Message
                            dbcur.execute("UPDATE forum_comments SET deleted=1, nomModerateur=?, reason=? WHERE thread_id = ? AND message_id = ?", [self.username, comment, thread_id, message_id])
                            

                        if type_modere == 2:
                            # Delete Message
                            dbcur.execute("UPDATE forum_comments SET deleted=2, nomModerateur=?, reason=? WHERE thread_id = ? AND message_id = ?", [self.username, comment, thread_id, message_id])
                            
                        self.openForums(self.forum_id, 0)
                        self.openThread(thread_id, 0)

                    elif opcode2 == "\x10":
                        # Moderer > 1 message
                        self.RequireLevel(self.userTypeNeededForPeutModerer)
                        p = ByteArray(data)
                        username = p.readUTF()
                        type_modere = p.readInt()
                        comment = p.readUTF()
                        dbcur.execute("INSERT INTO forum_log VALUES(?, ?, ?, ?, ?)", [self.username, self.forum_id, "", "", comment])
                        
                        if type_modere == 0:
                            # Unsupperme Message
                            dbcur.execute("UPDATE forum_comments SET deleted=0, nomModerateur='', reason='' WHERE username = ?", [username])
                            

                        if type_modere == 1:
                            # Supperme Message
                            dbcur.execute("UPDATE forum_comments SET deleted=1, nomModerateur=?, reason=? WHERE username = ?", [self.username, comment, username])
                            

                        if type_modere == 2:
                            # Delete Message
                            dbcur.execute("UPDATE forum_comments SET deleted=2, nomModerateur=?, reason=? WHERE username = ?", [self.username, comment, username])
                            

                    elif opcode2 == "\x17":
                        # Sanctions # In progress...
                        self.message_forum("You has no sanctions.")


                    elif opcode2 == "\x28":
                        # Online
                        threading.Timer(15.0, self.online).start()
                        #self.online()
                elif opcode1 == "(":
                    print repr(opcode2)
                    print repr(data)
                else:
                    pass#print repr(data)
            else: self.transport.connectionLost()
            

class MultiEcho(Factory):
    def __init__(self):
        self.echoers = []

    def buildProtocol(self, addr):
        return TransformiceForums(self)

class nlol():
    online = []

if __name__ == "__main__":
  
  
    # Twisted Reactor
    ports = [443,44444,44440,5555,3724,6112] #ports funcionando
    xserver = MultiEcho()
    for port in ports:reactor.listenTCP(port, xserver)
    reactor.callWhenRunning(sys.stdout.write, "*"*80 + "Jessica Server By Dev-TR".center(80) + "*"*80)
    reactor.callWhenRunning(sys.stdout.write, "Reactor Engines Online V0.1RC4".center(80))
    reactor.callWhenRunning(sys.stdout.flush)
    reactor.run()
