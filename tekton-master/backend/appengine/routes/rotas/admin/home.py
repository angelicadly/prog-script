# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from rota_app import facade
from routes.rotas.admin import new, edit


def delete(_handler, rota_id):
    facade.delete_rota_cmd(rota_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_rotas_cmd()
    rotas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.rota_short_form()

    def short_rota_dict(rota):
        rota_dct = short_form.fill_with_model(rota)
        rota_dct['edit_path'] = router.to_path(edit_path, rota_dct['id'])
        rota_dct['delete_path'] = router.to_path(delete_path, rota_dct['id'])
        return rota_dct

    short_rotas = [short_rota_dict(rota) for rota in rotas]
    context = {'rotas': short_rotas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

