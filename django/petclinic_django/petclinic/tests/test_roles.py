from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Role

class RoleTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        # Manually create dependencies to avoid recursion issues with instance methods
        user = cls.create_user(cls, username="role_test_user")
        # create_role takes 'user' argument, not 'username'
        cls.role = cls.create_role(cls, user=user)

    def test_create_role(self):
        """Test that a Role instance can be created with valid data."""
        role = self.create_role(role="ROLE_NEW")
        self.assertEqual(role.role, "ROLE_NEW", "Role name should match created value")
        self.assertIsNotNone(role.username, "Username should not be None")

    def test_read_role(self):
        """Test retrieving a Role instance from the database."""
        read_role = Role.objects.get(id=self.role.id)
        self.assertEqual(read_role.role, self.role.role, "Role name should match")
        self.assertEqual(read_role.username.username, self.role.username.username, "Username should match")

    def test_update_role(self):
        """Test updating a Role's attributes."""
        updated_role_name = "ROLE_ADMIN"
        # Create a new role for update test
        role = self.create_role()
        
        Role.objects.filter(id=role.id).update(
            role=updated_role_name
        )
        
        role.refresh_from_db()
        self.assertEqual(role.role, updated_role_name, "Role name should be updated")

    def test_delete_role(self):
        """Test deleting a Role instance."""
        role = self.create_role()
        role_id = role.id
        Role.objects.filter(id=role_id).delete()
        
        with self.assertRaises(Role.DoesNotExist, msg="Role should be deleted"):
            Role.objects.get(id=role_id)

    def test_role_str_method(self):
        """Test the string representation of the Role model."""
        self.assertTrue(str(self.role), "String representation should not be empty")

    def test_create_role_missing_required_fields(self):
        """Test creating a role with missing required fields."""
        with self.assertRaises(Exception):
            Role.objects.create(role=None)
