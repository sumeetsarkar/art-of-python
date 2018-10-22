class Logging:

    def log(self, *args):
        logstatement = ''
        for i in args:
            logstatement += str(i)
        print(logstatement)
