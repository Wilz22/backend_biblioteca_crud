from django.db import models

# Modelo Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
# Modelo Categoria
class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cat
    
# Modelo Editorial
class Editorial(models.Model):
    nombre_edi = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_edi
    
# Modelo Libro
class Libro(models.Model):
    nombre_libro = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_libro
