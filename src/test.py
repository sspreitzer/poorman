'''
    poorman - A poor man's cluster written in Python
    Copyright (C) 2014   Swiss Confederation
    Federal Department of Home Affairs FDHA
    Federal Office of Meteorology and Climatology MeteoSwiss
    
    Sascha Spreitzer <sascha.spreitzer@meteoswiss.ch>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) alny later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

import poorman

if __name__ == '__main__':
    client = poorman.Client(0)
    server = poorman.Server(0)
    