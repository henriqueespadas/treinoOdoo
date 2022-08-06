# Copyright 2022 Eva Alexandrina Tecnologia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class SacTicket(models.Model):

    _name = "sac.ticket"
    _description = "Sac Ticket"  # TODO

    name = fields.Char()
