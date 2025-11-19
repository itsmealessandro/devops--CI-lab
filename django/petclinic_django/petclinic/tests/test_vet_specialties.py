from petclinic.tests.base_test import BaseTestCase
from petclinic.models import VetSpecialty

class VetSpecialtyTests(BaseTestCase):
    def test_create_vet_specialty(self):
        """Test that a VetSpecialty instance can be created with valid data."""
        vet_specialty = self.create_vet_specialty()
        self.assertIsNotNone(vet_specialty.vet)
        self.assertIsNotNone(vet_specialty.specialty)

    def test_read_vet_specialty(self):
        """Test retrieving a VetSpecialty instance from the database."""
        vet_specialty = self.create_vet_specialty()
        read_vs = VetSpecialty.objects.get(id=vet_specialty.id)
        self.assertEqual(read_vs.vet.id, vet_specialty.vet.id)
        self.assertEqual(read_vs.specialty.id, vet_specialty.specialty.id)

    def test_update_vet_specialty(self):
        """Test updating a VetSpecialty's attributes."""
        vet_specialty = self.create_vet_specialty()
        new_specialty = self.create_specialty(name="Radiology")
        
        VetSpecialty.objects.filter(id=vet_specialty.id).update(specialty=new_specialty)
        
        vet_specialty.refresh_from_db()
        self.assertEqual(vet_specialty.specialty.id, new_specialty.id)

    def test_delete_vet_specialty(self):
        """Test deleting a VetSpecialty instance."""
        vet_specialty = self.create_vet_specialty()
        VetSpecialty.objects.filter(id=vet_specialty.id).delete()
        
        with self.assertRaises(VetSpecialty.DoesNotExist):
            VetSpecialty.objects.get(id=vet_specialty.id)
