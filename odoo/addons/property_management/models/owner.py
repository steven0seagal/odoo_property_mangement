from odoo import models, fields, api
class RentalOwner(models.Model):
    _name = 'promasy.owner'
    _description = 'Rental Property Owner Information'

    name = fields.Char(string='Full Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    address = fields.Text(string='Address')
    bank_account = fields.Char(string='Bank Account')
    property_ids = fields.Many2many('promasy.property', string='Properties')
    company_name = fields.Char(string='Company Name') # If the owner is a company
    id_type = fields.Selection([('passport', 'Passport'), ('id_card', 'ID Card')], string='ID Type')
    id_number = fields.Char(string='ID Number')
    tax_id = fields.Char(string='Tax ID')
    notes = fields.Text(string='Notes')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')
    # Other fields and relationships
