# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


"""
    General model
    -------------------------------
    name = REF number
    customer_id = customer
    consignee_id = consignee
    shipper_id = shipper
    operation_types = operation type
    freight_types = Freight Types
    gross_weigth = Gross weigth
    volume = CBM
    package_qty = Package Quantity
    fleet_id = vehicle 
    driver_id = driver tagged
    estimated_cost = User type cost
    actual_cost = Cost from service
    orgin_point = Origin country
    destination_point = Destiantion country
    estimated_pickup = Pickup date
    actual_pickup = Pickup date
    estimated_delivery = Delivery date
    actual_delivery = Delivery date
    notice = Notice text
    state = Operation status
    general_order = Order choice
    general_package = Package choice
    sales_product = Services choice
    -------------------------------
"""


class General(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
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

    notice = fields.Char(string="Notice")
    state = fields.Many2one('lms.general.status', string="State",
                            default=lambda self: self.env['lms.general.status'].search([('default', '=', 'True')]))
    general_order = fields.Many2many(
        'lms.general.order', string="Orders")
    general_package = fields.Many2many(
        'lms.general.package', string="Package"
    )
    sales_products = fields.Many2many(
        'product.template', string="Product"
    )

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'lms.general') or _('New')
        res = super(General, self).create(vals)
        return res
