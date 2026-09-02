from rest_framework import filters, viewsets
from .models import Customer, Invoice, Project, Task
from .serializers import CustomerSerializer, InvoiceSerializer, ProjectSerializer, TaskSerializer


class SearchableViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)


class CustomerViewSet(SearchableViewSet):
    queryset = Customer.objects.all().order_by("name")
    serializer_class = CustomerSerializer
    search_fields = ("name", "email")


class ProjectViewSet(SearchableViewSet):
    queryset = Project.objects.select_related("customer").all().order_by("-created_at")
    serializer_class = ProjectSerializer
    search_fields = ("name", "customer__name")


class TaskViewSet(SearchableViewSet):
    queryset = Task.objects.select_related("project").all().order_by("due_date")
    serializer_class = TaskSerializer
    search_fields = ("title", "status")


class InvoiceViewSet(SearchableViewSet):
    queryset = Invoice.objects.select_related("customer").all().order_by("-issued_at")
    serializer_class = InvoiceSerializer
    search_fields = ("number", "status", "customer__name")
