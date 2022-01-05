# -*- coding: utf-8 -*-
from odoo import http

# class MethodSkuAutomatic(http.Controller):
#     @http.route('/method_sku_automatic/method_sku_automatic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_sku_automatic/method_sku_automatic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_sku_automatic.listing', {
#             'root': '/method_sku_automatic/method_sku_automatic',
#             'objects': http.request.env['method_sku_automatic.method_sku_automatic'].search([]),
#         })

#     @http.route('/method_sku_automatic/method_sku_automatic/objects/<model("method_sku_automatic.method_sku_automatic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_sku_automatic.object', {
#             'object': obj
#         })