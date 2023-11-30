from django.contrib.auth import get_user_model
from django.db import models

class FavoriteItem(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=None,
    )
    text = models.TextField()
    algorithm = models.CharField(max_length=100, default='AES')
    custom_key = models.BooleanField(default=False)

    def __str__(self):
        return self.text
