from rest_framework import serializers
from todoapp.models import *

class TodolistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolists
        fields = ('id','name', 'creation_date','user')

class TodoitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitems
        fields = ('id','description', 'completed','todolist', 'due_by')



# from django.contrib.auth import update_session_auth_hash
# from rest_framework import serializers
#
# from .models import Account
#
#
# class AccountSerializer(serializers.ModelSerializer):
#        password = serializers.CharField(write_only=True, required=True)
#        confirm_password = serializers.CharField(write_only=True, required=True)
#        class Meta:
#                 model = Account
#                 fields = (
#                     'id', 'email', 'username', 'date_created', 'date_modified',
#                     'firstname', 'lastname', 'password', 'confirm_password')
#                 read_only_fields = ('date_created', 'date_modified')
#
#        def create(self, validated_data):
#                 return Account.objects.create_user(**validated_data)
#
#        def update(self, instance, validated_data):
#                 instance.email = validated_data.get('email', instance.email)
#                 instance.username = validated_data.get('username',
#                                                        instance.username)
#                 instance.firstname = validated_data.get('firstname',
#                                                         instance.firstname)
#                 instance.lastname = validated_data.get('lastname',
#                                                        instance.lastname)
#
#                 password = validated_data.get('password', None)
#                 confirm_password = validated_data.get('confirm_password', None)
#
#                 if password and password == confirm_password:
#                     instance.set_password(password)
#
#                 instance.save()
#                 return instance
#
#        def validate(self, data):
#                 '''
#                 Ensure the passwords are the same
#                 '''
#                 if data['password']:
#                     print "Here"
#                     if data['password'] != data['confirm_password']:
#                         raise serializers.ValidationError(
#                             "The passwords have to be the same"
#                         )
#                 return data
#
#


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     email = serializers.EmailField()
#     db_folder = serializers.CharField(required=False)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.db_folder = validated_data.get('db_folder', instance.db_folder)
#         instance.save()
#         return instance