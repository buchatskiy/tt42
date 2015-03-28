from django.test import TestCase
from users.models import Users
import datetime


class UserModelTest(TestCase):
    def test_new_save(self):
        user = Users()
        user.first_name = "Oleksandr"
        user.last_name = "Buchatskiy"
        user.date_birth = datetime.date(1990, 2, 20)
        user.email = "buchatskiy2@yandex.ru"
        user.jabber = "buchatskiy@chrome.pl"
        user.skype = "buchatskiy2"
        user.bio = "test/ntest/ntest"
        user.save()

        all_users = Users.objects.all()
        self.assertEquals(len(all_users), 1)
        first_user = all_users[0]
        self.assertEquals(first_user, user)

        self.assertEquals(first_user.email, "buchatskiy2@yandex.ru")
        self.assertEquals(first_user.date_birth, datetime.date(1990, 2, 20))