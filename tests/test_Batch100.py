# -*- coding: iso-8859-15 -*-
"""microblog FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase


class Batch100(FunkLoadTestCase):
    """
    Test ZODB insertion via bare helper view.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')

    def test_batch100(self):
        self.get(self.server_url + '/Plone/@@microblog_funkload?batch=100')

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")

if __name__ in ('main', '__main__'):
    unittest.main()
