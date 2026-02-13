from django.urls import path
from bio_data.api.views import biodata_list_create, biodata_detail
from bio_data.api.cbv_views import BiodataListCreateCBV, BiodataDetailCBV

urlpatterns = [
    path('list/', biodata_list_create, name="biodata-list"),
    path('<int:pk>/', biodata_detail, name="biodata-detail"),
    
    #class based view urls
    path('cbv/list/', BiodataListCreateCBV.as_view(), name="biodata-list-cbv"),
    path('cbv/<int:pk>/', BiodataDetailCBV.as_view(), name="biodata-detail-cbv"),
]
