from django import views
from django.urls import path
from .views import RemeraDelete, ArticuloCreacion, RemeraDetalle, CarteraLista, VestidoLista, ZapatoLista, PantalonLista, RemeraLista, AccesorioLista, OtroLista, PantalonDetalle, AccesorioDetalle, CarteraDetalle, VestidoDetalle, ZapatoDetalle, OtroDetalle, RemeraUpdate, PantalonUpdate, AccesorioUpdate, CarteraUpdate, VestidoUpdate, ZapatoUpdate, OtroUpdate, PantalonDelete, AccesorioDelete, CarteraDelete, VestidoDelete, ZapatoDelete, OtroDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, home, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', home.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='thriftshop/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaRemeras/', RemeraLista.as_view(), name='remeras'),
    path('listaPantalones/', PantalonLista.as_view(), name='pantalones'),
    path('listaAccesorios/', AccesorioLista.as_view(), name='accesorios'),
    path('listaZapatos/', ZapatoLista.as_view(), name='zapatos'),
    path('listaVestidos/', VestidoLista.as_view(), name='vestidos'),
    path('listaCarteras/', CarteraLista.as_view(), name='carteras'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('remeraDetalle/<int:pk>/', RemeraDetalle.as_view(), name='remera'),
    path('pantalonDetalle/<int:pk>/', PantalonDetalle.as_view(), name='pantalon'),
    path('accesorioDetalle/<int:pk>/', AccesorioDetalle.as_view(), name='accesorio'),
    path('carteraDetalle/<int:pk>/', CarteraDetalle.as_view(), name='cartera'),
    path('vestidoDetalle/<int:pk>/', VestidoDetalle.as_view(), name='vestido'),
    path('zapatoDetalle/<int:pk>/', ZapatoDetalle.as_view(), name='zapato'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('remeraEdicion/<int:pk>/', RemeraUpdate.as_view(), name='remera_editar'),
    path('pantalonEdicion/<int:pk>/', PantalonUpdate.as_view(), name='pantalon_editar'),
    path('accesorioEdicion/<int:pk>/', AccesorioUpdate.as_view(), name='accesorio_editar'),
    path('carteraEdicion/<int:pk>/', CarteraUpdate.as_view(), name='cartera_editar'),
    path('vestidoEdicion/<int:pk>/', VestidoUpdate.as_view(), name='vestido_editar'),
    path('zapatoEdicion/<int:pk>/', ZapatoUpdate.as_view(), name='zapato_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),


    path('remeraBorrado/<int:pk>/', RemeraDelete.as_view(), name='remera_eliminar'),
    path('pantalonBorrado/<int:pk>/', PantalonDelete.as_view(), name='pantalon_eliminar'),
    path('accesorioBorrado/<int:pk>/', AccesorioDelete.as_view(), name='accesorio_eliminar'),
    path('carteraBorrado/<int:pk>/', CarteraDelete.as_view(), name='cartera_eliminar'),
    path('vestidoBorrado/<int:pk>/', VestidoDelete.as_view(), name='vestido_eliminar'),
    path('zapatoBorrado/<int:pk>/', ZapatoDelete.as_view(), name='zapato_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('articuloCreacion/', ArticuloCreacion.as_view(), name='nuevo'),

    path('remeraDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('pantalonDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('accesorioDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('carteraDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('zapatoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('vestidoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]
