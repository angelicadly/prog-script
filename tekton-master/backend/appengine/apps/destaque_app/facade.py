# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from destaque_app.commands import ListDestaquesCommand, SaveDestaquesCommand, UpdateDestaquesCommand, \
    DestaquesPublicForm, DestaquesDetailForm, DestaquesShortForm


def save_destaques_cmd(**destaques_properties):
    """
    Command to save Destaques entity
    :param destaques_properties: a dict of properties to save on model
    :return: a Command that save Destaques, validating and localizing properties received as strings
    """
    return SaveDestaquesCommand(**destaques_properties)


def update_destaques_cmd(destaques_id, **destaques_properties):
    """
    Command to update Destaques entity with id equals 'destaques_id'
    :param destaques_properties: a dict of properties to update model
    :return: a Command that update Destaques, validating and localizing properties received as strings
    """
    return UpdateDestaquesCommand(destaques_id, **destaques_properties)


def list_destaquess_cmd():
    """
    Command to list Destaques entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListDestaquesCommand()


def destaques_detail_form(**kwargs):
    """
    Function to get Destaques's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return DestaquesDetailForm(**kwargs)


def destaques_short_form(**kwargs):
    """
    Function to get Destaques's short form. just a subset of destaques's properties
    :param kwargs: form properties
    :return: Form
    """
    return DestaquesShortForm(**kwargs)

def destaques_public_form(**kwargs):
    """
    Function to get Destaques'spublic form. just a subset of destaques's properties
    :param kwargs: form properties
    :return: Form
    """
    return DestaquesPublicForm(**kwargs)


def get_destaques_cmd(destaques_id):
    """
    Find destaques by her id
    :param destaques_id: the destaques id
    :return: Command
    """
    return NodeSearch(destaques_id)


def delete_destaques_cmd(destaques_id):
    """
    Construct a command to delete a Destaques
    :param destaques_id: destaques's id
    :return: Command
    """
    return DeleteNode(destaques_id)

