from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Visit

class VisitTests(BaseTestCase):
    def test_create_visit(self):
        print("######################################")
        print("VISIT TESTING")
        print("-------------- create visit --------------")
        visit = self.create_visit()
        self.assertEqual(visit.description, "Regular checkup")
        self.assertEqual(str(visit.visit_date), "2024-01-01")

    def test_read_visit(self):
        print("-------------- read visit --------------")
        visit = self.create_visit()
        read_visit = Visit.objects.get(id=visit.id)
        self.assertEqual(read_visit.description, visit.description)
        self.assertEqual(read_visit.pet.id, visit.pet.id)

    def test_update_visit(self):
        print("-------------- update visit --------------")
        DESCRIPTION = "Emergency visit"
        VISIT_DATE = "2024-02-15"
        visit = self.create_visit()
        
        Visit.objects.filter(id=visit.id).update(
            description=DESCRIPTION,
            visit_date=VISIT_DATE
        )
        
        visit.refresh_from_db()
        self.assertEqual(visit.description, DESCRIPTION)
        self.assertEqual(str(visit.visit_date), VISIT_DATE)

    def test_delete_visit(self):
        print("-------------- delete visit --------------")
        visit = self.create_visit()
        Visit.objects.filter(id=visit.id).delete()
        
        with self.assertRaises(Visit.DoesNotExist):
            Visit.objects.get(id=visit.id)
