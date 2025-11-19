from petclinic.tests.base_test import BaseTestCase
from petclinic.models import VetSpecialty

class VetSpecialtyTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        # Manually create dependencies to avoid recursion issues with instance methods
        vet = cls.create_vet(cls)
        specialty = cls.create_specialty(cls)
        cls.vet_specialty = cls.create_vet_specialty(cls, vet=vet, specialty=specialty)

    def test_create_vet_specialty(self):
        """Test that a VetSpecialty instance can be created with valid data."""
        vet_specialty = self.create_vet_specialty()
        self.assertIsNotNone(vet_specialty.vet, "Vet should not be None")
        self.assertIsNotNone(vet_specialty.specialty, "Specialty should not be None")

    def test_read_vet_specialty(self):
        """Test retrieving a VetSpecialty instance from the database."""
        read_vs = VetSpecialty.objects.get(id=self.vet_specialty.id)
        self.assertEqual(read_vs.vet.id, self.vet_specialty.vet.id, "Vet ID should match")
        self.assertEqual(read_vs.specialty.id, self.vet_specialty.specialty.id, "Specialty ID should match")

    def test_update_vet_specialty(self):
        """Test updating a VetSpecialty's attributes."""
        # Create a new vet_specialty for update test
        vet_specialty = self.create_vet_specialty()
        new_specialty = self.create_specialty(name="Radiology")
        
        VetSpecialty.objects.filter(id=vet_specialty.id).update(
            specialty=new_specialty
        )
        
        vet_specialty.refresh_from_db()
        self.assertEqual(vet_specialty.specialty.id, new_specialty.id, "Specialty ID should be updated")

    def test_delete_vet_specialty(self):
        """Test deleting a VetSpecialty instance."""
        vet_specialty = self.create_vet_specialty()
        vs_id = vet_specialty.id
        VetSpecialty.objects.filter(id=vs_id).delete()
        
        with self.assertRaises(VetSpecialty.DoesNotExist, msg="VetSpecialty should be deleted"):
            VetSpecialty.objects.get(id=vs_id)

    def test_vet_specialty_str_method(self):
        """Test the string representation of the VetSpecialty model."""
        self.assertTrue(str(self.vet_specialty), "String representation should not be empty")

    def test_create_vet_specialty_missing_required_fields(self):
        """Test creating a vet_specialty with missing required fields."""
        with self.assertRaises(Exception):
            VetSpecialty.objects.create(vet=None)
