import pytest
from operations.models import Customer, Invoice


@pytest.mark.django_db
def test_invoice_total_is_subtotal_plus_tax():
    customer = Customer.objects.create(name="Example Co", email="billing@example.com")
    invoice = Invoice.objects.create(customer=customer, number="INV-1001", subtotal="100.00", tax="18.00")
    assert invoice.total == 118
