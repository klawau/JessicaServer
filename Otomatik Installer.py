# -*- coding: utf-8 -*-
import sqlite3

dbcon = sqlite3.connect("./dbfile.sqlite")
dbcon.isolation_level = None
dbcur = dbcon.cursor()
dbcon.row_factory = sqlite3.Row
dbcon.text_factory = str
try:
    print "Yorum Tablosu Kuruluyor..."
    dbcur.execute("""CREATE TABLE IF NOT EXISTS `forum_comments` (
      `forum_id` INTEGER NOT NULL,
      `thread_id` INTEGER NOT NULL,
      `message_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `username` text NOT NULL,
      `title` text NOT NULL,
      `message` text NOT NULL,
      `time` int(11) NOT NULL,
      `deleted` tinyint(1) NOT NULL,
      `nomModerateur` text NOT NULL,
      `reason` text NOT NULL);""")
    print "Yorum Tablosu Kuruldu."
    print "Yorum Tablosu Verileri Aktariliyor..."
    dbcur.execute("""INSERT INTO `forum_comments` (`forum_id`, `thread_id`, `message_id`, `username`, `title`, `message`, `time`, `deleted`, `nomModerateur`, `reason`) VALUES(1, 1, 1, 'Ghost', 'New forum!', 'Forumumuza Hoşgeldiniz.', 1367768799, 0, '', '');""")
    dbcur.execute("""INSERT INTO `forum_comments` (`forum_id`, `thread_id`, `message_id`, `username`, `title`, `message`, `time`, `deleted`, `nomModerateur`, `reason`) VALUES(611, 2, 2, 'Hakan', 'Transformice Forums', 'Yakında En İyi Forum Olacağız', 1367842538, 0, '', '');""")
    dbcur.execute("""INSERT INTO `forum_comments` (`forum_id`, `thread_id`, `message_id`, `username`, `title`, `message`, `time`, `deleted`, `nomModerateur`, `reason`) VALUES(611, 2, 3, 'Ghost', ' ', '[quote=Testvip]Yakında En İyi Forum Olacağız[/quote]Evet!', 1367842729, 0, '', '');""")
    print "Yorum Tablosu Verileri Aktarildi."
    print "Forum Tablosu Kuruluyor..."
    dbcur.execute("""CREATE TABLE IF NOT EXISTS `forum_forums` (
      `lang` text NOT NULL,
      `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `icon` INTEGER NOT NULL
    );
    """)
    print "Forum Tablosu Kuruldu."
    print "Forum Tablosu Verileri Aktariliyor..."
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('xx', 1, 1);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 601, 2);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 602, 3);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 603, 4);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 604, 5);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 605, 6);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 606, 7);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 607, 8);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 608, 3);""")
    dbcur.execute("""INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 611, 3);""")
    print "Forum Tablosu Verileri Aktarildi."
    print "Moderator Tablosu Kuruluyor..."
    dbcur.execute("""
    CREATE TABLE IF NOT EXISTS `forum_moderation` (
      `forum_id` int(11) NOT NULL,
      `thread_id` int(11) NOT NULL,
      `message_id` int(11) NOT NULL,
      `type_modere` int(11) NOT NULL,
      `comment` text NOT NULL
    );""")
    print "Moderator Tablosu Kuruldu."
    print "Konu Tablosu Kuruluyor..."
    dbcur.execute("""
    CREATE TABLE IF NOT EXISTS `forum_threads` (
      `forum_id` int(11) NOT NULL,
      `thread_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `topic` text NOT NULL,
      `date` int(14) NOT NULL,
      `author` text NOT NULL,
      `last_poster` text NOT NULL,
      `sticky` tinyint(1) NOT NULL,
      `closed` tinyint(1) NOT NULL
    );""")
    print "Konu Tablosu Kuruldu."
    print "Konu Tablosu Verileri Aktariliyor..."
    dbcur.execute("""INSERT INTO `forum_threads` (`forum_id`, `thread_id`, `topic`, `date`, `author`, `last_poster`, `sticky`, `closed`) VALUES(1, 1, 'Yeni Forum | New Forum', 1367768799, 'Ghost', 'Devsaider', 1, 1);""")
    dbcur.execute("""INSERT INTO `forum_threads` (`forum_id`, `thread_id`, `topic`, `date`, `author`, `last_poster`, `sticky`, `closed`) VALUES(611, 2, 'Transformice Forumları', 1367842538, 'Testvip', 'Testvip', 0, 1);""")
    print "Konu Tablosu Verileri Aktarildi."
except:
    pass
dbcur.execute("DELETE FROM forum_forums")
print "Forum Tablosu Verileri[2] Aktariliyor..."
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 501, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 502, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 503, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 504, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 505, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 506, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 507, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 508, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('fr', 511, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 521, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 522, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 523, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 524, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 525, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 526, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 527, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 528, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('en', 531, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 541, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 542, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 543, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 544, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 545, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 546, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 547, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 548, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('br', 551, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 561, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 562, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 563, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 564, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 565, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 566, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 567, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 568, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('es', 571, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 581, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 582, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 583, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 584, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 585, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 586, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 587, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 588, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('tr', 591, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 601, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 602, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 603, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 604, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 605, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 606, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 607, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 608, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ru', 611, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 621, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 622, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 623, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 624, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 625, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 626, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 627, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 628, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('pl', 631, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 641, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 642, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 643, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 644, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 645, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 646, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 647, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 648, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('no', 651, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 661, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 662, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 663, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 664, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 665, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 666, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 667, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 668, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('hu', 671, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 681, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 682, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 683, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 684, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 685, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 686, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 687, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 688, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('cn', 691, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 701, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 702, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 703, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 704, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 705, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 706, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 707, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 708, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('nl', 711, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 721, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 722, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 723, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 724, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 725, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 726, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 727, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 728, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('ro', 731, 3);")

####### NoVa Language Code Creator #######
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 741, 2);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 742, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 743, 4);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 744, 5);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 745, 6);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 746, 7);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 747, 8);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 748, 3);")
dbcur.execute("INSERT INTO `forum_forums` (`lang`, `id`, `icon`) VALUES('id', 751, 3);")
print "Forum Tablosu Verileri[2] Aktarildi."
print "Sentinel Tablosu Kuruluyor..."
dbcur.execute("""
    CREATE TABLE IF NOT EXISTS forum_sentinel ( 
    isim TEXT );""")
print "Sentinel Tablosu Kuruldu."
print "Log Tablosu Kuruluyor..."
dbcur.execute("""CREATE TABLE IF NOT EXISTS forum_log ( 
    isim     TEXT,
    forum_no TEXT,
    konu_no  TEXT,
    yorum_no TEXT,
    log);""")
print "Log Tablosu Kuruldu."
import time
print "#NoVaLIB/Python/Flash-Forum[Sqlite3]"
print "We Are Dev-TR"
print "#NoVaLIB Developers DevelopetDesign&SevenOPS[HacqerNoVa]"
time.sleep(30)
