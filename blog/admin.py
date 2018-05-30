from django.contrib import admin

# Register your models here.
# Estou modificando aqui para fazer um teste
from .models import Post
from .models import Aluno
from .models import Turma
from .models import TurmaAluno

admin.site.register(Post)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(TurmaAluno)
