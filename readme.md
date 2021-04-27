para instalar git seguir este enlace http://git-scm.com/download/win
es un wizzard sencillo, sugiero como editor, cuando aparece vim cambiarlo a nano como sugerencia

instalacion de git flow https://github.com/nvie/gitflow/wiki/Windows


token : https://pypi.org/project/django-rest-auth-bearer/



para trabajar primero partir de la rama devel
para ingresar a la rama devel git checkout devel
se hacen los cambios
al terminar git pull
git push


generar migracion: python manage.py makemigrations paises --name creacion_paises
aplicar migracion python manage.py migrate
agregar a admin de django: admin.site.register(Pais)

class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=15)
    
    
class Pais(models.Model):
    nombre_pais = models.CharField(max_length=30, default="")
    nombre_nacionalidad = models.CharField(max_length=25, default="")
    abreviatura = models.CharField(max_length=5, default="")
    pais = models.ForeignKey(Nacionalidad, verbose_name='pais', related_name="paises", on_delete=models.PROTECT)
    