from ast import Return

from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter

from common.pagination import Pagination
from reader.models import Book
from reader.serializers import BookListSerializer, BookSerializer





# Create your views here.

@extend_schema(
     parameters=[
          OpenApiParameter("page"),
          OpenApiParameter("size"),
  ],
     request=BookSerializer,
     responses=BookSerializer
)
@api_view(['GET'])

def getAllBook(request):
     books = Book.objects.all()
     total_elements = books.count()

     page = request.query_params.get('page')
     size = request.query_params.get('size')

     # Pagination
     pagination = Pagination()
     pagination.page = page
     pagination.size = size
     books = pagination.paginate_data(books)

     serializer = BookListSerializer(books, many=True)

     response = {
          'books': serializer.data,
          'page': pagination.page,
          'size': pagination.size,
          'total_pages': pagination.total_pages,
          'total_elements': total_elements,
     }

     return Response(response, status=status.HTTP_200_OK)




@extend_schema(
     request=BookSerializer,
     responses=BookSerializer
)
@api_view(['GET'])

def getAllBookWithoutPagination(request):
    books = Book.objects.all()

    serializer = BookListSerializer(books, many=True)

    response = {
        'books': serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)





@extend_schema(request=BookSerializer, responses=BookSerializer)
@api_view(['GET'])

def getABook(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookListSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({'detail': f"Book id - {pk} doesn't exist"})




@extend_schema(request=BookSerializer, responses=BookSerializer)
@api_view(['GET'])

def searchBook(request):
     key = request.query_params.get('key')
     if key:
          books = Book.objects.filter(Q(title__icontains=key)|Q(author__icontains=key))
     else:
          return Return({'detail': "Please enter 'title' or 'author'to search"}, status=status.HTTP_400_BAD_REQUEST)

     total_elements = books.count()

     page = request.query_params.get('page')
     size = request.query_params.get('size')

     # Pagination
     pagination = Pagination()
     pagination.page = page
     pagination.size = size
     books = pagination.paginate_data(books)

     serializer = BookListSerializer(books, many=True)

     response = {
          'books': serializer.data,
          'page': pagination.page,
          'size': pagination.size,
          'total_pages': pagination.total_pages,
          'total_elements': total_elements,
     }

     if len(books) > 0:
          return Response(response, status=status.HTTP_200_OK)
     else:
          return Response({'detail': f"There are no Books matching your search"}, status=status.HTTP_400_BAD_REQUEST)



          
@extend_schema(request=BookSerializer, responses=BookSerializer)
@api_view(['POST'])

def createBook(request):
    data = request.data

    filtered_data = {}

        
    for key, value in data.items():
        if value != '' and value != '0' and value != 0 and value != 'undefined':
            filtered_data[key] = value


    serializer = BookSerializer(data=filtered_data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@extend_schema(request=BookSerializer, responses=BookSerializer)
@api_view(['PUT'])

def updateBook(request,pk):
    data = request.data
    restricted_values = ('', 'undefined', '0', 0, ' ')
    
    filtered_data = {}

    for key, value in data.items():
        if value not in restricted_values:
            filtered_data[key] = value

    try:
        book = Book.objects.get(pk=int(pk))
    except ObjectDoesNotExist:
        return Response({'detail': f"book id - {pk} doesn't exists"})


    serializer = BookSerializer(book, data=filtered_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)
    




@extend_schema(request=BookSerializer, responses=BookSerializer)
@api_view(['DELETE'])

def deleteBook(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({'detail': f'Book id - {pk} is deleted successfully'})
    except ObjectDoesNotExist:
        return Response({'detail': f"Book id - {pk} doesn't exists"})
