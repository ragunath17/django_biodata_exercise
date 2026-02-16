from rest_framework.pagination import PageNumberPagination
# from rest_framework.pagination import LimitOffsetPagination

class BiodataPaginationCBV(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    max_page_size = 100
    
    