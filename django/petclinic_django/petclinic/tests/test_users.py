from petclinic.tests.base_test import BaseTestCase
from petclinic.models import User

class UserTests(BaseTestCase):
    def test_create_user(self):
        print("######################################")
        print("USER TESTING")
        print("-------------- create user --------------")
        user = self.create_user()
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.enabled)

    def test_read_user(self):
        print("-------------- read user --------------")
        user = self.create_user()
        read_user = User.objects.get(username=user.username)
        self.assertEqual(read_user.username, user.username)
        self.assertEqual(read_user.enabled, user.enabled)

    def test_update_user(self):
        print("-------------- update user --------------")
        PASSWORD = "newpassword123"
        ENABLED = False
        user = self.create_user()
        
        User.objects.filter(username=user.username).update(
            password=PASSWORD,
            enabled=ENABLED
        )
        
        user.refresh_from_db()
        self.assertEqual(user.password, PASSWORD)
        self.assertEqual(user.enabled, ENABLED)

    def test_delete_user(self):
        print("-------------- delete user --------------")
        user = self.create_user()
        User.objects.filter(username=user.username).delete()
        
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=user.username)
