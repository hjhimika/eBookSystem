from django.contrib import admin


from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('email', 'fullname','status', 'is_admin', 'is_active', 'role')

  

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Role._meta.fields]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Permission._meta.fields]

