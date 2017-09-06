# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ByteArray
# Purpose:     This is part of Jessica server.
#
# Author:      Flyer ( Exfler )
#
# Created:     12.2012
# Copyright:   (c) Flyer 2012
#-------------------------------------------------------------------------------
import struct

class ByteArray:
    def __init__(self, bytes=''):
        self.bytesString = bytes

    def writeBoolean(self, value=1):
        self.bytesString += self.writeByte(value, False)

    def writeByte(self, value, noReturning=True):
        if noReturning: self.bytesString += struct.pack('!b', value)
        else: return struct.pack('!b', value)

    def writeBytes(self, value):
        self.bytesString += value

    def writeInt(self, value):
        self.bytesString += struct.pack('!l', value)

    def writeShort(self, value):
        self.bytesString += struct.pack('!h', value)
    ###Kabile Forumları İçin 1 Temmuz 2013 Tarihinde hαcφεƦπøυα™ Tarafından Güncellenmiştir### 
    def writeUTF(self, value, tribu=False):
        if tribu:
            valueSize = len(value)
            self.writeByte(valueSize)
            self.writeUTFBytes(value)
        else:
            valueSize = len(value)
            self.writeShort(valueSize)
            self.writeUTFBytes(value)

    def writeUTFBytes(self, value):
        self.bytesString += value

    def length(self):
        return len(self.bytesString)

    def toString(self):
        return self.bytesString

    def toPack(self):
        return struct.pack('!l', len(self.bytesString)+4)+self.bytesString

    def getSize(self, Pos):
        return struct.unpack('!l', self.bytesString[:4])[0]

    def readBy(self, Pos):
        self.bytesString = self.bytesString[Pos:]
        return self.bytesString

    def loc(self, byte):
        loc = self.bytesString[:byte]
        self.bytesString = self.bytesString[byte:]
        return struct.unpack('!b', loc)[0]

    def readInt(self):
        size = struct.unpack('!l', self.bytesString[:4])[0]
        self.bytesString = self.bytesString[4:]
        return size

    def readUTF(self):
        size = struct.unpack('!h', self.bytesString[:2])[0]
        string = self.bytesString[2:2 + size]
        self.bytesString = self.bytesString[size + 2:]
        return string.replace("'","")

    def readLongString(self):
        size = struct.unpack('!l', self.bytesString[:4])[0]
        string = self.bytesString[4:4 + size]
        self.bytesString = self.bytesString[size + 4:]
        return string.replace("'","")

    def readShort(self):
        size = struct.unpack('!h', self.bytesString[:2])[0]
        self.bytesString = self.bytesString[2:]
        return size

    def readBoolean(self):
        loc = struct.unpack('!b', self.bytesString[:1])[0]
        self.bytesString = self.bytesString[1:]
        if loc == 1: return True
        else: return False

    def readByte(self):
        size = struct.unpack('!b', self.bytesString[:1])[0]
        self.bytesString = self.bytesString[1:]
        return size

    def readList(self, size):
        list = list(self.bytesString[:size])
        self.bytesString = self.bytesString[size:]
        return list

    def readUTFBytes(self, size):
        string = self.bytesString[:size]
        self.bytesString = self.bytesString[size:]
        return string
