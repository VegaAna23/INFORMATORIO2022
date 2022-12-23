from django.db import models

 
    
class Autor(models.Model):
    nombres=models.CharField('Nombres', max_length=140)
    apellidos=models.CharField('Apellidos', max_length=140)
    facebook=models.URLField('Facebook', null=True, blank=True)
    estado=models.BooleanField('Autor activo/No activo', default=True)
    fecha_creacion=models.DateField ('Fecha de Creacion',auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'
        
    def _str_(self):
        return "{0},{1}".format(self.apellidos, self.nombres)    
    
class Post(models.Model):
    id= models.AutoField(primary_key = True)
    titulo= models.CharField('Titulo', max_length=90, blank= False, null=False)
    slug= models.CharField('Slug', max_length=100, blank= False, null=False)
    contenido= models.TextField('Contenido')
    autor=models.ForeignKey('Autor', on_delete=models.CASCADE)
    estado=models.BooleanField('Autor activo/No activo', default=True)
    fecha_creacion=models.DateField ('Fecha de Creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    
    def _str_(self):
        return self.titulo
