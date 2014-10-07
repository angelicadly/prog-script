# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from rota_app import facade


def index():
    cmd = facade.list_rotas_cmd()
    rota_list = cmd()
    short_form=facade.rota_short_form()
    rota_short = [short_form.fill_with_model(m) for m in rota_list]
    return JsonResponse(rota_short)


def save(**rota_properties):
    cmd = facade.save_rota_cmd(**rota_properties)
    return _save_or_update_json_response(cmd)


def update(rota_id, **rota_properties):
    cmd = facade.update_rota_cmd(rota_id, **rota_properties)
    return _save_or_update_json_response(cmd)


def delete(rota_id):
    facade.delete_rota_cmd(rota_id)()


def _save_or_update_json_response(cmd):
    try:
        rota = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.rota_short_form()
    return JsonResponse(short_form.fill_with_model(rota))

