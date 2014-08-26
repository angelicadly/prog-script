# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from destaque_app.model import Destaques

class DestaquesPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Destaques
    _include = [Destaques.destino, 
                Destaques.preco]


class DestaquesForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Destaques
    _include = [Destaques.destino, 
                Destaques.preco]


class DestaquesDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Destaques
    _include = [Destaques.creation, 
                Destaques.preco, 
                Destaques.destino]


class DestaquesShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Destaques
    _include = [Destaques.creation, 
                Destaques.preco, 
                Destaques.destino]


class SaveDestaquesCommand(SaveCommand):
    _model_form_class = DestaquesForm


class UpdateDestaquesCommand(UpdateNode):
    _model_form_class = DestaquesForm


class ListDestaquesCommand(ModelSearchCommand):
    def __init__(self):
        super(ListDestaquesCommand, self).__init__(Destaques.query_by_creation())

