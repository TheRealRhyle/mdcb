import configparser, os, socket, sys, time

sys.path.insert(0, os.getcwd())
print('\n'.join(sys.path))

from utils.pgres import Database as db
class ChanBot():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        config.sections()
        # get list of channels to join from the DB
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
        x= db()
        x.createChannelTable(channel)

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
        chatline=rbot.readChatMessage()
        # rbot.processCommands(chatline)
        
        # channel, user, message = rbot.readChatMessage()
        # @badge-info=subscriber/53;badges=broadcaster/1,subscriber/0,premium/1;client-nonce=96beb9f89ee721c007f0e53aa35b81f2;color=#8A2BE2;display-name=Rhyle_;emotes=;first-msg=0;flags=;id=efbcc93d-8211-4f77-8b45-215e34198c1b;mod=0;returning-chatter=0;room-id=38847203;subscriber=1;tmi-sent-ts=1671592517126;turbo=0;user-id=38847203;user-type= :rhyle_!rhyle_@rhyle_.tmi.twitch.tv PRIVMSG #rhyle_ :test
        if chatline.startswith("@badge-info") and 'USERSTATE' not in chatline:
            pinfo = chatline.split("user-id=")[1]
            uid, p2info = pinfo.split(";")
            username = p2info.split(":")[1].split('!')[0]
            channel, message = p2info.split("PRIVMSG ")[1].split(" :")
            print(f'uid: {uid}\tusername: {username}\tchannel: {channel}\tmessage: {message}')
        
        if chatline.startswith("@badge-info") and "!join me" in message:
            rbot.joinChannel(username)
            rbot.sendChannelMessage(username, "I am here as requested, feel free to ignore me. also... POTATO!")
        
        if chatline.startswith("@badge-info") and '!s' in message and username == 'rhyle_':
            channel = message.split(" ", 2)[1]
            rbot.sendChannelMessage(channel, message.split(" ", 2)[-1])
        
        # if "!part" in x:
        #     newchan = x.split(" ")[-1]
        #     rbot.sendChannelMessage(newchan, 'Banished again....')
        #     rbot.partChannel(newchan)
