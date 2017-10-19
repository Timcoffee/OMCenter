# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from controller.userMgmt import getUserCNTLR
from controller.userMgmt import addUserCNTLR
from controller.userMgmt import delUserCNTLR
from controller.userMgmt import updUserCNTLR
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

    #ret = chkDict(postJson, ['uid',])

    #if ret['status'] >= 9000:
    #    return HttpResponse(json.dumps(ret))

    if 'uid' in postJson:
        ret = getUserCNTLR(uid=int(postJson['uid']))
    elif 'userName' in postJson:
        ret = getUserCNTLR(userName=postJson['userName'])
    else:
        ret = getUserCNTLR()

    ret['object'] = ''
    return HttpResponse(json.dumps(ret))

@csrf_exempt
def addUser(request):
    defLogger.info(request)

    #format request data.
    postJson = fmtRequest(request)

    ret = chkDict(postJson, ['userName', 
                             'email',
                             'phoneNum',
                             'nickName',
                             'comment'])

    if ret['status'] != 0:
        return HttpResponse(json.dumps(ret))

    ret = addUserCNTLR(postJson['userName'], 
                       postJson['email'],
                       postJson['phoneNum'],
                       postJson['nickName'],
                       postJson['comment'])

    defLogger.debug(json.dumps(ret))

    return HttpResponse(json.dumps(ret))

@csrf_exempt
def delUser(request):
    defLogger.info(request)

    #format request data.
    postJson = fmtRequest(request)

    ret = chkDict(postJson, ['uid',])

    if ret['status'] != 0:
        return HttpResponse(json.dumps(ret))
    
    ret = delUserCNTLR(uid=int(postJson['uid']))

    defLogger.debug(json.dumps(ret))

    return HttpResponse(json.dumps(ret))

@csrf_exempt
def updUser(request):
    defLogger.info(request)

    #format request data.
    postJson = fmtRequest(request)

    ret = chkDict(postJson, ['uid',
                             'userName',
                             'email',
                             'phoneNum',
                             'nickName',
                             'comment'])
    if ret['status'] != 0:
        return ret

    ret = updUserCNTLR(postJson['uid'],
                       postJson['userName'], 
                       postJson['email'],
                       postJson['phoneNum'],
                       postJson['nickName'],
                       postJson['comment'])

    defLogger.debug(json.dumps(ret))

    return HttpResponse(json.dumps(ret))
