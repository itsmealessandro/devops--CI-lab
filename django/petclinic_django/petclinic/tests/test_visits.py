from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Visit

class VisitTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests in this class."""
        # Manually create dependencies to avoid recursion issues with instance methods
        owner = cls.create_owner(cls)
        pet_type = cls.create_type(cls)
        pet = cls.create_pet(cls, owner=owner, type=pet_type)
        cls.visit = cls.create_visit(cls, pet=pet)

    def test_create_visit(self):
        """Test that a Visit instance can be created with valid data."""
        visit = self.create_visit(description="New Visit")
        self.assertEqual(visit.description, "New Visit", "Visit description should match created value")

    def test_read_visit(self):
        """Test retrieving a Visit instance from the database."""
        read_visit = Visit.objects.get(id=self.visit.id)
        self.assertEqual(read_visit.description, self.visit.description, "Description should match")
        self.assertEqual(read_visit.pet.id, self.visit.pet.id, "Pet should match")

    def test_update_visit(self):
        """Test updating a Visit's attributes."""
        updated_description = "Emergency visit"
        updated_visit_date = "2024-02-15"
        # Create a new visit for update test
        visit = self.create_visit()
        
        Visit.objects.filter(id=visit.id).update(
            description=updated_description,
            visit_date=updated_visit_date
        )
        
        visit.refresh_from_db()
        self.assertEqual(visit.description, updated_description, "Description should be updated")
        self.assertEqual(str(visit.visit_date), updated_visit_date, "Visit date should be updated")

    def test_delete_visit(self):
        """Test deleting a Visit instance."""
        visit = self.create_visit()
        visit_id = visit.id
        Visit.objects.filter(id=visit_id).delete()
        
        with self.assertRaises(Visit.DoesNotExist, msg="Visit should be deleted"):
            Visit.objects.get(id=visit_id)

    def test_visit_str_method(self):
        """Test the string representation of the Visit model."""
        self.assertTrue(str(self.visit), "String representation should not be empty")

    def test_create_visit_missing_required_fields(self):
        """Test creating a visit with missing required fields."""
        with self.assertRaises(Exception):
            Visit.objects.create(description=None)
