from django import forms 
from subscription.models import	Subscription
from django.utils.translation import ungettext
from django.utils.translation import ugettext as _
from subscription.validators import CpfValidator

class SubscriptionForm(forms.ModelForm):  	

    name = forms.CharField(label=_('Nome'), max_length=100)
    cpf = forms.CharField(label = _('CPF'), max_length=11, min_length=11, validators = [CpfValidator])
    email = forms.EmailField(label= _('E-Mail'))
    phone = forms.CharField(label=_('Telefone'), required = False, max_length = 20)

    class Meta:
      model = Subscription
      exclude =	('created_at','paid',)

    def unique_check(self, fieldname, error_message):
        param = { fieldname: self.cleaned_data[fieldname] }
        try:
            s = Subscription.objects.get(**param)
        except Subscription.DoesNotExist:
            return self.cleaned_data[fieldname]
        raise forms.ValidationError(error_message)
    
    def clean_cpf(self):
        return self.unique_check('cpf', _(u'CPF ja inscrito.'))
    
    def clean_email(self):
        return self.unique_check('email', _(u'E-mail ja inscrito.'))

    def clean(self):
        super(SubscriptionForm, self).clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise forms.ValidationError(_(u'Voce precisa informar seu e-mail ou seu telefone.'))
        return self.cleaned_data
