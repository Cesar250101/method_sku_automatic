# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Productos(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, values):        
        values['default_code'] = self.env['ir.sequence'].next_by_code('SKU')
        res = super(Productos, self).create(values)
        return res
