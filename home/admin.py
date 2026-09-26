from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'service',
        'date',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'service',
        'date',
    )

    search_fields = (
        'name',
        'phone',
    )

    ordering = (
        '-created_at',
    )


from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)


    from django.contrib import admin
from .models import ClinicSettings


@admin.register(ClinicSettings)
class ClinicSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo', 'years_experience', 'patients_count', 'rating']