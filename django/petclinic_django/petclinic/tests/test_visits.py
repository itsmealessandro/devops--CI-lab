from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Visit

class VisitTests(BaseTestCase):
    def test_create_visit(self):
        """Test that a Visit instance can be created with valid data."""
        visit = self.create_visit()
        self.assertEqual(visit.description, "Regular checkup")
        self.assertEqual(str(visit.visit_date), "2024-01-01")

    def test_read_visit(self):
        """Test retrieving a Visit instance from the database."""
        visit = self.create_visit()
        read_visit = Visit.objects.get(id=visit.id)
        self.assertEqual(read_visit.description, visit.description)
        self.assertEqual(read_visit.pet.id, visit.pet.id)

    def test_update_visit(self):
        """Test updating a Visit's attributes."""
        updated_description = "Emergency visit"
        updated_visit_date = "2024-02-15"
        visit = self.create_visit()
        
        Visit.objects.filter(id=visit.id).update(
            description=updated_description,
            visit_date=updated_visit_date
        )
        
        visit.refresh_from_db()
        self.assertEqual(visit.description, updated_description)
        self.assertEqual(str(visit.visit_date), updated_visit_date)

    def test_delete_visit(self):
        """Test deleting a Visit instance."""
        visit = self.create_visit()
        Visit.objects.filter(id=visit.id).delete()
        
        with self.assertRaises(Visit.DoesNotExist):
            Visit.objects.get(id=visit.id)
