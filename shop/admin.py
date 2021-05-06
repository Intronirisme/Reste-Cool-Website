from django.contrib import admin
from shop.models import Commandes, Articles, MediaContents, Accueils, Collections

# Register your models here.

@admin.register(Commandes)
class CommandesAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'facturation_adress', 'total')
    list_filter = ('order_date', 'facturation_adress', 'total')
    search_fields = ('buyer', 'facturation_adress')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'id')
    list_filter = ('price',)
    search_fields = ('name',)

@admin.register(MediaContents)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_modif', 'id')

@admin.register(Accueils)
class AccueilsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')