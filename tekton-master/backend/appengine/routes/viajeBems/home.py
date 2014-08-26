# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from viajeBem_app import facade
from routes.viajeBems import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_viaje_bems_cmd()
    viaje_bems = cmd()
    public_form = facade.viaje_bem_public_form()
    viaje_bem_public_dcts = [public_form.fill_with_model(viaje_bem) for viaje_bem in viaje_bems]
    context = {'viaje_bems': viaje_bem_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

