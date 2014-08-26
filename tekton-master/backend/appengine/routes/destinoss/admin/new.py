# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from destinos_app import facade
from routes.destinoss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'destinoss/admin/form.html')


def save(_handler, viaje_bem_id=None, **viaje_bem_properties):
    cmd = facade.save_viaje_bem_cmd(**viaje_bem_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'viaje_bem': cmd.form}

        return TemplateResponse(context, 'destinoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

