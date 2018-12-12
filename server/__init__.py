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

import io
import sys
import os
sys.path.append('../caddie')

import cherrypy
import PIL.Image

class CaddieServer(object):
    @cherrypy.expose
    def index(self):
        """
        Static index page.
        """
        return "Caddie index."

    @cherrypy.expose
    def upload_image(self, file=None):
        """
        Upload an image. Some restrictions apply.
        """
        if cherrypy.request.method == 'POST':

            fhandle = None

            # Testing purposes, pass POST data as a custom header.
            for header in cherrypy.request.headers:
                value = cherrypy.request.headers[header]
                if header == 'Fake-Data':
                    fhandle = open(value, 'rb')

            if file:
                fhandle = file.file

            if not fhandle:
                toreturn = "Did not detect an uploaded file."
                return toreturn

            else:

                im = PIL.Image.open(io.BytesIO(fhandle.read()))
                im_format = im.format
                im_size = im.size

                toreturn = "Accepted %s (%dx%d)" % (im_format, im_size[0], im_size[1])
                return toreturn

        else:
            default_response = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><HTML>
    <HEAD><TITLE>Upload new File</TITLE></HEAD>
    <BODY>
        <H1>Upload new file</H1>
        <FORM method=post enctype=multipart/form-data><P>
                <INPUT type=file name=file />
                <INPUT type=submit value=Upload />
        </P></form>
    </BODY>
    </HTML>
    """
            return default_response
