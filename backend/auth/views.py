# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from controller.userMgmt import getUser
from controller.dataFmt import fmtRequest
from controller.dataChk import chkDict
import logging
import json


#Get logger from django config.
defLogger = logging.getLogger('platform')
reqLogger = logging.getLogger('request')


@csrf_exempt
def user(request):
    defLogger.info(request)

    #format request data.
    postJson = fmtRequest(request)

    ret = chkDict(postJson, ['uid',])

    if ret['status'] >= 9000:
        return HttpResponse(json.dumps(ret))

    ret = getUser(uid=int(postJson['uid']))
    ret['object'] = ''
    return HttpResponse(json.dumps(ret))

def users(request):    
    pass
