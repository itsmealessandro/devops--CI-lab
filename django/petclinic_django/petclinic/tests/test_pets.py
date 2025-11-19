# write the pet test like for the owner test

from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Pet

""" CRUD testing for pet """
""" test functionts runs in an lexicographic order"""

class PetTests(BaseTestCase):
    def test_create_pet(self):

        print("######################################")
        print("PET TESTING")

        print("-------------- create pet --------------")
        pet = self.create_pet()
        self.assertEqual(pet.id, 1) # id starts from 1 in djangoDB


    def test_read_pet(self):
        print("-------------- read pet --------------")
        pet = self.create_pet()
        read_pet = Pet.objects.get(id=pet.id)
        self.assertEqual(read_pet.name, pet.name)
        self.assertEqual(str(read_pet.birth_date), str(pet.birth_date))
        self.assertEqual(read_pet.type.id, pet.type.id)
        self.assertEqual(read_pet.owner.id, pet.owner.id)


    def test_update_pet(self):
        print("-------------- update pet --------------")
        NAME = "FIDO_UPDATED"
        BIRTH_DATE = "2020-01-01"
        pet = self.create_pet()
        print("old pet:")
        print(pet)
        querySet = Pet.objects.filter(id=pet.id)
        querySet.update(
            name=NAME,
            birth_date=BIRTH_DATE
        )

        # Refresh instance from DB to get updated values
        pet.refresh_from_db()

        print("pet after refresh_from_db")
        print(pet)
        self.assertEqual(pet.name, NAME)
        self.assertEqual(str(pet.birth_date), BIRTH_DATE)


    def test_delete_pet(self):
        print("-------------- delete pet --------------")
        pet= self.create_pet();
        querySet = Pet.objects.filter(id=pet.id)
        querySet.delete()
        with self.assertRaises(Pet.DoesNotExist):
            Pet.objects.get(id=pet.id)

