#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Color Caddie - Helps you read the field and select your tools, but in a coloring context.
#
# Copyright (C) 2018 Erik Mossberg
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import unittest
import os
import sys

import cherrypy
from cherrypy.test import helper

sys.path.append('../')

from server import CaddieServer

from caddie import ROOT_PATH

class TestServerUpload(helper.CPWebCase):
    
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(CaddieServer())


    def test_upload_should_show_resolution(self):
        """
        Test an image upload.
        """

        # Testing purposes, pass POST data as a custom header.
        post_fname = os.path.join(ROOT_PATH, "./media/single_tile_BG53.png")
        headers = []
        headers.append(('Fake-Data', post_fname))

        _, _, body = self.getPage("/upload_image", headers=headers, method="POST")

        self.assertTrue("Accepted PNG (144x205)" in body.decode("utf-8"))

    def test_get_should_return_form(self):
        """
        Verify that simple get of page without arguments provides an upload form.
        """
        status, _, body = self.getPage("/upload_image")
        self.assertTrue('200 OK' in status)
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')
        self.assertTrue('Upload new file' in body.decode("utf-8"))



if __name__ == '__main__':
    unittest.main()
