users = {
    'aaa':'111',
    'bbb':'222'
}
def isUser(f):
    def wrap(*args,**kwargs):
        name = input('请输入用户名:')
        passwd = input('请输入密码:')
        for user in users.items():
            if user[0]==name and passwd==user[1]:
                print('认证成功')
                f()
                return
            else:
                print('认证失败')
    return wrap

@isUser
def test():
    print('认证完成,谢谢!')
test()