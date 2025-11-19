from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Vet

class VetTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        cls.vet = cls.create_vet(cls)

    def test_create_vet(self):
        """Test that a Vet instance can be created with valid data."""
        vet = self.create_vet(first_name="New", last_name="Vet")
        self.assertEqual(vet.first_name, "New", "Vet first name should match created value")
        self.assertEqual(vet.last_name, "Vet", "Vet last name should match created value")

    def test_read_vet(self):
        """Test retrieving a Vet instance from the database."""
        read_vet = Vet.objects.get(id=self.vet.id)
        self.assertEqual(read_vet.first_name, self.vet.first_name, "First name should match")
        self.assertEqual(read_vet.last_name, self.vet.last_name, "Last name should match")

    def test_update_vet(self):
        """Test updating a Vet's attributes."""
        updated_first_name = "Luigi Updated"
        updated_last_name = "Verdi Updated"
        # Create a new vet for update test
        vet = self.create_vet()
        
        Vet.objects.filter(id=vet.id).update(
            first_name=updated_first_name,
            last_name=updated_last_name
        )
        
        vet.refresh_from_db()
        self.assertEqual(vet.first_name, updated_first_name, "First name should be updated")
        self.assertEqual(vet.last_name, updated_last_name, "Last name should be updated")

    def test_delete_vet(self):
        """Test deleting a Vet instance."""
        vet = self.create_vet()
        vet_id = vet.id
        Vet.objects.filter(id=vet_id).delete()
        
        with self.assertRaises(Vet.DoesNotExist, msg="Vet should be deleted"):
            Vet.objects.get(id=vet_id)

    def test_vet_str_method(self):
        """Test the string representation of the Vet model."""
        self.assertTrue(str(self.vet), "String representation should not be empty")

    def test_create_vet_missing_required_fields(self):
        """Test creating a vet with missing required fields."""
        with self.assertRaises(Exception):
            Vet.objects.create(first_name=None)
