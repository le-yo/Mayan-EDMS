from __future__ import absolute_import, unicode_literals

from collections import OrderedDict

from django import forms

from mayan.apps.common.classes import ModelProperty
from mayan.apps.common.widgets import NamedMultiWidget


class TemplateWidget(NamedMultiWidget):
    def __init__(self, attrs=None, **kwargs):
        widgets = OrderedDict()

        widgets['model_property'] = forms.widgets.Select()
        widgets['template'] = forms.widgets.Textarea(
            attrs={'rows': 5}
        )
        super(TemplateWidget, self).__init__(
            widgets=widgets, attrs=attrs, **kwargs
        )

    def decompress(self, value):
        choices = ModelProperty.get_choices_for(
            model=self.attrs['model']
        )
        self.widgets['model_property'].choices = (
            [('', '----')] + choices
        )
        return {
            'model_property': None, 'template': value
        }

    def value_from_datadict(self, querydict, files, name):
        template = querydict.get('{}_template'.format(name))

        return template
