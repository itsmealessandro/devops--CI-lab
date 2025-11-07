from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Owner

class OwnerTests(BaseTestCase):

    def test_create_owner(self):
        owner = self.create_owner()
        self.assertEqual(owner.first_name, "Mario")

    def test_update_owner(self):
        owner = self.create_owner("MARIO_UPDATE")
        querySet = Owner.objects.filter(id=owner.id)
        querySet.update(first_name="MARIO_UPDATED")
