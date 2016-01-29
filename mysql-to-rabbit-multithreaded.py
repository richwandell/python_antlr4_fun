import antlr4
from gen.MySQLLexer import MySQLLexer
from gen.MySQLParser import MySQLParser
from threading import Thread
from subprocess import PIPE, Popen


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

if __name__ == "__main__":

    def process(data):
        s = antlr4.InputStream(data)
        l = MySQLLexer(s)
        tokens = antlr4.CommonTokenStream(l)
        p = MySQLParser(tokens)
        p._errHandler = Handler()

        try:
            p._errHandler.test = 0
            p._errHandler.text = data
            p.select_clause()
        except Exception as e:
            pass

        try:
            p._errHandler.test = 1
            p._errHandler.text = data
            p.insert_stm()
        except:
            pass


    p = Popen(["python", "test.py"], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        if line != '':
            Thread(target=process, args=(line.strip(),)).start()
        else:
            break