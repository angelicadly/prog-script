# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from viajeBem_app.model import ViajeBem

class ViajeBemPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = ViajeBem
    _include = [ViajeBem.destino, 
                ViajeBem.preco]


class ViajeBemForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = ViajeBem
    _include = [ViajeBem.destino, 
                ViajeBem.preco]


class ViajeBemDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = ViajeBem
    _include = [ViajeBem.creation, 
                ViajeBem.preco, 
                ViajeBem.destino]


class ViajeBemShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = ViajeBem
    _include = [ViajeBem.creation, 
                ViajeBem.preco, 
                ViajeBem.destino]


class SaveViajeBemCommand(SaveCommand):
    _model_form_class = ViajeBemForm


class UpdateViajeBemCommand(UpdateNode):
    _model_form_class = ViajeBemForm


class ListViajeBemCommand(ModelSearchCommand):
    def __init__(self):
        super(ListViajeBemCommand, self).__init__(ViajeBem.query_by_creation())

