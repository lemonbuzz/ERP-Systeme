import Pyro4

class ServerCommunication():
    def __init__(self):
        #self.serverAdress = "PYRO:foo@localhost:48261"
        self.serverAdress = "PYRO:foo@10.57.47.25:48261"
        self.status = None
        self.server = None
        
    def connectToServer(self):
        self.server = Pyro4.Proxy(self.serverAdress)
        
<<<<<<< HEAD
    """def runSQLQuery(self,SQLquery, bindings = None):
        return self.server.executeSql(SQLquery)"""
    
    def runSQLQuery(self,SQLquery):
        return self.server.executeSql(SQLquery)
=======
    def runSQLQuery(self,SQLquery, bindings = None):
        return self.server.executeSql(SQLquery,bindings)
>>>>>>> e8c5d103319d2eeca3ad9fd51e1c3fb091078e43
        
    def logIn(self,user,password):
        if user.strip()== "" or password.strip() == "":
            return False
        else:
            message= self.server.loginValidation(user,password)
            print(message)
            return message
