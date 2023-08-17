from odoo import models, fields, api
class RentalPayment(models.Model):
    _name = 'promasy.payment'
    _description = 'Rental Payment Information'

    name = fields.Char(string='Payment Reference', required=True)
    tenant_id = fields.Many2one('promasy.tenant', string='Tenant', required=True)
    property_id = fields.Many2many('promasy.property', string='Property', required=True)
    contract_id = fields.Many2one('promasy.contract', string='Contract', required=True)
    payment_date = fields.Date(string='Payment Date', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    payment_type = fields.Selection([
        ('rent', 'Rent'),
        ('deposit', 'Deposit'),
        ('utility', 'Utility'),
        ('penalty', 'Penalty'),
        ('other', 'Other')
    ], string='Payment Type', required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
        ('other', 'Other')
    ], string='Payment Method')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('late', 'Late'),
        ('failed', 'Failed')
    ], string='Status', default='pending')
    notes = fields.Text(string='Notes')
    invoice_id = fields.Many2one('promasy.document', string='Invoice')
    # Other fields and relationships
