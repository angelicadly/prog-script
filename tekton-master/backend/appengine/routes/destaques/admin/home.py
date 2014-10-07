# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from destaque_app import facade
from routes.destaques.admin import new, edit


def delete(_handler, destaque_id):
    facade.delete_destaque_cmd(destaque_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_destaques_cmd()
    destaques = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.destaque_short_form()

    def short_destaque_dict(destaque):
        destaque_dct = short_form.fill_with_model(destaque)
        destaque_dct['edit_path'] = router.to_path(edit_path, destaque_dct['id'])
        destaque_dct['delete_path'] = router.to_path(delete_path, destaque_dct['id'])
        return destaque_dct

    short_destaques = [short_destaque_dict(destaque) for destaque in destaques]
    context = {'destaques': short_destaques,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

