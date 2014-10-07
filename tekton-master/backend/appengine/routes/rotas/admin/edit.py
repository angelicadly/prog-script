# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from rota_app import facade
from routes.rotas import admin


@no_csrf
def index(rota_id):
    rota = facade.get_rota_cmd(rota_id)()
    detail_form = facade.rota_detail_form()
    context = {'save_path': router.to_path(save, rota_id), 'rota': detail_form.fill_with_model(rota)}
    return TemplateResponse(context, 'rotas/admin/form.html')


def save(_handler, rota_id, **rota_properties):
    cmd = facade.update_rota_cmd(rota_id, **rota_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'rota': cmd.form}

        return TemplateResponse(context, 'rotas/admin/form.html')
    _handler.redirect(router.to_path(admin))

