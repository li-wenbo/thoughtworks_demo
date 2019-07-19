#! *-* utf-8 *-*
"""
    test_flask.py
    ~~~~~~~~~

    so the unit test case should be here

    :copyright:
    :license:
"""
import unittest

from flask_testing import TestCase

import server


class MyTest(TestCase):
    def create_app(self):
        app = server.app
        app.config['TESTING'] = True
        return app

    def test_index(self):
        """
        test route '/'
        :return:
        """
        with self.app.test_client() as c:
            rv = c.get('/')
            self.assert200(rv, 'index error')


if __name__ == '__main__':
    unittest.main(verbosity=2)
