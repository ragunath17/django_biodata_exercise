from django.urls import path
from bio_data.api.views import biodata_list_create, biodata_detail
from bio_data.api.cbv_views import BiodataListCreateCBV, BiodataDetailCBV, biodata_list, biodata_detail, biodata_create
from bio_data.api.cbv_pagination_views import BiodataListCreatePaginationApiview, BiodataDetailPaginationApiview
from bio_data.api.generic_views import BiodataListCreateMixinView, BiodataRetriveUpdateDestroyMixinView

urlpatterns = [
    path('template_list/', biodata_list, name="biodata-list"),
    path('create/', biodata_create, name="biodata-create"),
    path('<int:pk>/', biodata_detail, name="biodata-detail"),
    
    #class based view urls
    path('cbv/list/', BiodataListCreateCBV.as_view(), name="biodata-list-cbv"),
    path('cbv/<int:pk>/', BiodataDetailCBV.as_view(), name="biodata-detail-cbv"),
    
    #class based view with pagination
    path('cbv-pagination/list/', BiodataListCreatePaginationApiview.as_view(), name="biodata-list-cbv-pagination"),
    path('cbv-pagination/<int:pk>/', BiodataDetailPaginationApiview.as_view(), name="biodata-detail-cbv-pagination"),
    
    #Mixins and Generic based view urls
    path('mixin/list/', BiodataListCreateMixinView.as_view(), name="biodata-list-mixin"),
    path('mixin/<int:pk>/', BiodataRetriveUpdateDestroyMixinView.as_view(), name="biodata-detail-mixin"),
    
    path('bio_data/', biodata_list, name="biodata-lists"),
    path('biodata/<int:pk>/', biodata_detail, name='biodata-detail'),
]

