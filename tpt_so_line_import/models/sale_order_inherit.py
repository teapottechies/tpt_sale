# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import base64
import csv
import logging

_logger = logging.getLogger(__name__)


class SaleOrderImport(models.Model):
    _name = "sale.order.import"
    _description = "Import Order Lines"

    upload_file = fields.Binary(string="Upload File")
    filename = fields.Char('Filename')

    def action_confirm(self):
        try:
            order_file = base64.b64decode(self.upload_file).decode("utf-8", "ignore")
            reader = csv.DictReader(order_file.split('\n'))
            order_id = self.env['sale.order'].browse(self._context.get('active_id'))
            product_not_found = []
            for row in reader:
                product_id = self.env['product.product'].search(
                    [('default_code', '=', row['Code'])])
                if product_id:
                    self.env['sale.order.line'].create(
                        {'order_id': order_id.id, 'product_id': product_id.id,
                         'product_uom_qty': int(row['Quantity']),
                         'discount': row['Discount']})
                else:
                    product_not_found.append(str(row['Code']))
                    raise ValidationError(_("Internal Reference is not found!! '%s'" % product_not_found))
        except Exception as e:
            raise ValidationError(u'{}'.format(e))
