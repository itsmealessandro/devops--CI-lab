from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Specialty

class SpecialtyTests(BaseTestCase):
    def test_create_specialty(self):
        """Test that a Specialty instance can be created with valid data."""
        specialty = self.create_specialty()
        self.assertEqual(specialty.name, "Surgery")

    def test_read_specialty(self):
        """Test retrieving a Specialty instance from the database."""
        specialty = self.create_specialty()
        read_specialty = Specialty.objects.get(id=specialty.id)
        self.assertEqual(read_specialty.name, specialty.name)

    def test_update_specialty(self):
        """Test updating a Specialty's attributes."""
        updated_name = "Cardiology"
        specialty = self.create_specialty()
        
        Specialty.objects.filter(id=specialty.id).update(name=updated_name)
        
        specialty.refresh_from_db()
        self.assertEqual(specialty.name, updated_name)

    def test_delete_specialty(self):
        """Test deleting a Specialty instance."""
        specialty = self.create_specialty()
        Specialty.objects.filter(id=specialty.id).delete()
        
        with self.assertRaises(Specialty.DoesNotExist):
            Specialty.objects.get(id=specialty.id)
