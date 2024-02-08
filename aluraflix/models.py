from django.db import models

class Programa(models.Model):
    """
    Modelo que representa um programa de televisão, filme ou série.

    Atributos:
        titulo (CharField): O título do programa, limitado a 50 caracteres.
        tipo (CharField): O tipo do programa, escolhido entre 'Filme' ou 'Série'.
        data_lancamento (DateField): A data de lançamento do programa.
        likes (PositiveIntegerField): O número de curtidas que o programa recebeu, padrão é 0.
        dislikes (PositiveIntegerField): O número de descurtidas que o programa recebeu, padrão é 0.
    """

    TIPO = (
        ('F', 'Filme'), 
        ('S', 'Série'),
    )

    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False, default='F')
    data_lancamento = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Retorna a representação de string do programa.

        Retorna:
            str: O título do programa.
        """
        return self.titulo
