class customException(Exception):
    def __init__(self):
        super(Exception, self).__init__()
        self.args = ("Raised custom exception",)
        
try:
    raise customException()
except customException as ex:
    print(ex)