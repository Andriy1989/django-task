from .models import User,Goods
from rest_framework import viewsets
from .serializers import UserSerializer, GoodsSerializer
from rest_framework import generics
from datetime import datetime
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class GoodsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    
    
class UserDateViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    serializer_class = UserSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        date = datetime.strptime(self.kwargs['date'], "%Y-%m-%d")
        
        
        return User.objects.filter(RegistrationDate=date)