from django.contrib import admin


from .models import Category, Chicken, Drinks, Hamburger, Hotdog, Potato, RegularPizza, SicilianPizza, Toppings, Pasta, Salad, UserOrder, SavedCarts
from tinymce.widgets import TinyMCE
from django.db import models

class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class RegularPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class SicilianPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }


admin.site.register(Category,CategoryAdmin)
admin.site.register(RegularPizza, RegularPizzaAdmin)
admin.site.register(SicilianPizza, SicilianPizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Hotdog)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Hamburger)  
admin.site.register(Potato)
admin.site.register(Chicken)
admin.site.register(Drinks)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
