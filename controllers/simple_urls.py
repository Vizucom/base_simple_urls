# -*- coding: utf-8 -*-
from openerp.addons.web import http
from openerp.addons.web.http import request
import werkzeug
import logging

_logger = logging.getLogger(__name__)


class SimpleUrlController(http.Controller):

    @http.route('/redirect', type='http', auth="user")
    def redirect(self, **args):

        ''' Check that the url contains only one GET parameter '''
        if len(args) != 1:
            _logger.debug("Wrong number of GET parameters ({})".format(args))
            return werkzeug.utils.redirect('/web')

        key, value = args.popitem()

        rule_model = request.env['base_simple_urls.redirect_rule']
        matching_rule = rule_model.search([('get_variable', '=', key)])

        if not matching_rule:
            _logger.debug("Redirect rule for GET parameters not found ({})".format(args))
            return werkzeug.utils.redirect('/web')

        ''' Do a case insensitive search to the model and field defined in the
        redirect rule, e.g. product.product's default_code field '''
        target_model = request.env[matching_rule[0].model_id.model]
        matching_ids = target_model.search([(matching_rule[0].field_id.name, '=ilike', value)])

        if len(matching_ids) != 1:
            _logger.debug("Wrong number of search results. GET parameters: {}".format(args))
            return werkzeug.utils.redirect('/web')

        url_params = {
            'view_type': 'form',
            'model': matching_rule[0].model_id.model,
            'id': matching_ids[0].id,
            'action': matching_rule[0].action_id.id,
        }

        url_string = '/web#{}'.format(werkzeug.url_encode(url_params))
        return werkzeug.utils.redirect(url_string)