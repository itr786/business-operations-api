from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, InvoiceViewSet, ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register("customers", CustomerViewSet)
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)
router.register("invoices", InvoiceViewSet)

urlpatterns = router.urls
