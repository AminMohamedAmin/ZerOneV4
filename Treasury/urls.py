from django.urls import path
from .views import *

app_name ="Treasury"
urlpatterns = [
    path('list/', TreasuryList.as_view(), name="TreasuryList"),
    path('trach/', TreasuryTrachList.as_view(), name="TreasuryTrachList"),
    path('create/', TreasuryCreate.as_view(), name="TreasuryCreate"),
    path('create/<int:pk>/', TreasuryUpdate.as_view(), name="TreasuryUpdate"),
    path('delete/<int:pk>', TreasuryDelete.as_view(), name="TreasuryDelete"),
    path('restore/<int:pk>', TreasuryRestore.as_view(), name="TreasuryRestore"),
    path('superDelete/<int:pk>', TreasurySuperDelete.as_view(), name="TreasurySuperDelete"),

]