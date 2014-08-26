# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from destaque_app import facade
from routes.destaques import admin


@no_csrf
def index(destaques_id):
    destaques = facade.get_destaques_cmd(destaques_id)()
    detail_form = facade.destaques_detail_form()
    context = {'save_path': router.to_path(save, destaques_id), 'destaques': detail_form.fill_with_model(destaques)}
    return TemplateResponse(context, 'destaques/admin/form.html')


def save(_handler, destaques_id, **destaques_properties):
    cmd = facade.update_destaques_cmd(destaques_id, **destaques_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'destaques': cmd.form}

        return TemplateResponse(context, 'destaques/admin/form.html')
    _handler.redirect(router.to_path(admin))

