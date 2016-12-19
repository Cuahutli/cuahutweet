from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["el usuario debe estar logueado para continuar"])
            return self.form_invalid(form)

class UserOwnerMixin(object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["El usuario no tiene permisos para modificar este Tweet"])
            return self.form_invalid(form)
