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

sys.path.append('../')

from caddie.images import CaddieImage
from caddie import ROOT_PATH

class TestImageReader(unittest.TestCase):

    def test_simple_read(self):
        filename = os.path.join(ROOT_PATH, 'media/copic_subset.png')
        ci = CaddieImage(filename)
        ci.load()
        self.assertEquals(ci.get_dimensions(), (680, 875), "Successfully get image dimensions.")

if __name__ == '__main__':
    unittest.main()
