# -*- coding: iso-8859-15 -*-
"""microblog FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload
from funkload.utils import Data
#from funkload.utils import xmlrpc_get_credential

class Microblog(FunkLoadTestCase):
    """XXX

    This test use a configuration file Microblog.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')
        server_url = self.server_url
        # /tmp/tmpTJKroN_funkload/watch0001.request
        self.get(server_url + "/Plone/login",
            description="Get /Plone/login")
        # /tmp/tmpTJKroN_funkload/watch0035.request
        self.post(server_url + "/Plone/login_form", params=[
            ['came_from', ''],
            ['next', ''],
            ['ajax_load', ''],
            ['ajax_include_head', ''],
            ['target', ''],
            ['mail_password_url', ''],
            ['join_url', ''],
            ['form.submitted', '1'],
            ['js_enabled', '0'],
            ['cookies_enabled', ''],
            ['login_name', ''],
            ['pwd_empty', '0'],
            ['__ac_name', 'admin'],
            ['__ac_password', 'admin'],
            ['submit', 'Log in']],
            description="Post /Plone/login_form")

        # XXX here you can setup the credential access like this
        # credential_host = self.conf_get('credential', 'host')
        # credential_port = self.conf_getInt('credential', 'port')
        # self.login, self.password = xmlrpc_get_credential(credential_host,
        #                                                   credential_port,
        # XXX replace with a valid group
        #                                                   'members')

    def test_microblog(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin of test ---------------------------------------------

        # /tmp/tmpTJKroN_funkload/watch0081.request
        self.get(server_url + "/Plone",
            description="Get /Plone")
#        # /tmp/tmpTJKroN_funkload/watch0127.request
#        self.post(server_url + "/Plone/kss_z3cform_inline_validation?kukitTimeStamp=1335969520379", params=[
#            ['formname', 'activitystream_view'],
#            ['fieldname', 'form.widgets.text'],
#            ['value', 'Adding a microblog comment.'],
#            ['form.widgets.in_reply_to', ''],
#            ['form.widgets.author_name', ''],
#            ['form.widgets.author_email', ''],
#            ['form.widgets.text', 'Adding a microblog comment.'],
#            ['form.widgets.user_notification:list', 'selected']],
#            description="Post /Plone/kss_z3cform_inline_validation")
        # /tmp/tmpTJKroN_funkload/watch0128.request
        self.post(server_url + "/Plone/activitystream_view", params=[
            ['form.widgets.in_reply_to', ''],
            ['form.widgets.author_name', ''],
            ['form.widgets.author_email', ''],
            ['form.widgets.text', 'Adding a microblog comment.'],
            ['form.widgets.user_notification:list', 'selected'],
            ['form.buttons.status', 'Comment']],
            description="Post /Plone/activitystream_view")

        # end of test -----------------------------------------------

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")



if __name__ in ('main', '__main__'):
    unittest.main()
