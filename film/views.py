from rest_framework import viewsets

class UserWineViewSet(viewsets.ModelViewSet):
    queryset = WineUser.objects.all()
    model = WineUser
    serializer_class = UserWineSerializer