# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Simple URLs',
    'category': 'Utilities',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['web'],
    'description': """
Simple URLs
===========
* Makes it possible to create redirection rules so that users can access Odoo pages with simpler URLs.
* E.g. a rule could be created to have URL http://<odoo url>:<port>/redirect?pr=<product's internal reference> point to a product's form view instead of using the normal http://<odoo url>:<port>/web#id=13238&view_type=form&model=product.product&menu_id=283&action=360
* Rules are freely configurable in Settings menu by users that have Technical Features access rights

""",
    'data': [
        'views/redirect_rule.xml',
    ],
}
