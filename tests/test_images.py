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

"""
Verify ImageReader class.
"""

import unittest
import os
import sys

from colormath.color_objects import sRGBColor
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_conversions import convert_color


sys.path.append('../')

from caddie.images import CaddieImage
from caddie import ROOT_PATH

class TestImageReader(unittest.TestCase):
    """
    Verify ImageReader class.
    """

    def test_simple_read(self):
        """
        Test simple image loading.
        """
        filename = os.path.join(ROOT_PATH, 'media/copic_subset.png')
        ci = CaddieImage(filename)
        ci.load()
        self.assertEqual(ci.get_dimensions(), (680, 875), "Successfully get image dimensions.")

    def test_swatch_crop(self):
        """
        Verify that we can crop the color part of a swatch.
        """
        filename = os.path.join(ROOT_PATH, 'media/single_tile_BG53.png')
        ci = CaddieImage(filename)
        ci.load()
        dims_pre = ci.get_dimensions()
        cropped = ci.crop_color_subimage()

        dims_post = cropped.get_dimensions()
        size_pre = dims_pre[0] * dims_pre[1]
        size_post = dims_post[0] * dims_post[1]
        self.assertTrue(size_post < 0.5 * size_pre, "Successfully crop an image. ")
        self.assertTrue(size_post > 100, "Successfully crop an image, but not the entire thing.")


    def test_swatch_color(self):
        """
        Verify that we can extract the color from a color swatch.
        """
        filename = os.path.join(ROOT_PATH, 'media/single_tile_BG53.png')
        swatch_bg53 = CaddieImage(filename)
        swatch_bg53.load()

        filename = os.path.join(ROOT_PATH, 'media/single_tile_P84.png')
        swatch_p84 = CaddieImage(filename)
        swatch_p84.load()


        color_bg53 = swatch_bg53.get_swatch_color()
        expected_bg53 = sRGBColor(0x23, 0x83, 0x65) # Manually determined with paint.net
        delta_bg53 = delta_e_cie2000(convert_color(color_bg53, LabColor), convert_color(expected_bg53, LabColor))
        self.assertTrue(delta_bg53 < 1.5, "Can extract BG53 color.")

        color_p84 = swatch_p84.get_swatch_color()
        expected_p84 = sRGBColor(0xdf, 0xab, 0xe3) # Manually determined with paint.net
        delta_p84 = delta_e_cie2000(convert_color(color_p84, LabColor), convert_color(expected_p84, LabColor))
        self.assertTrue(delta_p84 < 1.5, "Can extract P84 color.")



if __name__ == '__main__':
    unittest.main()
