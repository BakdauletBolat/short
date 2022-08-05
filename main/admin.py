from django.contrib import admin
from .models import Url, View


class URLAdmin(admin.ModelAdmin):

    def get_views(self,obj):
        print(obj)
        return len(obj.views.all())



    list_display = ('original_url','creation_date','get_views')

admin.site.register(Url,URLAdmin)

admin.site.register(View)