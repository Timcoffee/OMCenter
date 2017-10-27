from unittest import TestCase
from django.test import Client
from auth.models import User
import json

class GetUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        try:
            user = User.objects.get(userName="test1")
            user.delete()
            user = User.objects.get(userName="test2")
            user.delete()
        except Exception:
            pass

    def testGetUser(self):
        userDataHandler = User(userName='test1', 
                nickName='nicktest', 
                email='test1@test.com', 
                phoneNum='21111111111', 
                comment='')
        userDataHandler.save()

        response = self.client.post('/omservice/usermgmt/user/', 
                                    {'userName': 'test1'})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)

        #self.assertEqual(data['msg'], 0)
        #self.assertEqual(data['result'], 0)

        self.assertEqual(data['status'], 0)

    def testGetAllUser(self):
        userDataHandler = User(userName='test1', 
                nickName='nicktest', 
                email='test1@test.com', 
                phoneNum='21111111111', 
                comment='')
        userDataHandler.save()
        userDataHandler = User(userName='test2', 
                nickName='nicktest2', 
                email='test2@test.com', 
                phoneNum='11111111112', 
                comment='')
        userDataHandler.save()

        response = self.client.post('/omservice/usermgmt/user/', {'all': 'all'})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)

        #self.assertEqual(data['msg'], 0)
        #self.assertEqual(data['result'], 0)

        self.assertEqual(data['status'], 0)

class AddUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        user = User.objects.get(userName="test")
        user.delete()

    def testAddUserWhenTheUserDoesNotExsit(self):
        response = self.client.post('/omservice/usermgmt/adduser/', 
                {'userName': 'test', 
                 'email':'test@test.com',
                 'phoneNum':'11111111111',
                 'nickName':'testnickname',
                 'comment':''})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(data['status'], 0)

    def testAddUserWhenTheUserHasExsited(self):
        userDataHandler = User(userName='test', 
                nickName='nicktest', 
                email='test@test.com', 
                phoneNum='11111111111', 
                comment='')
        userDataHandler.save()

        response = self.client.post('/omservice/usermgmt/adduser/', 
                {'userName': 'test', 
                 'email':'test@test.com',
                 'phoneNum':'11111111111',
                 'nickName':'testnickname',
                 'comment':''})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(int(data['status']), 1048)

class DelUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def testDelUserWhenTheUserHasExsited(self):
        userDataHandler = User(userName='test', 
                nickName='nicktest', 
                email='test@test.com', 
                phoneNum='11111111111', 
                comment='')
        userDataHandler.save()

        uid = userDataHandler.id
        response = self.client.post('/omservice/usermgmt/deluser/', 
                {'uid':uid})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(data['status']), 0)

    def testDelUserWhenTheUserDoesNotExsit(self):
        response = self.client.post('/omservice/usermgmt/deluser/', 
                {'uid': 1})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(data['status']), 0)

class UdpUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        try:
            user = User.objects.get(userName='test')
            user.delete()
        except Exception:
            pass

    def testUdpUserWhenTheUserHasExsited(self):
        userDataHandler = User(userName='test', 
                nickName='nicktest', 
                email='test@test.com', 
                phoneNum='11111111111', 
                comment='')
        userDataHandler.save()

        uid = userDataHandler.id
        userName = userDataHandler.userName
        nickName = 'nicktest1'
        email = 'test1@test.com'
        phoneNum = userDataHandler.phoneNum
        comment = 'test'
        response = self.client.post('/omservice/usermgmt/udpuser/', 
                {'uid':uid,
                 'userName': userName,
                 'nickName': nickName,
                 'email': email,
                 'phoneNum': phoneNum,
                 'comment': comment})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(data['status']), 0)

    def testUdpUserWhenTheUserDoesNotExsit(self):
        uid = 2
        userName = 'test'
        nickName = 'nicktest1'
        email = 'test1@test.com'
        phoneNum = '1'
        comment = 'test'
        response = self.client.post('/omservice/usermgmt/udpuser/', 
                {'uid':uid,
                 'userName': userName,
                 'nickName': nickName,
                 'email': email,
                 'phoneNum': phoneNum,
                 'comment': comment})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(data['status']), 1001)
