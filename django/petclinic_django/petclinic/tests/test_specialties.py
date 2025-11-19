from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Specialty

class SpecialtyTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        cls.specialty = cls.create_specialty(cls)

    def test_create_specialty(self):
        """Test that a Specialty instance can be created with valid data."""
        specialty = self.create_specialty(name="New Specialty")
        self.assertEqual(specialty.name, "New Specialty", "Specialty name should match created value")

    def test_read_specialty(self):
        """Test retrieving a Specialty instance from the database."""
        read_specialty = Specialty.objects.get(id=self.specialty.id)
        self.assertEqual(read_specialty.name, self.specialty.name, "Specialty name should match")

    def test_update_specialty(self):
        """Test updating a Specialty's attributes."""
        updated_name = "Cardiology"
        # Create a new specialty for update test
        specialty = self.create_specialty()
        
        Specialty.objects.filter(id=specialty.id).update(
            name=updated_name
        )
        
        specialty.refresh_from_db()
        self.assertEqual(specialty.name, updated_name, "Specialty name should be updated")

    def test_delete_specialty(self):
        """Test deleting a Specialty instance."""
        specialty = self.create_specialty()
        specialty_id = specialty.id
        Specialty.objects.filter(id=specialty_id).delete()
        
        with self.assertRaises(Specialty.DoesNotExist, msg="Specialty should be deleted"):
            Specialty.objects.get(id=specialty_id)

    def test_specialty_str_method(self):
        """Test the string representation of the Specialty model."""
        self.assertTrue(str(self.specialty), "String representation should not be empty")

    def test_create_specialty_missing_required_fields(self):
        """Test creating a specialty with missing required fields."""
        with self.assertRaises(Exception):
            Specialty.objects.create(name=None)
