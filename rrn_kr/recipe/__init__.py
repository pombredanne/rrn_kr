# -*- coding: utf-8 -*-
#
#   rrn_kr : ROK Resident Registry Number (RRN) validator
#   Copyright (C) 2016 mete0r <mete0r@sarangbang.or.kr>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import
from __future__ import unicode_literals


class Recipe:

    def __init__(self, buildout, name, options):
        pass

    def install(self):
        return tuple()

    def update(self):
        return tuple()


def uninstall(name, options):
    pass
