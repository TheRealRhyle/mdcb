import configparser
import psycopg2
import datetime

class Database():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        self.host = config['PostgreSQL']['host']
        self.database = config['PostgreSQL']['database']
        self.user=config['PostgreSQL']['user']
        self.password=config['PostgreSQL']['password']
        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        self.c = self.conn.cursor()
        
    def createChannelTable(self, channel):
        # Gets called when someone uses the !join <channel command>
        query = f"CREATE TABLE IF NOT EXISTS public.stream_{channel}"
        query = query + """
        (
            id SERIAL PRIMARY KEY,
            username text NOT NULL,
            status text NOT NULL
        )"""
        q2 = f"INSERT INTO streams (streamname, \"joinedOn\") VALUES('{channel}', (SELECT NOW()))"
        self.c.execute(query)
        try:
            self.c.execute(q2)
        except:
            print(f'Stream named {channel} already in the list.')
        self.conn.commit()
        
    def readTable(self, table):
        self.c.execute(f"SELECT * from {table};")
        table_data = self.c.fetchall()
        return table_data
    
    def insertChannelData(self, channel, data):
        query = f"INSERT INTO stream_{channel} (username, status) VALUES {data}"
        self.c.execute(query)
        self.conn.commit()
        
    def updateTable(self, table, data):
        pass
    
    def deleteTable(self, table):
        pass
    

if __name__ == "__main__":
    test = Database()
    print(test.readTable("quotes"))
    # test.createChannelTable("rhyle_")
    # test.insertChannelData("rhyle_", ("rhyle_", "broadcaster"))
    test.insertChannelData("rhyle_",("13thfaerie","mod"))
    
    # config = configparser.ConfigParser()
    # config.read('config.cfg')
    # conn = psycopg2.connect(host=config['PostgreSQL']['host'], database=config['PostgreSQL']['database'], user=config['PostgreSQL']['user'], password=config['PostgreSQL']['password'])
    # c = conn.cursor()
    # quotes = c.execute("SELECT * from quotes;")
    # quotes = c.fetchall()
    
    # print(quotes)
    
    