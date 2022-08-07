# Copyright 2022 Eva Alexandrina Tecnologia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class SacTicket(models.Model):

    _name = "sac.ticket"
    _description = "Sac Ticket"  # TODO

    name = fields.Char()

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


