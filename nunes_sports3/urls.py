from django.urls import path

from .views import (ProductCreateView, ProductDeleteView, ProductListView,
                    ProductUpdateView)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

from django.urls import include, path

urlpatterns = [
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
]

