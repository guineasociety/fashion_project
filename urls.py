from django.urls import path, include
from . import views

urlpatterns = (

    # Les Accueils
    path('accueil/', views.accueil, name='accueil'),

    # ============= MESURE DETAIL ============

    path('add_mesure/', views.add_mesure, name='add_mesure'),
    path('list_mesure/', views.list_mesure, name='list_mesure'),

    path('detail_mesure/<str:pk>', views.detail_mesure, name='detail_mesure'),
    path('update_mesure/<str:pk>', views.update_mesure, name='update_mesure'),
    path('delete_mesure/<str:pk>', views.delete_mesure, name='delete_mesure'),


    # Les Listes
    path('list_employe/', views.list_employe, name='list_employe'),
    path('list_charge/', views.list_charge, name='list_charge'),
    path('list_finance/', views.list_finance, name='list_finance'),


    # Les détails
    path('detail_charge/<str:pk>', views.detail_charge, name='detail_charge'),
    path('detail_employe/<str:pk>', views.detail_employe, name='detail_employe'),


    # Les Mises à jour

    path('update_charge/<str:pk>', views.update_charge, name='update_charge'),
    path('update_employe/<str:pk>', views.update_employe, name='update_employe'),

    # Les Ajouts

    path('add_charge/', views.add_charge, name='add_charge'),
    path('add_employe/', views.add_employe, name='add_employe'),

    # Les suppressions
    path('delete_employe/<str:pk>', views.delete_employe, name='delete_employe'),
    path('delete_charge/<str:pk>', views.delete_charge, name='delete_charge'),

)