from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from buku.models import ModelAuthor
from buku.serializers import ModelAuthorSerial, ModelBookSerial

# Create Your Views
class AuthorCollection(APIView):
  """
  List All Author or Insert Author
  """
  def get(self, request):
    """
    Return All Author
    """
    return Response("Hallo, Author", status=status.HTTP_200_OK)
  
  def post(self, request):
    """
    Insert Author to Table Author
    """
    serializer = ModelAuthorSerial(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class BookCollection(APIView):
  def get(self, request):
    """
    Return All Book
    """
    return Response("Hallo, Book !", status=status.HTTP_200_OK)
  
  def post(self, request):
    """
    """
    serializer = ModelBookSerial(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)