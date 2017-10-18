# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=45, unique=True)
    nickName = models.CharField(max_length=45, unique=True)
    email = models.CharField(max_length=60, unique=True)
    phoneNum = models.CharField(max_length=30, unique=True)
    comment = models.CharField(max_length=100, null=True)
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'user'
    def __unicode__(self):
        ret = {'id': self.id,
               'userName': self.userName,
               'nickName': self.nickName,
               'email': self.email,
               'phoneNum': self.phoneNum,
               'comment': self.comment,
               'createTimestamp': str(self.createTimestamp),
               'updateTimestamp': str(self.updateTimestamp)
               }
        return json.dumps(ret)

class LocalAuth(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(unique=True)
    salt = models.CharField(max_length=45)
    password = models.CharField(max_length=256)
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'localAuth'
    def __unicode__(self):
        return u'%d %s %s' % (self.uid, self.salt, self.password)

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(unique=True)
    token = models.CharField(max_length=100, unique=True)
    permission = models.CharField(max_length=280)
    ip = models.CharField(max_length=15)
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'token'
        unique_together = (("uid", "token"))
    def __unicode__(self):
        return u'%d %d %s %s' % (self.id, self.uid, self.token, self.permissions)

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=45)
    comment = models.CharField(max_length=100)
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'role'
    def __unicode__(self):
        return u'%d %s %s' % (self.rid, self.roleName, self.comment)

class RoleMember(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(unique=True)
    rid = models.IntegerField(unique=True)
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'roleMember'
    def __unicode__(self):
        return u'%d %d %d' % (self.id, self.uid, self.rid)

class Module(models.Model):
    id = models.AutoField(primary_key=True)
    moduleName = models.CharField(max_length=45)
    nickName = models.CharField(max_length=45)
    comment = models.CharField(max_length=100)
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'module'
    def __unicode__(self):
        return u'%d %s %s %s' % (
                self.id, 
                self.moduleName, 
                self.nickName, 
                self.comment
                )

class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    mid = models.IntegerField(unique=True)
    rid = models.IntegerField(unique=True)
    permission = models.IntegerField()
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'permission'
    def __unicode__(self):
        return u'%d %d %d' % (self.mid, self.rid, self.permission)

class ModuleRelationship(models.Model):
    id = models.AutoField(primary_key=True)
    mid = models.IntegerField(unique=True)
    pid = models.IntegerField(unique=True)
    createTimestamp = models.DateTimeField(auto_now_add=True)
    updateTimestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'moduleRelationship'
    def __unicode__(self):
        return u'%d %d %d' % (self.mid, self.rid, self.permission)
