from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lis_app.views import (
    MessageHeadersViewset,
    PatientViewset,
    SpecimenViewset,
    LabOrderViewset,
    ObservationViewset,
    OrderViewset,
    DpdViewset
)

router = DefaultRouter()
router.register(r"messageheaders", MessageHeadersViewset)
router.register(r"patients", PatientViewset)
router.register(r"specimens", SpecimenViewset)
router.register(r"laborders", LabOrderViewset)
router.register(r"observations", ObservationViewset)
router.register(r"orders", OrderViewset)
router.register(r"dpd", DpdViewset)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
