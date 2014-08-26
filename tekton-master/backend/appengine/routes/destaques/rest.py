# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from destaque_app import facade


def index():
    cmd = facade.list_destaquess_cmd()
    destaques_list = cmd()
    short_form=facade.destaques_short_form()
    destaques_short = [short_form.fill_with_model(m) for m in destaques_list]
    return JsonResponse(destaques_short)


def save(**destaques_properties):
    cmd = facade.save_destaques_cmd(**destaques_properties)
    return _save_or_update_json_response(cmd)


def update(destaques_id, **destaques_properties):
    cmd = facade.update_destaques_cmd(destaques_id, **destaques_properties)
    return _save_or_update_json_response(cmd)


def delete(destaques_id):
    facade.delete_destaques_cmd(destaques_id)()


def _save_or_update_json_response(cmd):
    try:
        destaques = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.destaques_short_form()
    return JsonResponse(short_form.fill_with_model(destaques))

