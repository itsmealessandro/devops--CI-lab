from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Vet

class VetTests(BaseTestCase):
    def test_create_vet(self):
        """Test that a Vet instance can be created with valid data."""
        vet = self.create_vet()
        self.assertEqual(vet.first_name, "Luigi")
        self.assertEqual(vet.last_name, "Verdi")

    def test_read_vet(self):
        """Test retrieving a Vet instance from the database."""
        vet = self.create_vet()
        read_vet = Vet.objects.get(id=vet.id)
        self.assertEqual(read_vet.first_name, vet.first_name)
        self.assertEqual(read_vet.last_name, vet.last_name)

    def test_update_vet(self):
        """Test updating a Vet's attributes."""
        updated_first_name = "Luigi Updated"
        updated_last_name = "Verdi Updated"
        vet = self.create_vet()
        
        Vet.objects.filter(id=vet.id).update(
            first_name=updated_first_name,
            last_name=updated_last_name
        )
        
        vet.refresh_from_db()
        self.assertEqual(vet.first_name, updated_first_name)
        self.assertEqual(vet.last_name, updated_last_name)

    def test_delete_vet(self):
        """Test deleting a Vet instance."""
        vet = self.create_vet()
        Vet.objects.filter(id=vet.id).delete()
        
        with self.assertRaises(Vet.DoesNotExist):
            Vet.objects.get(id=vet.id)
