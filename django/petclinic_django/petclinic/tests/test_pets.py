# write the pet test like for the owner test

from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Pet

""" CRUD testing for pet """
""" test functionts runs in an lexicographic order"""

class PetTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        # We need to create dependencies explicitly because helper methods in BaseTestCase
        # are instance methods and might not work correctly when called with 'cls' if they use 'self'.
        # However, create_pet uses self.create_owner().
        # To fix this without refactoring BaseTestCase completely, we can manually create the dependencies here.
        owner = cls.create_owner(cls)
        pet_type = cls.create_type(cls)
        cls.pet = cls.create_pet(cls, owner=owner, type=pet_type)

    def test_create_pet(self):
        """Test that a Pet instance can be created with valid data."""
        pet = self.create_pet(name="New Pet")
        self.assertEqual(pet.name, "New Pet", "Pet name should match created value")


    def test_read_pet(self):
        """Test retrieving a Pet instance from the database."""
        read_pet = Pet.objects.get(id=self.pet.id)
        self.assertEqual(read_pet.name, self.pet.name, "Pet name should match")
        self.assertEqual(str(read_pet.birth_date), str(self.pet.birth_date), "Birth date should match")
        self.assertEqual(read_pet.type.id, self.pet.type.id, "Pet type should match")
        self.assertEqual(read_pet.owner.id, self.pet.owner.id, "Pet owner should match")


    def test_update_pet(self):
        """Test updating a Pet's attributes."""
        updated_name = "Fido Updated"
        updated_birth_date = "2020-01-01"
        # Create a new pet for update test
        pet = self.create_pet()
        
        Pet.objects.filter(id=pet.id).update(
            name=updated_name,
            birth_date=updated_birth_date
        )

        # Refresh instance from DB to get updated values
        pet.refresh_from_db()

        self.assertEqual(pet.name, updated_name, "Pet name should be updated")
        self.assertEqual(str(pet.birth_date), updated_birth_date, "Birth date should be updated")


    def test_delete_pet(self):
        """Test deleting a Pet instance."""
        pet = self.create_pet()
        pet_id = pet.id
        Pet.objects.filter(id=pet_id).delete()
        
        with self.assertRaises(Pet.DoesNotExist, msg="Pet should be deleted"):
            Pet.objects.get(id=pet_id)

    def test_pet_str_method(self):
        """Test the string representation of the Pet model."""
        self.assertTrue(str(self.pet), "String representation should not be empty")

    def test_create_pet_missing_required_fields(self):
        """Test creating a pet with missing required fields."""
        with self.assertRaises(Exception):
            Pet.objects.create(name=None)

