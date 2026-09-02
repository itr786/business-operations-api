from decimal import Decimal

from django.db import transaction

from operations.models import Invoice


@transaction.atomic
def calculate_invoice(invoice: Invoice) -> Decimal:
    """Return the authoritative invoice total from persisted monetary fields."""
    return invoice.subtotal + invoice.tax


@transaction.atomic
def mark_issued(invoice: Invoice) -> Invoice:
    if invoice.status != "draft":
        raise ValueError("Only draft invoices can be issued")
    invoice.status = "issued"
    invoice.save(update_fields=["status"])
    return invoice


@transaction.atomic
def mark_paid(invoice: Invoice) -> Invoice:
    if invoice.status not in {"issued", "overdue"}:
        raise ValueError("Only issued invoices can be marked paid")
    invoice.status = "paid"
    invoice.save(update_fields=["status"])
    return invoice
