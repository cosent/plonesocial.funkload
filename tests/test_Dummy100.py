# -*- coding: iso-8859-15 -*-
"""microblog FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase


class Dummy100(FunkLoadTestCase):
    """
    Test ZODB insertion via bare helper view.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')

    def test_dummy100(self):
        self.get(self.server_url + '/Plone/@@microblog_funkload?dummy100')

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")

if __name__ in ('main', '__main__'):
    unittest.main()
