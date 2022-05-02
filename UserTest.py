from UserPkg.UserManager import UserManager
import unittest


if __name__ == '__main__':
    um = UserManager()
    print(um.listUser())  # 번호 및 전화번호에 문자열이 들어가야 저장할 때 문자열로 저장됨
    print(um.createUser('강주성', '성북구 솔샘로 4길', '010-3377-5284', True, 'wntjd3686@gmail.com', '123456789'))