#!/bin/sh

if [ "x$1" = "x--i-really-know-what-im-doing" ] ; then
  echo Proceeding as requested by command line ...
else
  echo "*** Please run again with --i-really-know-what-im-doing ..."
  exit 1
fi

tmp=`mktemp -d`

hg clone https://code.google.com/p/carve/ $tmp/carve

for p in `cat ./patches/series`; do
  echo "Applying patch $p..."
  cat ./patches/$p | patch -d $tmp/carve -p1
done

find include -type f -not -iwholename '*.svn*' -exec rm -rf {} \;
find lib -type f -not -iwholename '*.svn*' -exec rm -rf {} \;

cat "files.txt" | while read f; do
  mkdir -p `dirname $f`
  cp $tmp/carve/$f $f
done

rm -rf $tmp

sources=`find ./lib -type f -iname '*.cc' -or -iname '*.cpp' -or -iname '*.c' | sed -r 's/^\.\//\t/' | sort -d`
headers=`find ./lib -type f -iname '*.h' -or -iname '*.hpp' | sed -r 's/^\.\//\t/' | sort -d`
includes=`find ./include -type f -iname '*.h' -or -iname '*.hpp' | sed -r 's/^\.\//\t/' | sort -d`

cp patches/files/config.h include/carve/config.h
mkdir -p include/carve/random
cp patches/files/random.h include/carve/random/random.h

cat > CMakeLists.txt << EOF
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# The Original Code is Copyright (C) 2006, Blender Foundation
# All rights reserved.
#
# The Original Code is: all of this file.
#
# Contributor(s): Jacques Beaurai, Erwin Coumans
#
# ***** END GPL LICENSE BLOCK *****

# NOTE: This file is automatically generated by bundle.sh script
#       If you're doing changes in this file, please update template
#       in that script too

set(INC
	include
)

set(INC_SYS
)

set(SRC
	carve-capi.cc
	carve-util.cc
${sources}

	carve-capi.h
	carve-util.h
${headers}

${includes}
)

if(WITH_BOOST)
	if(NOT MSVC)
		# Boost is setting as preferred collections library in the Carve code when using MSVC compiler
		add_definitions(
			-DHAVE_BOOST_UNORDERED_COLLECTIONS
		)
	endif()

	add_definitions(
		-DCARVE_SYSTEM_BOOST
		-DHAVE_BOOST_LIBRARY
	)

	list(APPEND INC_SYS
		\${BOOST_INCLUDE_DIR}
	)
endif()

blender_add_lib(extern_carve "\${SRC}" "\${INC}" "\${INC_SYS}")
EOF
