from rest_framework import serializers
from bookstore.models import Book, Author, Publisher


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'price', 'popularity']

class BookDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class AuthorDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class PublisherDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

