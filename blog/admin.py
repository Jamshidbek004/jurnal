from django.contrib import admin

from blog.models import Jurnallar, Fayl_turi,Yangiliklar


# Register your models here.
@admin.register(Jurnallar)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['nomi', "slug", 'chopetilishVaqti', 'holati']
    list_filter = ['nomi', 'chopetilishVaqti', 'holati']
    prepopulated_fields = {"slug": ('nomi',)}
    search_fields = ['nomi', 'Text']
    date_hierarchy = 'chopetilishVaqti'
    ordering = ['holati', 'chopetilishVaqti']



@admin.register(Fayl_turi)
class FaylturiAdmin(admin.ModelAdmin):
    list_display = ['turi']


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ['nomi', "slug", 'chopetilishVaqti', 'holati']
    list_filter = ['nomi', 'chopetilishVaqti', 'holati']
    prepopulated_fields = {"slug": ('nomi',)}
    search_fields = ['nomi', 'Text']
    date_hierarchy = 'chopetilishVaqti'
    ordering = ['holati', 'chopetilishVaqti']