# -*- coding: utf-8 -*-
# Copyright (C) 2010-2013 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Archive commands for the nomarch program."""
import os

def extract_arc (archive, compression, cmd, verbosity, outdir):
    """Extract an ARC archive."""
    # Since extracted files will be placed in the current directory,
    # the cwd argument has to be the output directory.
    cmdlist = [cmd, os.path.abspath(archive)]
    return (cmdlist, {'cwd': outdir})

def list_arc (archive, compression, cmd, verbosity):
    """List an ARC archive."""
    cmdlist = [cmd, '-l']
    if verbosity > 1:
        cmdlist.append('-v')
    cmdlist.append(archive)
    return cmdlist

def test_arc (archive, compression, cmd, verbosity):
    """Test an ARC archive."""
    return [cmd, '-t', archive]