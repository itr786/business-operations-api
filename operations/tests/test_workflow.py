from decimal import Decimal

from django.test import TestCase

from operations.models import Customer, Project, Task
from operations.services.invoicing import mark_issued, mark_paid
from operations.services.workflow import change_project_status, complete_task


class WorkflowTests(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Acme", email="ops@example.com")
        self.project = Project.objects.create(name="Website", customer=customer, status="planned", budget=Decimal("12000"))
        self.task = Task.objects.create(project=self.project, title="Build API", status="in_progress")

    def test_project_transition(self):
        change_project_status(self.project, "active")
        self.project.refresh_from_db()
        self.assertEqual(self.project.status, "active")

    def test_invalid_project_transition_is_rejected(self):
        with self.assertRaises(ValueError):
            change_project_status(self.project, "completed")

    def test_task_can_be_completed(self):
        complete_task(self.task)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, "done")

    def test_invoice_lifecycle(self):
        from operations.models import Invoice
        invoice = Invoice.objects.create(customer=self.project.customer, number="INV-1001", subtotal=Decimal("100"), tax=Decimal("18"))
        mark_issued(invoice)
        mark_paid(invoice)
        invoice.refresh_from_db()
        self.assertEqual(invoice.status, "paid")
