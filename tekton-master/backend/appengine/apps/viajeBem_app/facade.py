# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from viajeBem_app.commands import ListViajeBemCommand, SaveViajeBemCommand, UpdateViajeBemCommand, \
    ViajeBemPublicForm, ViajeBemDetailForm, ViajeBemShortForm


def save_viaje_bem_cmd(**viaje_bem_properties):
    """
    Command to save ViajeBem entity
    :param viaje_bem_properties: a dict of properties to save on model
    :return: a Command that save ViajeBem, validating and localizing properties received as strings
    """
    return SaveViajeBemCommand(**viaje_bem_properties)


def update_viaje_bem_cmd(viaje_bem_id, **viaje_bem_properties):
    """
    Command to update ViajeBem entity with id equals 'viaje_bem_id'
    :param viaje_bem_properties: a dict of properties to update model
    :return: a Command that update ViajeBem, validating and localizing properties received as strings
    """
    return UpdateViajeBemCommand(viaje_bem_id, **viaje_bem_properties)


def list_viaje_bems_cmd():
    """
    Command to list ViajeBem entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListViajeBemCommand()


def viaje_bem_detail_form(**kwargs):
    """
    Function to get ViajeBem's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ViajeBemDetailForm(**kwargs)


def viaje_bem_short_form(**kwargs):
    """
    Function to get ViajeBem's short form. just a subset of viaje_bem's properties
    :param kwargs: form properties
    :return: Form
    """
    return ViajeBemShortForm(**kwargs)

def viaje_bem_public_form(**kwargs):
    """
    Function to get ViajeBem'spublic form. just a subset of viaje_bem's properties
    :param kwargs: form properties
    :return: Form
    """
    return ViajeBemPublicForm(**kwargs)


def get_viaje_bem_cmd(viaje_bem_id):
    """
    Find viaje_bem by her id
    :param viaje_bem_id: the viaje_bem id
    :return: Command
    """
    return NodeSearch(viaje_bem_id)


def delete_viaje_bem_cmd(viaje_bem_id):
    """
    Construct a command to delete a ViajeBem
    :param viaje_bem_id: viaje_bem's id
    :return: Command
    """
    return DeleteNode(viaje_bem_id)

