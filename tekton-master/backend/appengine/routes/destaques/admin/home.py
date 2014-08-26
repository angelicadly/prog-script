# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from destaque_app import facade
from routes.destaques.admin import new, edit


def delete(_handler, destaques_id):
    facade.delete_destaques_cmd(destaques_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_destaquess_cmd()
    destaquess = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.destaques_short_form()

    def short_destaques_dict(destaques):
        destaques_dct = short_form.fill_with_model(destaques)
        destaques_dct['edit_path'] = router.to_path(edit_path, destaques_dct['id'])
        destaques_dct['delete_path'] = router.to_path(delete_path, destaques_dct['id'])
        return destaques_dct

    short_destaquess = [short_destaques_dict(destaques) for destaques in destaquess]
    context = {'destaquess': short_destaquess,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

