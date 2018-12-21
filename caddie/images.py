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
import tesserocr

from PIL import ImageFont, ImageDraw


class CaddieImage:
    def __init__(self, filename):
        """
        Handle for image specified by filename.
        """
        self._filename = filename
        if self._filename is not None:
            self._filename = os.path.abspath(self._filename)

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


class SingleSwatch(CaddieImage):

    def __init__(self, filename):
        """
        A single swatched tile.
        """
        super(SingleSwatch, self).__init__(filename)

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

    def guess_colorname(self):
        """
        Simple extraction of swatch color name.
        """
        return tesserocr.image_to_text(self._image)


    @classmethod
    def generate_swatch(cls, swatch_name, swatch_rgb):
        """
        Generate a tidy-looking swatch.
        """
        mode = 'RGB'
        img_w = 200
        img_h = 100

        bgcolor = 'grey'

        canvas = PIL.Image.new(mode, (img_w, img_h), bgcolor)

        noto = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf', 24)
        drawer = ImageDraw.Draw(canvas)

        fontcolor = (222,222,222)

        label_w, label_h = drawer.textsize(swatch_name, noto)

        drawer.text((img_w/2 - label_w/2, 8), swatch_name, fontcolor, font=noto)
        drawer.rectangle([(16, 16 + label_h), (img_w-16, img_h-16)], fill=swatch_rgb)

        canvas.save('/tmp/swatch_%s.png' % swatch_name)

        toreturn = cls.from_image(canvas)
        return toreturn

    @staticmethod
    def from_image(image):
        """
        Factory : Create a SingleSwatch from an image.
        """
        toreturn = SingleSwatch(None)
        toreturn._image = image
        return toreturn

class MultiSwatch(CaddieImage):

    def __init__(self, filename):
        """
        A sheet of multiple swatches.
        """
        super(MultiSwatch, self).__init__(filename)

    def split_swatches(self, count_horiz, count_vert):
        """
        Split a sheet multi-swatch into
        """
        raise Exception("Not implemented.")
