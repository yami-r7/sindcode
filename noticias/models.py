from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return f"Categoria [nome={self.nome}]"


class Autor(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)
    perfil = models.TextField()

    def __str__(self):
        return self.nome + self.perfil


class Noticia(models.Model):
    titulo = models.CharField(max_length=90, null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    # Define a data e hora na criação do objeto, útil para publicações
    data_publicacao = models.DateTimeField(auto_now_add=True)
    destaque = models.CharField(
        max_length=2,
        choices=[
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')  # <--- MUST BE ADDED TO CHOICES
        ],
        default='5',  # <--- DEFAULT VALUE SET HERE
        null=False,
        blank=False
    )
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=False)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,  # Se o Autor for deletado, todas as suas notícias também serão.
        related_name='noticias_autor',  # Nome do relacionamento reverso (autor.noticias.all())
        null=False,  # criar campo autor_id
    )
    # relacionamento de 1:N
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,  # Se a Categoria for deletada, todas as notícias dessa categoria também serão.
        related_name='noticias_categoria',  # Nome do relacionamento reverso (categoria.noticias.all())
        null=False,  # criar campo categoria_id
    )

    def __str__(self):
        return self.titulo
# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
