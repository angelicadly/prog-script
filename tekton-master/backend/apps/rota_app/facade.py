# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from rota_app.commands import ListRotaCommand, SaveRotaCommand, UpdateRotaCommand, \
    RotaPublicForm, RotaDetailForm, RotaShortForm


def save_rota_cmd(**rota_properties):
    """
    Command to save Rota entity
    :param rota_properties: a dict of properties to save on model
    :return: a Command that save Rota, validating and localizing properties received as strings
    """
    return SaveRotaCommand(**rota_properties)


def update_rota_cmd(rota_id, **rota_properties):
    """
    Command to update Rota entity with id equals 'rota_id'
    :param rota_properties: a dict of properties to update model
    :return: a Command that update Rota, validating and localizing properties received as strings
    """
    return UpdateRotaCommand(rota_id, **rota_properties)


def list_rotas_cmd():
    """
    Command to list Rota entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListRotaCommand()


def rota_detail_form(**kwargs):
    """
    Function to get Rota's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return RotaDetailForm(**kwargs)


def rota_short_form(**kwargs):
    """
    Function to get Rota's short form. just a subset of rota's properties
    :param kwargs: form properties
    :return: Form
    """
    return RotaShortForm(**kwargs)

def rota_public_form(**kwargs):
    """
    Function to get Rota'spublic form. just a subset of rota's properties
    :param kwargs: form properties
    :return: Form
    """
    return RotaPublicForm(**kwargs)


def get_rota_cmd(rota_id):
    """
    Find rota by her id
    :param rota_id: the rota id
    :return: Command
    """
    return NodeSearch(rota_id)


def delete_rota_cmd(rota_id):
    """
    Construct a command to delete a Rota
    :param rota_id: rota's id
    :return: Command
    """
    return DeleteNode(rota_id)

