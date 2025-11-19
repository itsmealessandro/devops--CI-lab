from petclinic.tests.base_test import BaseTestCase
from petclinic.models import User

class UserTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        # Use a unique username for the shared user
        cls.user = cls.create_user(cls, username="shared_user")

    def test_create_user(self):
        """Test that a User instance can be created with valid data."""
        # Use a unique username for this test
        user = self.create_user(username="newuser_create")
        self.assertEqual(user.username, "newuser_create", "Username should match created value")
        self.assertTrue(user.enabled, "User should be enabled by default")

    def test_read_user(self):
        """Test retrieving a User instance from the database."""
        read_user = User.objects.get(username=self.user.username)
        self.assertEqual(read_user.username, self.user.username, "Username should match")
        self.assertEqual(read_user.password, self.user.password, "Password should match")

    def test_update_user(self):
        """Test updating a User's attributes."""
        updated_password = "newpassword123"
        updated_enabled = False
        # Create a new user for update test with unique username
        user = self.create_user(username="update_test_user")
        
        User.objects.filter(username=user.username).update(
            password=updated_password,
            enabled=updated_enabled
        )
        
        user.refresh_from_db()
        self.assertEqual(user.password, updated_password, "Password should be updated")
        self.assertEqual(user.enabled, updated_enabled, "Enabled status should be updated")

    def test_delete_user(self):
        """Test deleting a User instance."""
        user = self.create_user()
        username = user.username
        User.objects.filter(username=username).delete()
        
        with self.assertRaises(User.DoesNotExist, msg="User should be deleted"):
            User.objects.get(username=username)

    def test_user_str_method(self):
        """Test the string representation of the User model."""
        self.assertTrue(str(self.user), "String representation should not be empty")

    def test_create_user_missing_required_fields(self):
        """Test creating a user with missing required fields."""
        # SQLite might allow NULLs if not strictly enforced or if Django model allows it.
        # However, username is usually required. If create() doesn't fail, full_clean() should.
        user = User(username=None)
        with self.assertRaises(Exception):
             # Force model validation
             user.full_clean()
             user.save()
