# -*- coding: utf-8 -*-
from odoo import http

# class PruebaQs(http.Controller):
#     @http.route('/prueba_qs/prueba_qs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba_qs/prueba_qs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba_qs.listing', {
#             'root': '/prueba_qs/prueba_qs',
#             'objects': http.request.env['prueba_qs.prueba_qs'].search([]),
#         })

#     @http.route('/prueba_qs/prueba_qs/objects/<model("prueba_qs.prueba_qs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba_qs.object', {
#             'object': obj
#         })