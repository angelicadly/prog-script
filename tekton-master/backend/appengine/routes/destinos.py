# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm
from tekton import router
from gaegraph.model import Node, Arc
from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    query=Destino.query().order(Destino.destino)
    destino_lista = query.fetch()
    destino_form=DestinoFormTable()
    destino_lista=[destino_form.fill_with_model(destino) for destino in destino_lista]
    editar_form_path=router.to_path(editar_form)
    delete_path=router.to_path(delete)
    for destino in destino_lista:
        destino['edit_path']='%s/%s'%(editar_form_path, destino['id'])
        destino['delete_path']='%s/%s'%(delete_path, destino['id'])
    contexto={'destino_lista': destino_lista,
              'form_path':router.to_path(form),
              'regioes_path':router.to_path(regioes),
              'destinos_por_regiao':router.to_path(destinosRegiao)}
    return  TemplateResponse(contexto)

def delete(destino_id):
    chave=ndb.Key(Destino,int(destino_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))

@no_csrf
def editar_form(destino_id):
    destino_id=int(destino_id)
    destino = Destino.get_by_id(destino_id)
    destino_form=DestinoForm()
    destino_form.fill_with_model(destino)
    contexto={'salvar_path':router.to_path(editar, destino_id),
              'destino':destino_form}
    return TemplateResponse(contexto, 'destinos/form.html')

@no_csrf
def form(regiao_id):
    contexto={'salvar_path':router.to_path(salvar, regiao_id)}
    return TemplateResponse(contexto)

@no_csrf
def destino_regiao(regiao_id):
    query=Destino.query(Destino.regiao_id==regiao_id).order(Destino.destino)
    destino_lista = query.fetch()
    destino_form=DestinoForm()
    destino_lista=[destino_form.fill_with_model(destino) for destino in destino_lista]

    contexto={'destino_lista': destino_lista}
    return TemplateResponse(contexto, 'destinos/destino_regiao.html')

@no_csrf
def regioes():

    query=Regiao.query().order(Regiao.regiao)
    regiao_lista = query.fetch()
    regiao_form=RegiaoForm()
    regiao_lista=[regiao_form.fill_with_model(regiao) for regiao in regiao_lista]

    form_path=router.to_path(form)
    #regiao_lista = {'id':0, 'regiao':'Norte'}, {'id':1,'regiao':'Nordeste'},{'id': 2,'regiao':'Centro-Oeste'}, {'id':3,'regiao':'Sudeste'}, {'id':4,'regiao':'Sul'}
    for regiao in regiao_lista:
        regiao['form_path']='%s/%s'%(form_path, regiao['id'])
    contexto={'regiao_lista': regiao_lista}
    return TemplateResponse(contexto, 'destinos/regioes.html')

@no_csrf
def destinosRegiao():

    query=Regiao.query().order(Regiao.regiao)
    regiao_lista = query.fetch()
    regiao_form=RegiaoForm()
    regiao_lista=[regiao_form.fill_with_model(regiao) for regiao in regiao_lista]

    destino_regiao_path=router.to_path(destino_regiao)
    for regiao in regiao_lista:
        regiao['destino_regiao_path']='%s/%s'%(destino_regiao_path, regiao['id'])
    contexto={'regiao_lista': regiao_lista}
    return TemplateResponse(contexto, 'destinos/regioes_destinos.html')

@no_csrf
class Regiao(Node):
    regiao=ndb.StringProperty(required=True)

@no_csrf
class RegiaoForm(ModelForm):
   _model_class = Regiao
   _include = [Regiao.regiao]

@no_csrf
def salvarRegiao(**propriedades):
    regiao_form=RegiaoForm(**propriedades)
    erros=regiao_form.validate()
    if erros:
        contexto={'salvar_regiao_path':router.to_path(salvarRegiao),
                  'erros':erros,
                  'regiao':regiao_form}
        return TemplateResponse(contexto, 'destinos/regiao_form.html')
    regiao = regiao_form.fill_model()
    chave_do_destino = regiao.put()
    return RedirectResponse(router.to_path(regioes))

@no_csrf
def regiao_form():
    contexto={'salvar_regiao_path':router.to_path(salvarRegiao)}
    return TemplateResponse(contexto)

class Destino(Node):
    destino=ndb.StringProperty(required=True)
    preco=ndb.FloatProperty()
    descricao=ndb.StringProperty()
    regiao_id=ndb.StringProperty()
    #regiao=ndb.StringProperty()
    #categoria=ndb.StringProperty()

#class DestinoForm(Form):
#   destino=base.StringField(required=True)
#   preco=base.FloatField()
#   regiao=base.StringField()
#   categoria=base.StringField()

class DestinoForm(ModelForm):
   _model_class = Destino
   _include = [Destino.destino, Destino.preco, Destino.descricao, Destino.regiao_id]

class DestinoFormTable(ModelForm):
   _model_class = Destino
   _include = [Destino.destino, Destino.preco, Destino.regiao_id]

def salvar(regiao_id,**propriedades):
    propriedades.update({'regiao_id':regiao_id})

    destino_form=DestinoForm(**propriedades)
    erros=destino_form.validate()
    if erros:
        contexto={'salvar_path':router.to_path(salvar, regiao_id),
                  'erros':erros,
                  'destino':destino_form}
        return TemplateResponse(contexto, 'destinos/form.html')
    #destino=Destino(destino=propriedades['destino'],
    #                preco=float(propriedades['preco']),
    #                regiao=propriedades['regiao'],
    #                categoria=propriedades['categoria'])
    destino = destino_form.fill_model()
    chave_do_destino = destino.put()

    #_resp.write(propriedades)
    return RedirectResponse(router.to_path(index))

def editar(destino_id,**propriedades):
    destino_id=int(destino_id)
    destino = Destino.get_by_id(destino_id)
    destino_form=DestinoForm(**propriedades)
    erros=destino_form.validate()
    if erros:
        contexto={'salvar_path':router.to_path(salvar),
                  'erros':erros,
                  'destino':destino_form}
        return TemplateResponse(contexto, 'destinos/form.html')
    destino_form.fill_model(destino)
    destino.put()
    #_resp.write(propriedades)
    return RedirectResponse(router.to_path(index))

class CategoriaDestino (Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Destino, required=True)