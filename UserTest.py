from UserPkg.UserManager import UserManager


if __name__ == '__main__':
    um = UserManager()
    # print(um.listUser())
    print(um.createUser('강주성', '성북구 솔샘로 4길', '01033775284', True, 'wntjd3686@gmail.com', '123456789'))