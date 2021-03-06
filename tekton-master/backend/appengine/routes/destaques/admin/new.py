# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from destaque_app import facade
from routes.destaques import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'destaques/admin/form.html')


def save(_handler, destaque_id=None, **destaque_properties):
    cmd = facade.save_destaque_cmd(**destaque_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'destaque': cmd.form}

        return TemplateResponse(context, 'destaques/admin/form.html')
    _handler.redirect(router.to_path(admin))

