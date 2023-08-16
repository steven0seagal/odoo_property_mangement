from odoo import models, fields, api
class RentalContractor(models.Model):
    _name = 'promasy.contractor'
    _description = 'Rental Property Contractor Information'

    name = fields.Char(string='Contractor Name', required=True)
    contact_name = fields.Char(string='Contact Person')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    service_type = fields.Selection([
        ('maintenance', 'Maintenance'),
        ('cleaning', 'Cleaning'),
        ('construction', 'Construction'),
        ('renovation', 'Renovation'),
        ('other', 'Other')
    ], string='Service Type', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    bank_account = fields.Char(string='Bank Account')
    tax_id = fields.Char(string='Tax ID')
    notes = fields.Text(string='Notes')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='active')
    # Other fields and relationships
