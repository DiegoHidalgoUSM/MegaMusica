from rest_framework import viewsets
from .serializer import DiscoSerializer
from .models import Disco

# Create your views here.
class DiscoViewSet(viewsets.ModelViewSet):
    queryset = Disco.objects.order_by('ventas')[:5]
    serializer_class = DiscoSerializer