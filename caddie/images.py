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
import PIL.ImageFilter
from colormath.color_objects import sRGBColor

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

    def crop_color_subimage(self):
        """
        Crop the edges from a image. This is appropriate if the image is a
        pallette swatch, and we only want the center colored part.
        """

        width, height = self.get_dimensions()
        toreturn = CaddieImage('.')
        toreturn._image = self._image.crop((0.2 * width, 0.3 * height, 0.8 * width, 0.7 * height))
        return toreturn

    def get_swatch_color(self):
        """
        Return the color for a color swatch.
        """
        scratch = self.crop_color_subimage()._image
        for _ in range(3):
            scratch = scratch.filter(PIL.ImageFilter.BoxBlur(11))
        scratch = scratch.filter(PIL.ImageFilter.MedianFilter(5))
        center = (scratch.size[0]/2, (scratch.size[1]/2))
        center_pixel = scratch.getpixel(center)
        return sRGBColor(center_pixel[0], center_pixel[1], center_pixel[2], False)
