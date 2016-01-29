from twisted.internet import protocol
from twisted.internet import reactor
import antlr4
from gen.MySQLLexer import MySQLLexer
from gen.MySQLParser import MySQLParser


class Handler:

    inErrorRecoveryMode = False

    def reportError(self, error):
        pass

    def recover(self, error):
        pass

    def recoverInline(self, error):
        pass

    def reportMatch(self, parser):

        if self.test == 0:
            print "select"
        elif self.test == 1:
            print "insert"
        elif self.test == 2:
            print "delete"
        elif self.test == 3:
            print "alter"
        print self.text

class MyPP(protocol.ProcessProtocol):

    def connectionMade(self):
        self.transport.closeStdin()

    def outReceived(self, data):
        lines = [l.strip() for l in data.splitlines()]

        for line in lines:
            s = antlr4.InputStream(line)
            l = MySQLLexer(s)
            tokens = antlr4.CommonTokenStream(l)
            p = MySQLParser(tokens)
            p._errHandler = Handler()

            try:
                p._errHandler.test = 0
                p._errHandler.text = line
                p.select_clause()
            except Exception as e:
                pass

            try:
                p._errHandler.test = 1
                p._errHandler.text = line
                p.insert_stm()
            except:
                pass

    def errReceived(self, data):
        pass

    def inConnectionLost(self):
        pass

    def outConnectionLost(self):
        pass

    def errConnectionLost(self):
        pass

    def processExited(self, reason):
        pass

    def processEnded(self, reason):
        reactor.stop()

pp = MyPP()
reactor.spawnProcess(pp, "python", args=["python", "test.py"])
reactor.run()