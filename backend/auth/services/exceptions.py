#(c) 2017, Jason Gao <kidnet05@gmail.com>
#This file is part of OMCenter Programe

class UserMgmtException(Exception):
    #The base User Management exception from which all others should subclass.
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class UserDoesNotExist(UserMgmtException):
    pass

class UnknowError(UserMgmtException):
    pass

class UserAuthException(Exception):
    #The base User Management exception from which all others should subclass.
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return {
            "status": self.code,
            "msg": self.msg
        }

class UserAuthFailed(UserAuthException):
    def __init__(self):
        self.code = 1022
        self.msg = 'user auth failed'