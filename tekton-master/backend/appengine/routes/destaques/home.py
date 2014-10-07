# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from destaque_app import facade
from routes.destaques import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_destaques_cmd()
    destaques = cmd()
    public_form = facade.destaque_public_form()
    destaque_public_dcts = [public_form.fill_with_model(destaque) for destaque in destaques]
    context = {'destaques': destaque_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

