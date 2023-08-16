from odoo import models, fields, api


class PromasyDocument(models.Model):

    _name = 'promasy.document'
    _description = 'Document'

    name = fields.Char(string='Document Name', required=True)
    document_type = fields.Selection([
        ('agreement', 'Rental Agreement'),
        ('id_proof', 'ID Proof'),
        ('maintenance', 'Maintenance Receipt'),
        ('inspection', 'Inspection Report'),
        ('other', 'Other')
    ], string='Document Type')
    file = fields.Binary(string='File', attachment=True)
    tenant_id = fields.Many2one('promasy.tenant', string='Tenant')
    property_id = fields.Many2many('promasy.property', string='Property')
    owner_id = fields.Many2one('promasy.owner', string='Owner')
    contract_id = fields.Many2one('promasy.contract', string='Contract')
    expiry_date = fields.Date(string='Expiry Date')
    notes = fields.Text(string='Notes')