class CommandHistory (object):
    def __init__ (self, *args, **kwargs):
        self.__history = []

    def add (self, uCommand):
        ## skip, in case is a repeated command
        if uCommand == self.__history [-1]: return
        self.__history.append (uCommand)

    def get_back (self):
        return self.__history.pop ()
