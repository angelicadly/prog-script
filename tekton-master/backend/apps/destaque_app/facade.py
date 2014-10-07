# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from destaque_app.commands import ListDestaqueCommand, SaveDestaqueCommand, UpdateDestaqueCommand, \
    DestaquePublicForm, DestaqueDetailForm, DestaqueShortForm


def save_destaque_cmd(**destaque_properties):
    """
    Command to save Destaque entity
    :param destaque_properties: a dict of properties to save on model
    :return: a Command that save Destaque, validating and localizing properties received as strings
    """
    return SaveDestaqueCommand(**destaque_properties)


def update_destaque_cmd(destaque_id, **destaque_properties):
    """
    Command to update Destaque entity with id equals 'destaque_id'
    :param destaque_properties: a dict of properties to update model
    :return: a Command that update Destaque, validating and localizing properties received as strings
    """
    return UpdateDestaqueCommand(destaque_id, **destaque_properties)


def list_destaques_cmd():
    """
    Command to list Destaque entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListDestaqueCommand()


def destaque_detail_form(**kwargs):
    """
    Function to get Destaque's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return DestaqueDetailForm(**kwargs)


def destaque_short_form(**kwargs):
    """
    Function to get Destaque's short form. just a subset of destaque's properties
    :param kwargs: form properties
    :return: Form
    """
    return DestaqueShortForm(**kwargs)

def destaque_public_form(**kwargs):
    """
    Function to get Destaque'spublic form. just a subset of destaque's properties
    :param kwargs: form properties
    :return: Form
    """
    return DestaquePublicForm(**kwargs)


def get_destaque_cmd(destaque_id):
    """
    Find destaque by her id
    :param destaque_id: the destaque id
    :return: Command
    """
    return NodeSearch(destaque_id)


def delete_destaque_cmd(destaque_id):
    """
    Construct a command to delete a Destaque
    :param destaque_id: destaque's id
    :return: Command
    """
    return DeleteNode(destaque_id)

