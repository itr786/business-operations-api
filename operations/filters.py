from django_filters import rest_framework as filters

from operations.models import Invoice, Project, Task


class ProjectFilter(filters.FilterSet):
    min_budget = filters.NumberFilter(field_name="budget", lookup_expr="gte")
    max_budget = filters.NumberFilter(field_name="budget", lookup_expr="lte")

    class Meta:
        model = Project
        fields = ["status", "customer"]


class TaskFilter(filters.FilterSet):
    due_before = filters.DateFilter(field_name="due_date", lookup_expr="lte")

    class Meta:
        model = Task
        fields = ["status", "project"]


class InvoiceFilter(filters.FilterSet):
    class Meta:
        model = Invoice
        fields = ["status", "customer"]
