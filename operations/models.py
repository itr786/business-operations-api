from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=180)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="projects")
    status = models.CharField(max_length=30, default="active")
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=30, default="todo")
    due_date = models.DateField(null=True, blank=True)


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="invoices")
    number = models.CharField(max_length=40, unique=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=30, default="draft")
    issued_at = models.DateField(null=True, blank=True)

    @property
    def total(self):
        return self.subtotal + self.tax
