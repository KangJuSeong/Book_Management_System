from UserPkg.UserManager import UserManager
import unittest


class TestUserManager(unittest.TestCase):
    
    def test_create(self):
        um = UserManager()
        uid = um.createUser('TEST', 'TEST_ADDRESS', 'TEST-3377-5284', True, 'TEST@gmail.com', 'TEST3686')
        test_case = [uid, 'TEST', 'TEST_ADDRESS', 'TEST-3377-5284', True, 'TEST@gmail.com', 'TEST3686']
        self.assertEqual(um.getUser(uid=uid), test_case)
        um.deleteUser(uid=uid)        


    def test_update(self):
        um = UserManager()
        uid = um.createUser('UPDATE_TEST', 'UPDATE_TEST', 'UPDATE_TEST', False, 'UPDATE_TEST', 'UPDATE_TEST')
        flag = um.updateUser('test', 'test', 'test', True, 'test', 'test', uid)
        result = um.getUser(uid=uid)
        result.append(flag)
        test_case = [uid, 'test', 'test', 'test', True, 'test', 'test', True]
        um.deleteUser(uid=uid)
        self.assertEqual(result, test_case)
        
    def test_login(self):
        um = UserManager()
        uid = um.createUser('TEST', 'TEST_ADDRESS', 'TEST-3377-5284', True, 'TEST@gmail.com', 'TEST3686')
        flag = um.login('TEST@gmail.com', 'TEST3686')
        self.assertEqual(flag, True)
        um.deleteUser(uid=uid)
        

if __name__ == '__main__':
    unittest.main()
    