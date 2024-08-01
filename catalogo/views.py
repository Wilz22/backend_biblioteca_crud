from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Autor, Categoria, Editorial, Libro
from .serializers import AutorSerializer, CategoriaSerializer, EditorialSerializer, LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        id_autor = self.request.query_params.get('autor', None)
        id_categoria = self.request.query_params.get('categoria', None)
        id_editorial = self.request.query_params.get('editorial', None)
        
        if id_autor:
            queryset = queryset.filter(autor_id=id_autor)
        if id_categoria:
            queryset = queryset.filter(categoria_id=id_categoria)
        if id_editorial:
            queryset = queryset.filter(editorial_id=id_editorial)
        
        return queryset

    @action(detail=False, methods=['get'])
    def libros_por_autor(self, request):
        autor_id = request.query_params.get('autor_id')
        if not autor_id:
            return Response({'error': 'autor_id parameter is required'}, status=400)
        libros = self.get_queryset().filter(autor_id=autor_id)
        serializer = self.get_serializer(libros, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def libros_por_categoria(self, request):
        id_categoria = request.query_params.get('id_categoria')
        if not id_categoria:
            return Response({'error': 'id_categoria parameter is required'}, status=400)
        libros = self.get_queryset().filter(categoria_id=id_categoria)
        serializer = self.get_serializer(libros, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def libros_por_editorial(self, request):
        id_editorial = request.query_params.get('id_editorial')
        if not id_editorial:
            return Response({'error': 'id_editorial parameter is required'}, status=400)
        libros = self.get_queryset().filter(editorial_id=id_editorial)
        serializer = self.get_serializer(libros, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def autores_por_categoria(self, request):
        id_categoria = request.query_params.get('id_categoria')
        if not id_categoria:
            return Response({'error': 'id_categoria parameter is required'}, status=400)
        libros = self.get_queryset().filter(categoria_id=id_categoria).values_list('autor_id', flat=True).distinct()
        autores = Autor.objects.filter(id__in=libros)
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)
