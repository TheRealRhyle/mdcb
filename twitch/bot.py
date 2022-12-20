import socket
import json
from urllib import request
import time
import os
import configparser

# config = configparser.ConfigParser()
# config.read('config.cfg')

class ChanBot():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        config.sections()
        self.channels = []
        self.listenChannel = config['DEFAULT']['listenChannel']
        self.host = config['DEFAULT']['host']
        self.nick = config['DEFAULT']['nick']
        self.port = config['DEFAULT']['port']
        self.oauth = config['KEYS']['oauth']
        self.ClientID = config['KEYS']['ClientID']
        self.Token = config['KEYS']['Token']
        self.s = socket.socket()
        self.s.connect((self.host, int(self.port)))
        self.s.send(bytes('PASS %s\r\n' % self.oauth, 'UTF-8'))
        self.s.send(bytes('NICK %s\r\n' % self.nick, 'UTF-8'))
        self.s.send(bytes('CAP REQ :twitch.tv/membership\r\n', 'UTF-8'))
        self.s.send(bytes('CAP REQ :twitch.tv/tags\r\n', 'UTF-8'))
        self.s.send(bytes('CAP REQ :twitch.tv/commands\r\n', 'UTF-8'))

    def disconnect(self):
        self.s.close()
    
    def joinChannel(self, channel):
        self.s.send(bytes("JOIN #" + channel + "\r\n", 'UTF-8'))
        self.channels.append(channel)

    def partChannel(self, channel):
        self.s.send(bytes("PART #" + channel + "\r\n", 'UTF-8'))
        self.channels.remove(channel)
    
    def sendChannelMessage(self, channel, message):
        self.s.send((f"PRIVMSG #{channel} : {message} \r\n").encode('UTF-8'))
    
    def readChatMessage(self):
        readbuffer = self.s.recv(1024).decode("UTF-8")
        temp = str(readbuffer).split("\n")
        readbuffer = temp.pop()
        for line in temp:
            if ("PING :" in line):
                self.s.send(bytes("PONG\r\n", "utf-8"))
            return line
    
    def processCommands(self, line):
        if line.startswith("!"):
            print("this was a command")
        

if  __name__=="__main__":
    os.system('cls')
    rbot = ChanBot()
    rbot.joinChannel(rbot.listenChannel)
    
    while True:
        time.sleep(1)
        x= rbot.readChatMessage()
        rbot.processCommands(x)
        
        # with open('chatlog.txt', 'a' , encoding="utf-8") as cl:
        #     cl.writelines(x)
        
        # channel, user, message = rbot.readChatMessage()
        print(x)
        # get actual message

        
        message = x.split(":")[-1].strip("!s ")
        if "!join" in x:
            newchan = x.split(" ")[-1]
            rbot.joinChannel(newchan)
            # rbot.sendChannelMessage(newchan, "I am here as requested, feel free to ignore me. also... POTATO")
        if '!s' in x and 'display-name=Rhyle_' in x:
            rbot.sendChannelMessage('13thfaerie', message)
        # if "!part" in x:
        #     newchan = x.split(" ")[-1]
        #     rbot.sendChannelMessage(newchan, 'Banished again....')
        #     rbot.partChannel(newchan)
