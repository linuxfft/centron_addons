# -*- coding: utf-8 -*-
from odoo import http

# class PurchaseCentron(http.Controller):
#     @http.route('/purchase_centron/purchase_centron/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_centron/purchase_centron/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_centron.listing', {
#             'root': '/purchase_centron/purchase_centron',
#             'objects': http.request.env['purchase_centron.purchase_centron'].search([]),
#         })

#     @http.route('/purchase_centron/purchase_centron/objects/<model("purchase_centron.purchase_centron"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_centron.object', {
#             'object': obj
#         })