# -*- coding: iso-8859-15 -*-
"""microblog FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload
from funkload.utils import Data
#from funkload.utils import xmlrpc_get_credential

class Home(FunkLoadTestCase):
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

    def test_home(self):
        server_url = self.server_url
        for i in xrange(100):
            self.get(server_url + "/Plone",
                     description="Get /Plone")

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")



if __name__ in ('main', '__main__'):
    unittest.main()
