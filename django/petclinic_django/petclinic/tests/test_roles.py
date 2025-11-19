from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Role

class RoleTests(BaseTestCase):
    def test_create_role(self):
        """Test that a Role instance can be created with valid data."""
        role = self.create_role()
        self.assertEqual(role.role, "ROLE_USER")
        self.assertIsNotNone(role.username)

    def test_read_role(self):
        """Test retrieving a Role instance from the database."""
        role = self.create_role()
        read_role = Role.objects.get(id=role.id)
        self.assertEqual(read_role.role, role.role)
        self.assertEqual(read_role.username.username, role.username.username)

    def test_update_role(self):
        """Test updating a Role's attributes."""
        updated_role_name = "ROLE_ADMIN"
        role = self.create_role()
        
        Role.objects.filter(id=role.id).update(role=updated_role_name)
        
        role.refresh_from_db()
        self.assertEqual(role.role, updated_role_name)

    def test_delete_role(self):
        """Test deleting a Role instance."""
        role = self.create_role()
        Role.objects.filter(id=role.id).delete()
        
        with self.assertRaises(Role.DoesNotExist):
            Role.objects.get(id=role.id)
