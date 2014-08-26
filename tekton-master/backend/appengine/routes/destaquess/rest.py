# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from destaques_app import facade


def index():
    cmd = facade.list_viaje_bems_cmd()
    viaje_bem_list = cmd()
    short_form=facade.viaje_bem_short_form()
    viaje_bem_short = [short_form.fill_with_model(m) for m in viaje_bem_list]
    return JsonResponse(viaje_bem_short)


def save(**viaje_bem_properties):
    cmd = facade.save_viaje_bem_cmd(**viaje_bem_properties)
    return _save_or_update_json_response(cmd)


def update(viaje_bem_id, **viaje_bem_properties):
    cmd = facade.update_viaje_bem_cmd(viaje_bem_id, **viaje_bem_properties)
    return _save_or_update_json_response(cmd)


def delete(viaje_bem_id):
    facade.delete_viaje_bem_cmd(viaje_bem_id)()


def _save_or_update_json_response(cmd):
    try:
        viaje_bem = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.viaje_bem_short_form()
    return JsonResponse(short_form.fill_with_model(viaje_bem))

