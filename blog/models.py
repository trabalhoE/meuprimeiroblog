
from django.db import models
from django.utils import timezone

# Create your models here.
# Estou modificando aqui para testar

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


class Aluno(models.Model):
    matricula=models.CharField(max_length=12,primary_key=True)
    nome=models.CharField(max_length=32)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    id=models.CharField(max_length=3,primary_key=True)
    ano=models.IntegerField(max_length=4)

    def __str__(self):
        return str(self.id)+"-"+str(self.ano)


class TurmaAluno(models.Model):
    cod=models.ForeignKey(Turma)
    aluno=models.ForeignKey(Aluno)

    def __str__(self):
        return str(self.cod)+" - "+str(self.aluno)
