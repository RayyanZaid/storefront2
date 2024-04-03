from rest_framework import serializers
from .models import Product, Collection


from decimal import Decimal


# class CollectionSerializer(serializers.Serializer):

#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



# Completely separate from the product class

# Using this, we can go from (Product Object) --> Python Dictionary
# class ProductSerializer(serializers.Serializer):

#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')

#     # Add a custom serializer

#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

#     def calculate_tax(self, product : Product):

#                       # decimal           # float
#         return round(product.unit_price * Decimal(1.1),2)


#     # 3 ways to include related objects

#     # 1) PrimaryKeyRelatedField
#     # include pk (id) of each collection in Product object
#     # collection = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all()
#     # )

#     # 2) StringRelatedField - returns the string representation of the object
#     # need to include .selectrelated('collection') in the views
#     # collection = serializers.StringRelatedField()

#     # 3) Use the serializer class of that object

#     # collection = CollectionSerializer()

#     # 4) Use HyperLink

#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name = 'collection-detail'
#     )


# Model Serializer - don't have to redefine all the fields since they're already in the models.py
    
class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection

        fields = ['id' , 'title']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product

        # Django will auto create serializer
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']

    
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product : Product):

                    # decimal           # float
        return round(product.unit_price * Decimal(1.1),2)
    

    # override the validate method in the serializer

    def validate(self, data):

        if data['unit_price'] < 2:
            return serializers.ValidationError('Unit Price is less than $2')
        
        return data