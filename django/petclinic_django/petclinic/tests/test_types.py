from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Type

class TypeTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        cls.pet_type = cls.create_type(cls)

    def test_create_type(self):
        """Test that a Type instance can be created with valid data."""
        pet_type = self.create_type(name="New Type")
        self.assertEqual(pet_type.name, "New Type", "Type name should match created value")

    def test_read_type(self):
        """Test retrieving a Type instance from the database."""
        read_type = Type.objects.get(id=self.pet_type.id)
        self.assertEqual(read_type.name, self.pet_type.name, "Type name should match")

    def test_update_type(self):
        """Test updating a Type's attributes."""
        updated_name = "Cat"
        # Create a new type for update test
        pet_type = self.create_type()
        
        Type.objects.filter(id=pet_type.id).update(
            name=updated_name
        )
        
        pet_type.refresh_from_db()
        self.assertEqual(pet_type.name, updated_name, "Type name should be updated")

    def test_delete_type(self):
        """Test deleting a Type instance."""
        pet_type = self.create_type()
        type_id = pet_type.id
        Type.objects.filter(id=type_id).delete()
        
        with self.assertRaises(Type.DoesNotExist, msg="Type should be deleted"):
            Type.objects.get(id=type_id)

    def test_type_str_method(self):
        """Test the string representation of the Type model."""
        self.assertTrue(str(self.pet_type), "String representation should not be empty")

    def test_create_type_missing_required_fields(self):
        """Test creating a type with missing required fields."""
        with self.assertRaises(Exception):
            Type.objects.create(name=None)
