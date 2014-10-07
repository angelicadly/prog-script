# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from rota_app.model import Rota

class RotaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Rota
    _include = [Rota.idade, 
                Rota.nome]


class RotaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Rota
    _include = [Rota.idade, 
                Rota.nome]


class RotaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Rota
    _include = [Rota.idade, 
                Rota.creation, 
                Rota.nome]


class RotaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Rota
    _include = [Rota.idade, 
                Rota.creation, 
                Rota.nome]


class SaveRotaCommand(SaveCommand):
    _model_form_class = RotaForm


class UpdateRotaCommand(UpdateNode):
    _model_form_class = RotaForm


class ListRotaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListRotaCommand, self).__init__(Rota.query_by_creation())

