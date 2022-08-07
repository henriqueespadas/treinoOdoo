# Copyright 2022 Eva Alexandrina Tecnologia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class SacMotivo(models.Model):

    _name = "sac.motivo"
    _description = "Sac Motivo"  # TODO

    name = fields.Char()
