# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from destaques_app import facade
from routes.destaquess import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'destaquess/admin/form.html')


def save(_handler, viaje_bem_id=None, **viaje_bem_properties):
    cmd = facade.save_viaje_bem_cmd(**viaje_bem_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'viaje_bem': cmd.form}

        return TemplateResponse(context, 'destaquess/admin/form.html')
    _handler.redirect(router.to_path(admin))

