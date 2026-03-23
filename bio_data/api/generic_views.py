from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from bio_data.api.serializers import BiodataSerializer
from bio_data.models import BioData

class BiodataListCreateMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = BioData.objects.all()
    serializer_class = BiodataSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class BiodataRetriveUpdateDestroyMixinView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                                      mixins.DestroyModelMixin, GenericAPIView):
    queryset = BioData.objects.all()
    serializer_class = BiodataSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
