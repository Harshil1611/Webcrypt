# import os
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.db import models


# # chat attachment path for conversations
# def chat_att_path():
#     return os.path.join(settings.BASE_DIR, 'media')


# # Create your models here.
# class Users(models.Model):
#     # name = models.CharField(max_length=100, null=False)
#     # username = models.CharField(max_length=25, null=False)
#     # email = models.EmailField(max_length=254, null=False)
#     # password = models.CharField(max_length=100, null=False)
#     p_pic = models.ImageField(upload_to='static', blank=True)
#     p_desc = models.CharField(max_length=1000, blank=True)
#     own_comp = models.BooleanField(default=False, blank=True)
#     comp_name = models.CharField(max_length=100, blank=True)
#     Fr_list = models.FileField(upload_to=settings.JSON_DIR, blank=True)
#     Client_list = models.FileField(upload_to=settings.JSON_CLIENT_DIR, blank=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#
# class Chat(models.Model):
#     comp = models.BooleanField(default=False)
#     comp_id = models.IntegerField()
#     F_usr = models.IntegerField()
#     T_usr = models.IntegerField()
#     date = models.DateTimeField()
#     data = models.CharField(max_length=1000)
#     file = models.FileField(upload_to=settings.MEDIA_DIR, blank=True)  # can be image,video anything