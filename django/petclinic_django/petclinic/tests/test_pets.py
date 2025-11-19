# write the pet test like for the owner test

from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Pet

""" CRUD testing for pet """
""" test functionts runs in an lexicographic order"""

class PetTests(BaseTestCase):
    def test_create_pet(self):
        """Test that a Pet instance can be created with valid data."""
        pet = self.create_pet()
        self.assertEqual(pet.id, 1) # id starts from 1 in djangoDB


    def test_read_pet(self):
        """Test retrieving a Pet instance from the database."""
        pet = self.create_pet()
        read_pet = Pet.objects.get(id=pet.id)
        self.assertEqual(read_pet.name, pet.name)
        self.assertEqual(str(read_pet.birth_date), str(pet.birth_date))
        self.assertEqual(read_pet.type.id, pet.type.id)
        self.assertEqual(read_pet.owner.id, pet.owner.id)


    def test_update_pet(self):
        """Test updating a Pet's attributes."""
        updated_name = "Fido Updated"
        updated_birth_date = "2020-01-01"
        pet = self.create_pet()
        Pet.objects.filter(id=pet.id).update(
            name=updated_name,
            birth_date=updated_birth_date
        )

        # Refresh instance from DB to get updated values
        pet.refresh_from_db()

        self.assertEqual(pet.name, updated_name)
        self.assertEqual(str(pet.birth_date), updated_birth_date)


    def test_delete_pet(self):
        """Test deleting a Pet instance."""
        pet= self.create_pet();
        querySet = Pet.objects.filter(id=pet.id)
        querySet.delete()
        with self.assertRaises(Pet.DoesNotExist):
            Pet.objects.get(id=pet.id)

