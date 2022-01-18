"""User admin classes"""
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """profile admin."""
    # variables a mostras
    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    # variables con link
    list_display_links = ('pk','user')
    # variables editables
    list_editable = ('phone_number',)
    # agregar busqueda
    search_fields = ('user__email','user__username','user__first_name','user__last_name')
    # filtros
    list_filter = ('modified','user__is_active')

    # variables de admin
    fieldsets = (
        ('Profile',{
            'fields':(('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website'),
                ('phone_number'),
                ('biography')
            ),
            'classes': ('wide','extrapretty'),
        }),
        ('Metadata',{
            'fields': (('created','modified'),)
        })
    )
    # detalles no editables
    readonly_fields = ('created','modified', 'user')

# adding the admin to the profile

class ProfileInLine(admin.StackedInline):
    """Profile in line admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    """Add porfile admin to base user admin"""
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
