# # cookbook/schema.py
# import graphene
# from graphene_django import DjangoObjectType

# from .models import Category, Ingredient

# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = ("id", "name", "ingredients")

# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
#         fields = ("id", "name", "notes", "category")

# class Query(graphene.ObjectType):
#     all_ingredients = graphene.List(IngredientType)
#     category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

#     def resolve_all_ingredients(root, info):
#         # We can easily optimize query count in the resolve method
#         return Ingredient.objects.select_related("category").all()

#     def resolve_category_by_name(root, info, name):
#         try:
#             return Category.objects.get(name=name)
#         except Category.DoesNotExist:
#             return None

# schema = graphene.Schema(query=Query)




# file upload
import graphene
from graphene_file_upload.scalars import Upload
from .models import ProductImage
class Query(graphene.ObjectType):
    ok = graphene.Boolean(default_value=True)

class MyUpload(graphene.Mutation):
    class Arguments:
        file_in = Upload()

    ok = graphene.Boolean()

    def mutate(self, info, file_in):
        ProductImage.objects.create(image = file_in)
        return MyUpload(ok=True)

class Mutation(graphene.ObjectType):
    my_upload = MyUpload.Field()

schema = graphene.Schema(query=Query, mutation=Mutation, types=[])