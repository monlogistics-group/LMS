# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api, _

class General(models.Model):
    _name = 'lms.general'
    _description = 'LMS general information'

    name = fields.Char(string='Ref', required=True,
                       readonly=True, default=lambda self: _('New'))
    customer_id = fields.Many2one('res.partner', string='Customer')
    consignee_id = fields.Many2one('res.partner', string='Consignee')
    shipper_id = fields.Many2one('res.partner', string='Shipper')
    operation_types = fields.Many2one(
        'lms.operation.type.datas', string="Operation Types")
    freigth_types = fields.Many2one(
        'lms.freight.type.datas', string="Freigth Types")
    gross_weigth = fields.Float(string="Gross Weight")
    volume = fields.Float(string="CBM")
    package_qty = fields.Float(string="Package Quantity")
    fleet_id = fields.Many2one('fleet.vehicle', string="Trucks")
    driver_id = fields.Many2one('res.users', string="Drivers")
    estimated_cost = fields.Float(string="Estimated Cost")
    actual_cost = fields.Float(string="Actual Cost")
    origin_point = fields.Many2one('res.country', string='Origin Country')
    destination_point = fields.Many2one(
        'res.country', string='Destination Country')
    estimated_pickup = fields.Date(string="Pickup Date")
    actual_pickup = fields.Date(string="Pickup Date")
    estimated_delivery = fields.Date(string="Delivery Date")
    actual_delivery = fields.Date(string="Delivery Date")

    notice = fields.Text(string="Notice")
    state = fields.Many2one('lms.general.status', string="State",
                            default=lambda self: self.env['lms.general.status'].search([('default', '=', 'True')]))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'lms.general') or _('New')
        res = super(General, self).create(vals)
        return res
