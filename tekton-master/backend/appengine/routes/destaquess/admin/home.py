# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from destaques_app import facade
from routes.destaquess.admin import new, edit


def delete(_handler, viaje_bem_id):
    facade.delete_viaje_bem_cmd(viaje_bem_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_viaje_bems_cmd()
    viaje_bems = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.viaje_bem_short_form()

    def short_viaje_bem_dict(viaje_bem):
        viaje_bem_dct = short_form.fill_with_model(viaje_bem)
        viaje_bem_dct['edit_path'] = router.to_path(edit_path, viaje_bem_dct['id'])
        viaje_bem_dct['delete_path'] = router.to_path(delete_path, viaje_bem_dct['id'])
        return viaje_bem_dct

    short_viaje_bems = [short_viaje_bem_dict(viaje_bem) for viaje_bem in viaje_bems]
    context = {'viaje_bems': short_viaje_bems,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

