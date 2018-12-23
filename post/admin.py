from django.contrib import admin
from .models import yazi

# Register your models here.



class adminYazi(admin.ModelAdmin):
    list_display = ["başlık","yayinTarihi"]
    list_display_links = ["yayinTarihi"]
    list_filter = ["yayinTarihi"]
    search_fields = ["başlık","metin"]
    list_editable = ["başlık"]
    class Meta:
        model = yazi


admin.site.register(yazi,adminYazi)