from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Type

class TypeTests(BaseTestCase):
    def test_create_type(self):
        """Test that a Type instance can be created with valid data."""
        pet_type = self.create_type()
        self.assertEqual(pet_type.name, "Dog")

    def test_read_type(self):
        """Test retrieving a Type instance from the database."""
        pet_type = self.create_type()
        read_type = Type.objects.get(id=pet_type.id)
        self.assertEqual(read_type.name, pet_type.name)

    def test_update_type(self):
        """Test updating a Type's attributes."""
        updated_name = "Cat"
        pet_type = self.create_type()
        
        Type.objects.filter(id=pet_type.id).update(name=updated_name)
        
        pet_type.refresh_from_db()
        self.assertEqual(pet_type.name, updated_name)

    def test_delete_type(self):
        """Test deleting a Type instance."""
        pet_type = self.create_type()
        Type.objects.filter(id=pet_type.id).delete()
        
        with self.assertRaises(Type.DoesNotExist):
            Type.objects.get(id=pet_type.id)
