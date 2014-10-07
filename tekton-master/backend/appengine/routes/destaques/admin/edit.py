# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from destaque_app import facade
from routes.destaques import admin


@no_csrf
def index(destaque_id):
    destaque = facade.get_destaque_cmd(destaque_id)()
    detail_form = facade.destaque_detail_form()
    context = {'save_path': router.to_path(save, destaque_id), 'destaque': detail_form.fill_with_model(destaque)}
    return TemplateResponse(context, 'destaques/admin/form.html')


def save(_handler, destaque_id, **destaque_properties):
    cmd = facade.update_destaque_cmd(destaque_id, **destaque_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'destaque': cmd.form}

        return TemplateResponse(context, 'destaques/admin/form.html')
    _handler.redirect(router.to_path(admin))

