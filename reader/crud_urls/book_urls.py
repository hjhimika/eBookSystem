
from django.urls import path

from reader.crud_views import book_crud as views


urlpatterns = [
	path('api/v1/book/all/', views.getAllBook),

	path('api/v1/book/without_paginaiton/all/', views.getAllBookWithoutPagination),

	path('api/v1/book/<int:pk>', views.getABook),

	path('api/v1/book/search/', views.searchBook),
	
	path('api/v1/book/create/', views.createBook),

	path('api/v1/book/update/<int:pk>', views.updateBook),

	path('api/v1/book/delete/<int:pk>', views.deleteBook),
 
]
