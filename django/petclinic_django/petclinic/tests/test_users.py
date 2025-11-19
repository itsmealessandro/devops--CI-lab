from petclinic.tests.base_test import BaseTestCase
from petclinic.models import User

class UserTests(BaseTestCase):
    def test_create_user(self):
        """Test that a User instance can be created with valid data."""
        user = self.create_user()
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.enabled)

    def test_read_user(self):
        """Test retrieving a User instance from the database."""
        user = self.create_user()
        read_user = User.objects.get(username=user.username)
        self.assertEqual(read_user.username, user.username)
        self.assertEqual(read_user.enabled, user.enabled)

    def test_update_user(self):
        """Test updating a User's attributes."""
        updated_password = "newpassword123"
        updated_enabled = False
        user = self.create_user()
        
        User.objects.filter(username=user.username).update(
            password=updated_password,
            enabled=updated_enabled
        )
        
        user.refresh_from_db()
        self.assertEqual(user.password, updated_password)
        self.assertEqual(user.enabled, updated_enabled)

    def test_delete_user(self):
        """Test deleting a User instance."""
        user = self.create_user()
        User.objects.filter(username=user.username).delete()
        
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=user.username)
