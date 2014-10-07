# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from destaque_app.model import Destaque

class DestaquePublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Destaque
    _include = [Destaque.categoria, 
                Destaque.destino, 
                Destaque.preco]


class DestaqueForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Destaque
    _include = [Destaque.categoria, 
                Destaque.destino, 
                Destaque.preco]


class DestaqueDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Destaque
    _include = [Destaque.categoria, 
                Destaque.creation, 
                Destaque.preco, 
                Destaque.destino]


class DestaqueShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Destaque
    _include = [Destaque.categoria, 
                Destaque.creation, 
                Destaque.preco, 
                Destaque.destino]


class SaveDestaqueCommand(SaveCommand):
    _model_form_class = DestaqueForm


class UpdateDestaqueCommand(UpdateNode):
    _model_form_class = DestaqueForm


class ListDestaqueCommand(ModelSearchCommand):
    def __init__(self):
        super(ListDestaqueCommand, self).__init__(Destaque.query_by_creation())

