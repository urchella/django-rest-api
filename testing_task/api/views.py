from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
# from django.shortcuts import render
# from rest_framework import generics
from .models import Breeds, Cats
from .serializers import CatsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes=(IsOwnerOrReadOnly, )

    @action(methods=['get'],detail=False)
    def breed(self,request):
        breeds= Breeds.objects.all()
        return Response({'breeds':[b.breed for b in breeds]})
    

# class CatsApiCreateListView(generics.ListCreateAPIView):
#     queryset = Cats.objects.all()
#     serializer_class = CatsSerializer

# class CatsApiView(APIView):
#     def put(self,request,*args,**kwargs):
#         pk=kwargs.get('pk',None)
#         if not pk:
#             return Response({'error':'Method PUT not allowed'})
#         try:
#             instance = Cats.objects.get(pk=pk)
#         except:
#             return Response({'error':'Object does not exist'})
#         serializer=CatsSerializer(data=request.data,instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post':serializer.data})
    
#     def delete(self, request, pk):
#         try:
#             cat = Cats.objects.get(pk=pk)
#         except Cats.DoesNotExist:
#             return Response({'error': 'Cat not found'})

#         serializer = CatsSerializer()
#         serializer.delete(cat)

#         return Response({'message': 'Cat deleted successfully'})