class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                break

    def display_users(self):
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")


# Пример использования
user1 = User(1, 'Alice')
user2 = User(2, 'Bob')
admin = Admin(3, 'Admin')

admin.add_user(user1)
admin.add_user(user2)
admin.display_users()

admin.remove_user(1)
admin.display_users()





