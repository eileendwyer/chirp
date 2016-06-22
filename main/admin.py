from django.contrib import admin
from main.models import Chirp, StopWord

# Register your models here.
class ChirpAdmin(admin.ModelAdmin):
    list_display = ["body", "bird"]
    search_fields = ["body"]

admin.site.register(Chirp, ChirpAdmin)

class StopWordAdmin(admin.ModelAdmin):
    list_display = ["word"]
    search_fields = ["word"]
# list display negates need for __str__
admin.site.register(StopWord, StopWordAdmin)
