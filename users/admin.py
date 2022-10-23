from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    # fieldsets과 fields 의 차이점은 fieldsets은 세션을 만들 수 있다.
    fieldsets = (
        ("profile", 
        {
            "fields": ("username", "password", "name", "email", "is_host"),
            "classes": ("wide",),
            },
        ),
        (
            "Important Dates",
            {
                "fields":("last_login", "date_joined", ),
                "classes":("collapse",), 
            },
        ),
    )

    # fields = ("email", "password", "name")
    
    list_display =  ("username", "email", "name", "is_host")



