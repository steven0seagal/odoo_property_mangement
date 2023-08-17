from odoo import models, fields, api


class RentalContract(models.Model):
    _name = 'promasy.contract'
    _description = 'Rental Contract Information'

    name = fields.Char(string='Contract Reference', required=True)
    property_id = fields.Many2many('promasy.property', string='Property', required=True)
    tenant_id = fields.Many2one('promasy.tenant', string='Tenant', required=True)
    owner_id = fields.Many2one('promasy.owner', string='Owner', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    rent_amount = fields.Float(string='Rent Amount', required=True)
    deposit_amount = fields.Float(string='Deposit Amount')
    payment_frequency = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually')
    ], string='Payment Frequency', required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('bank_transfer', 'Bank Transfer')
    ], string='Payment Method', required=True)
    payment_date = fields.Date(string='Payment Date')
    utility_included = fields.Boolean(string='Utilities Included')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('terminated', 'Terminated')
    ], string='Status', default='draft')
    contract_file = fields.Binary(string='Contract File', attachment=True)
    notes = fields.Text(string='Notes')
    # Other fields and relationships
