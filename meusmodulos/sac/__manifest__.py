# Copyright 2022 Espadas
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Sac',
    'summary': """
        SAC - Servico de Atendimento ao Cliente""",
    'version': '13',
    'license': 'AGPL-3',
    'author': 'Espadas,Odoo Community Association (OCA)',
    'depends': [
        'mail',
    ],
    'data': [
        'security/sac_motivo.xml',
        'security/sac_ticket.xml',
        'data/sac_sequence.xml',
        'views/sac_menu.xml',
        'views/sac_motivo.xml',
        'views/sac_ticket.xml',
    ],
    'demo': [
        'demo/sac_motivo.xml',
        'demo/sac_ticket.xml',
    ],
}
