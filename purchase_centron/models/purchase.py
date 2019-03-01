# -*- coding: utf-8 -*-

from odoo import models, fields, api,SUPERUSER_ID
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    @api.multi
    def button_confirm(self):
        if not (self._uid == SUPERUSER_ID or self.env.user.has_group('purchase_centron.group_purchase_order_approve')):
            raise UserError(u'必须是采购订单申批员才能进行确认')
        super(PurchaseOrder, self).button_confirm()