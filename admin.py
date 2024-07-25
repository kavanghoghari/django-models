from django.contrib import admin
from core.models import Product, CartOrder, CartOrderItem, Category, Vendor, ProductImage, Wishlist

# Inline for ProductImages to allow adding/editing product images directly within the Product admin page
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1  # Allows adding one extra blank inline form

# Custom admin class for the Product model
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]  # Attach the inline admin to the Product admin
    list_display = ['title', 'product_image', 'price', 'product_status', 'in_stock']  # Fields to display in the list view
    search_fields = ['title', 'description']  # Fields to search by
    list_filter = ['product_status', 'in_stock', 'category']  # Filters for the right sidebar
    list_editable = ['price', 'product_status', 'in_stock']  # Fields editable directly in the list view

# Custom admin class for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']  # Fields to display in the list view
    search_fields = ['title']  # Fields to search by

# Custom admin class for the Vendor model
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']  # Fields to display in the list view
    search_fields = ['title', 'address']  # Fields to search by

# Custom admin class for the CartOrder model
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'product_status']  # Fields to display in the list view
    search_fields = ['user__email']  # Fields to search by (search by user's email)
    list_filter = ['paid_status', 'product_status']  # Filters for the right sidebar

# Custom admin class for the CartOrderItem model
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_status', 'item', 'image', 'qty', 'price', 'total']  # Fields to display in the list view
    search_fields = ['order__user__email', 'item']  # Fields to search by (search by user's email and item name)
    list_filter = ['product_status']  # Filters for the right sidebar

# Custom admin class for the Wishlist model
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']  # Fields to display in the list view
    search_fields = ['user__email', 'product__title']  # Fields to search by (search by user's email and product title)

# Registering the models with their custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemAdmin)
admin.site.register(Wishlist, WishlistAdmin)
