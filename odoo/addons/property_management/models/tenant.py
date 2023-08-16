from odoo import models, fields, api


class Tenant(models.Model):

    _name = 'promasy.tenant'
    _description = 'Tenant'

    name = fields.Char(string='Full Name', required=True)
    image = fields.Binary(string='Image',required=False)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    date_of_birth = fields.Date(string='Date of Birth')
    id_type = fields.Selection([('passport', 'Passport'), ('id_card', 'ID Card')], string='ID Type')
    id_number = fields.Char(string='ID Number')
    occupation = fields.Char(string='Occupation')
    emergency_contact_name = fields.Char(string='Emergency Contact Name')
    emergency_contact_phone = fields.Char(string='Emergency Contact Phone')
    property_ids = fields.Many2many('promasy.property', string='Rented Properties')
    contract_ids = fields.One2many('promasy.contract', 'tenant_id', string='Contracts')
    document_ids = fields.One2many('promasy.document', 'tenant_id', string='Documents')
    notes = fields.Text(string='Notes')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

