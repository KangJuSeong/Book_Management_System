from UserPkg.UserDBManager import UserDBManager
from UserPkg.UserController import UserController
import unittest


class TestUserManager(unittest.TestCase):
    
    def test_create(self):
        um = UserDBManager()
        uid = um.createUser('TEST', 'TEST_ADDRESS', 'TEST-3377-5284', True, 'TEST@gmail.com', 'TEST3686')
        test_case = {'uid': uid, 'name': 'TEST', 'address': 'TEST_ADDRESS', 'phone': 'TEST-3377-5284', 'manager': True, 'email': 'TEST@gmail.com', 'password': 'TEST3686'}
        self.assertEqual(UserController(UserDBManager().getUser(uid)).getUserAttr(), test_case)
        um.deleteUser(uid=uid)        
        
    def test_login(self):
        um = UserDBManager()
        uid = um.createUser('TEST', 'TEST_ADDRESS', 'TEST-3377-5284', True, 'TEST@gmail.com', 'TEST3686')
        flag = UserController.login('TEST@gmail.com', 'TEST3686')
        self.assertEqual(flag, uid)
        um.deleteUser(uid=uid)
        

if __name__ == '__main__':
    unittest.main()
    