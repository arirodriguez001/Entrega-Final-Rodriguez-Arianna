from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Articulo, Comentario
from .forms import ActualizacionArticulo, FormularioCambioPassword, FormularioEdicion, FormularioNuevoArticulo, FormularioRegistroUsuario, FormularioComentario


class home(LoginRequiredMixin, TemplateView):
    template_name = 'thriftshop/home.html'

class LoginPagina(LoginView):
    template_name = 'thriftshop/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'thriftshop/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'thriftshop/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'thriftshop/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'thriftshop/passwordExitoso.html', {})


# REMERA

class RemeraLista(LoginRequiredMixin, ListView):
    context_object_name = 'remeras'
    queryset = Articulo.objects.filter(articulo__startswith='remera')
    template_name = 'thriftshop/listaRemeras.html'
    login_url = '/login/'

class RemeraDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = 'remera'
    template_name = 'thriftshop/remeraDetalle.html'

class RemeraUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ActualizacionArticulo
    success_url = reverse_lazy('remeras')
    context_object_name = 'remeras'
    template_name = 'thriftshop/remeraEdicion.html'

class RemeraDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('remeras')
    context_object_name = 'remera'
    template_name = 'thriftshop/remeraBorrado.html'

# PANTALON

class PantalonLista(LoginRequiredMixin, ListView):
    context_object_name = 'pantalones'
    queryset = Articulo.objects.filter(articulo__startswith='pantalon')
    template_name = 'thriftshop/listaPantalones.html'

class PantalonDetalle(LoginRequiredMixin,DetailView):
    model = Articulo
    context_object_name = 'pantalon'
    template_name = 'thriftshop/pantalonDetalle.html'

class PantalonUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ActualizacionArticulo
    success_url = reverse_lazy('pantalones')
    context_object_name = 'pantalon'
    template_name = 'thriftshop/pantalonEdicion.html'

class PantalonDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('pantalones')
    context_object_name = 'pantalon'
    template_name = 'thriftshop/pantalonBorrado.html'

# ACCESORIO

class AccesorioLista(LoginRequiredMixin, ListView):
    context_object_name = 'accesorios'
    queryset = Articulo.objects.filter(articulo__startswith='accesorio')
    template_name = 'thriftshop/listaAccesorios.html'

class AccesorioDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = 'accesorio'
    template_name = 'thriftshop/accesorioDetalle.html'

class AccesorioUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ActualizacionArticulo
    success_url = reverse_lazy('accesorios')
    context_object_name = 'accesorio'
    template_name = 'thriftshop/accesorioEdicion.html'

class AccesorioDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('accesorios')
    context_object_name = 'accesorio'
    template_name = 'thriftshop/accesorioBorrado.html'

# CARTERA

class CarteraLista(LoginRequiredMixin, ListView):
    context_object_name = 'carteras'
    queryset = Articulo.objects.filter(articulo__startswith='cartera')
    template_name = 'thriftshop/listaCarteras.html'

class CarteraDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = 'cartera'
    template_name = 'thriftshop/carteraDetalle.html'

class CarteraUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ActualizacionArticulo
    success_url = reverse_lazy('carteras')
    context_object_name = 'cartera'
    template_name = 'thriftshop/carteraEdicion.html'

class CarteraDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('carteras')
    context_object_name = 'cartera'
    template_name = 'thriftshop/carteraBorrado.html'

# VESTIDO

class VestidoLista(LoginRequiredMixin, ListView):
    context_object_name = 'vestidos'
    queryset = Articulo.objects.filter(articulo__startswith='vestido')
    template_name = 'thriftshop/listaVestidos.html'

class VestidoDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = 'vestido'
    template_name = 'thriftshop/vestidoDetalle.html'

class VestidoUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ActualizacionArticulo
    success_url = reverse_lazy('vestidos')
    context_object_name = 'vestido'
    template_name = 'thriftshop/vestidoEdicion.html'

class VestidoDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('vestidos')
    context_object_name = 'vestido'
    template_name = 'thriftshop/vestidoBorrado.html'

# ZAPATO

class ZapatoLista(LoginRequiredMixin, ListView):
    context_object_name = 'zapatos'
    queryset = Articulo.objects.filter(articulo__startswith='zapato')
    template_name = 'thriftshop/listaZapatos.html'

class ZapatoDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = 'zapato'
    template_name = 'thriftshop/zapatoDetalle.html'

class ZapatoUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ActualizacionArticulo
    success_url = reverse_lazy('zapatos')
    context_object_name = 'zapato'
    template_name = 'thriftshop/zapatoEdicion.html'

class ZapatoDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('zapatos')
    context_object_name = 'zapato'
    template_name = 'thriftshop/zapatoBorrado.html'


# OTRO

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Articulo.objects.filter(articulo__startswith='otro')
    template_name = 'thriftshop/listaOtros.html'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = 'otro'
    template_name = 'thriftshop/otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ActualizacionArticulo
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'thriftshop/otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'thriftshop/otroBorrado.html'

# CREACION ARTICULO

class ArticuloCreacion(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = FormularioNuevoArticulo
    success_url = reverse_lazy('home')
    template_name = 'thriftshop/articuloCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArticuloCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'thriftshop/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'thriftshop/acercaDeMi.html', {})
