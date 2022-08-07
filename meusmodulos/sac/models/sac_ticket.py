# Copyright 2022 Eva Alexandrina Tecnologia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class SacTicket(models.Model):

    _name = "sac.ticket"
    _description = "Sac Ticket"  # TODO

    name = fields.Char(
        default=lambda self: _('New'),
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
    )
    partner_name = fields.Char(
        string="Nome",
    )
    partner_gender = fields.Selection(
        [
            ('m', 'Masculino'),
            ('f', 'feminino')
        ]
    )
    partner_birthday = fields.Date()
    partner_phone = fields.Char()
    partner_email = fields.Char()
    mensagem = fields.Text()
    create_date = fields.Date(
        readonly=True,
    )
    state_id = fields.Many2one(
        'res.country.state',
        domain=[
            ('country_id.code', '=', 'BR'),
        ]
    )
    city = fields.Char()
    motivo_id = fields.Many2one(
        'sac.motivo'
    )

    @api.onchange('partner_id')
    def onchange_method(self):
        if self.partner_id:
            self.partner_name = self.partner_id.name
            self.partner_phone = self.partner_id.phone
            self.partner_email = self.partner_id.email

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sac') or ('New')
        return super(SacTicket, self).create(vals)

