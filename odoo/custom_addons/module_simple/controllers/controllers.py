# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleSimple(http.Controller):
#     @http.route('/module_simple/module_simple', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_simple/module_simple/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_simple.listing', {
#             'root': '/module_simple/module_simple',
#             'objects': http.request.env['module_simple.module_simple'].search([]),
#         })

#     @http.route('/module_simple/module_simple/objects/<model("module_simple.module_simple"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_simple.object', {
#             'object': obj
#         })

