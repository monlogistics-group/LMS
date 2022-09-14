# -*- coding: utf-8 -*-
from email.policy import strict
from odoo import models, fields, api, _
from datetime import date, timedelta

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
    general_package = Package choice
    general_order = Order choice
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
        'product.product', string="Product"
    )
    declaration_number = fields.Char(string="Declaration Number")
    declaration_date = fields.Date(string="Declaration Date")
    customs_clerance_date = fields.Date(string="Customs Clearance Date")
    tracking = fields.Many2many(
        'lms.general.order.tracking', string="Tracking"
    )

    def create_invoice(self):
        products = []
        for product in self.sales_products:
            one = self.env['product.product'].search([('id','=',product.id)])
            products.append((
                0,
                0,
                {
                    'product_id': one.id,
                    'price_unit': one.list_price
                }
            ))

        invoices = self.env['account.move'].create([
            {
                'move_type': 'out_invoice',
                'partner_id': self.customer_id.id,
                'invoice_date': date.today(),
                'invoice_date_due': date.today()+timedelta(days=14),
                'invoice_line_ids': products,
            },
        ])
        invoices.action_post()
        ## FOR REGISTER AS PAID
        # for invoice in invoices:
        #     self.env['account.payment.register'].with_context(active_model='account.move', active_ids=invoice.ids).create({})._create_payments()
        invoices.flush()

class Tracking(models.Model):
    _name = "lms.general.order.tracking"
    _description = "LMS general order tracking"

    location = fields.Char(string="Location")
    description = fields.Char(string="Description")
    date = fields.Date(string="Date")

