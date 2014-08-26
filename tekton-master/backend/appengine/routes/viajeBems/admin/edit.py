# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from viajeBem_app import facade
from routes.viajeBems import admin


@no_csrf
def index(viaje_bem_id):
    viaje_bem = facade.get_viaje_bem_cmd(viaje_bem_id)()
    detail_form = facade.viaje_bem_detail_form()
    context = {'save_path': router.to_path(save, viaje_bem_id), 'viaje_bem': detail_form.fill_with_model(viaje_bem)}
    return TemplateResponse(context, 'viajeBems/admin/form.html')


def save(_handler, viaje_bem_id, **viaje_bem_properties):
    cmd = facade.update_viaje_bem_cmd(viaje_bem_id, **viaje_bem_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'viaje_bem': cmd.form}

        return TemplateResponse(context, 'viajeBems/admin/form.html')
    _handler.redirect(router.to_path(admin))

