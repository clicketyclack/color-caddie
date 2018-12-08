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

import os
import PIL.Image

class CaddieImage:
    def __init__(self, filename):
        """
        Handle for image specified by filename.
        """
        self._filename = os.path.abspath(filename)
        self._image = None


    def load(self):
        """
        Load image from file system.
        """
        self._image = PIL.Image.open(self._filename)

    def get_dimensions(self):
        """
        Return image dimensions.
        """
        return self._image.size
