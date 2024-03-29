from django.contrib import admin
from core.models import Speaker, Contact, Talk

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class TalkInline(admin.TabularInline):
    model = Talk
    extra = 2

class SpeakerInline(admin.TabularInline):
    model = Speaker
    extra = 3

class TalkAdmin(admin.ModelAdmin):
#    inlines = [SpeakerInline, ContactInline, ]
    prepopulated_fields = {'title': ('description', )}


class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInline, TalkInline, ]
    prepopulated_fields = {'slug': ('name', )}
    
admin.site.register(Speaker, SpeakerAdmin )
admin.site.register(Talk, TalkAdmin )

