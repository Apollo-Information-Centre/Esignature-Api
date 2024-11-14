from django.contrib import admin

# Register your models here.
from .models import Document, Signature

# Register Document model to the admin interface
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')  # Fields to display in the list view
    search_fields = ('title',)  # Search functionality on the title field
    list_filter = ('uploaded_at',)  # Filter by the uploaded date

admin.site.register(Document, DocumentAdmin)

# Register Signature model to the admin interface
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('document', 'user', 'signed_at')  # Fields to display in the list view
    search_fields = ('document__title', 'user__username')  # Search functionality on document title and user
    list_filter = ('signed_at', 'user')  # Filter by the signing date and user

admin.site.register(Signature, SignatureAdmin)