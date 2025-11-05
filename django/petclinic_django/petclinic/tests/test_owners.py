from petclinic.tests.base_test import BaseTestCase

class OwnerTests(BaseTestCase):
    def test_create_owner(self):
        owner = self.create_owner()
        self.assertEqual(owner.first_name, "Mario")
