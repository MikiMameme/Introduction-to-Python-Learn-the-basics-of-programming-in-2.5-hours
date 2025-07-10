class User:
    def __init__(self, name, mail_adress, point):
        self.name = name
        self.mail_adress = mail_adress
        self.point = point

    def add_point(self, point):
        self.point += point

user_1 = User("佐藤葵", "sato@example.com", 500)
user_1.add_point(100)
print(user_1.point)

user_2 = User("小林ゆい", "kobayashi@example.com", 1000)
user_2.point = 0
print(user_2.point)

