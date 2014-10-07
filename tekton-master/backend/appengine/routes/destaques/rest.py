# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from destaque_app import facade


def index():
    cmd = facade.list_destaques_cmd()
    destaque_list = cmd()
    short_form=facade.destaque_short_form()
    destaque_short = [short_form.fill_with_model(m) for m in destaque_list]
    return JsonResponse(destaque_short)


def save(**destaque_properties):
    cmd = facade.save_destaque_cmd(**destaque_properties)
    return _save_or_update_json_response(cmd)


def update(destaque_id, **destaque_properties):
    cmd = facade.update_destaque_cmd(destaque_id, **destaque_properties)
    return _save_or_update_json_response(cmd)


def delete(destaque_id):
    facade.delete_destaque_cmd(destaque_id)()


def _save_or_update_json_response(cmd):
    try:
        destaque = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.destaque_short_form()
    return JsonResponse(short_form.fill_with_model(destaque))

