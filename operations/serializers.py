from rest_framework import serializers
from .models import Customer, Invoice, Project, Task


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "id", "name", "email", "active", "created_at"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "id", "name", "customer", "status", "budget", "created_at"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "id", "project", "title", "status", "due_date"


class InvoiceSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Invoice
        fields = "id", "customer", "number", "subtotal", "tax", "total", "status", "issued_at"
