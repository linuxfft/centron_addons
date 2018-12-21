# -*- coding: utf-8 -*-
from odoo import http

# class ProductCentron(http.Controller):
#     @http.route('/product_centron/product_centron/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_centron/product_centron/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_centron.listing', {
#             'root': '/product_centron/product_centron',
#             'objects': http.request.env['product_centron.product_centron'].search([]),
#         })

#     @http.route('/product_centron/product_centron/objects/<model("product_centron.product_centron"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_centron.object', {
#             'object': obj
#         })