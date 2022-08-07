# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
from totalvoice.cliente import Cliente


DEFAULT_ENDPOINT = 'api.totalvoice.com.br'


class SmsApi(models.AbstractModel):
    _inherit = 'sms.api'

    @api.model
    def _send_sms(self, numbers, message):
        account = self.env['iap.account'].get('sms')
        cliente = Cliente(account.account_token, DEFAULT_ENDPOINT)
        for number in numbers:
            cliente.sms.enviar(number, message)
