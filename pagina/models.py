from django.db import models

class Conteudo(models.Model):
    titulo = models.CharField(max_length=100) # título[cite: 3]
    slug = models.SlugField(unique=True) # slug[cite: 3]
    conteudo_html = models.TextField() # conteúdo HTML[cite: 3]
    ativo = models.BooleanField(default=True) # ativo[cite: 3]

    def __str__(self):
        return self.titulo

class Menu(models.Model):
    TIPO_DESTINO = [
        ('interno', 'Conteúdo interno'), # Conteúdo interno
        ('externo', 'Link externo') # Link externo[cite: 4]
    ]
    
    titulo = models.CharField(max_length=100) # título[cite: 4]
    tipo_destino = models.CharField(max_length=10, choices=TIPO_DESTINO) # tipo de destino[cite: 4]
    ordem = models.IntegerField(default=0) # ordem[cite: 4]
    ativo = models.BooleanField(default=True) # ativo[cite: 4]
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE, null=True, blank=True) # relacionamento com Conteudo[cite: 4]
    url_externa = models.URLField(blank=True, null=True) # URL externa[cite: 4]

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo