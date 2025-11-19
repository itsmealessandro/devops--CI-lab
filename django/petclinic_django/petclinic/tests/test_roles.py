from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Role

class RoleTests(BaseTestCase):
    def test_create_role(self):
        print("######################################")
        print("ROLE TESTING")
        print("-------------- create role --------------")
        role = self.create_role()
        self.assertEqual(role.role, "ROLE_USER")
        self.assertIsNotNone(role.username)

    def test_read_role(self):
        print("-------------- read role --------------")
        role = self.create_role()
        read_role = Role.objects.get(id=role.id)
        self.assertEqual(read_role.role, role.role)
        self.assertEqual(read_role.username.username, role.username.username)

    def test_update_role(self):
        print("-------------- update role --------------")
        ROLE_NAME = "ROLE_ADMIN"
        role = self.create_role()
        
        Role.objects.filter(id=role.id).update(role=ROLE_NAME)
        
        role.refresh_from_db()
        self.assertEqual(role.role, ROLE_NAME)

    def test_delete_role(self):
        print("-------------- delete role --------------")
        role = self.create_role()
        Role.objects.filter(id=role.id).delete()
        
        with self.assertRaises(Role.DoesNotExist):
            Role.objects.get(id=role.id)
