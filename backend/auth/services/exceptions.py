#(c) 2017, Jason Gao <kidnet05@gmail.com>
#This file is part of OMCenter Programe

class UserEexception(Exception):
    #The base User Management exception from which all others should subclass.
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
