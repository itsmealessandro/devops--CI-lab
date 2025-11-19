from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Owner
""" CRUD testing for owner """
""" test functionts runs in an lexicographic order"""
class OwnerTests(BaseTestCase):

    def test_create_owner(self):
        """Test that an Owner instance can be created with valid data."""
        owner = self.create_owner()
        self.assertEqual(owner.id, 1) # id starts from 1 in djangoDB


    def test_read_owner(self):
        """Test retrieving an Owner instance from the database."""
        owner = self.create_owner()
        read_owner = Owner.objects.get(id=owner.id)
        self.assertEqual(read_owner.first_name, owner.first_name)
        self.assertEqual(read_owner.last_name, owner.last_name)
        self.assertEqual(read_owner.address, owner.address)
        self.assertEqual(read_owner.city, owner.city)
        self.assertEqual(read_owner.telephone, owner.telephone)




    def test_update_owner(self):
        """Test updating an Owner's attributes."""
        updated_first_name = "Mario Updated"
        updated_last_name = "Rossi Updated"
        updated_address = "Via Milano 99"
        updated_city = "Rome"
        updated_telephone = "3339876543"
        owner = self.create_owner()
        Owner.objects.filter(id=owner.id).update(
            first_name=updated_first_name,
            last_name=updated_last_name,
            address=updated_address,
            city=updated_city,
            telephone=updated_telephone
        )

        # Refresh instance from DB to get updated values
        owner.refresh_from_db()

        self.assertEqual(owner.first_name, updated_first_name)
        self.assertEqual(owner.last_name, updated_last_name)
        self.assertEqual(owner.address, updated_address)
        self.assertEqual(owner.city, updated_city)
        self.assertEqual(owner.telephone, updated_telephone)


    def test_delete_owner(self):
        """Test deleting an Owner instance."""
        owner= self.create_owner();
        querySet = Owner.objects.filter(id=owner.id)
        querySet.delete()

        with self.assertRaises(Owner.DoesNotExist):
            Owner.objects.get(id=owner.id)
