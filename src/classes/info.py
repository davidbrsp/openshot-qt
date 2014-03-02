""" 
 @file
 @brief This file contains the current version number of OpenShot, along with other global settings.
 @author Jonathan Thomas <jonathan@openshot.org>
 
 @section LICENSE
 
 Copyright (c) 2008-2014 OpenShot Studios, LLC
 (http://www.openshotstudios.com). This file is part of
 OpenShot Video Editor (http://www.openshot.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.
 
 OpenShot Video Editor is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with OpenShot Library.  If not, see <http://www.gnu.org/licenses/>.
 """
 
import os

VERSION             = "2.0.0"
DATE                = "20130602800000"
NAME                = 'openshot'
GPL_VERSION         = '3'
SUPPORTED_LANGUAGES = ['English', 'Dutch', 'French', 'German', 'Italian', 'Portuguese', 'Spanish', 'Swedish']
PATH = os.path.dirname(os.path.dirname( os.path.realpath( __file__) )) # Primary openshot folder

# names of all contributers, using 'u' for unicode encoding
AF   = {'name': u'Andy Finch', 'email': 'we.rocked.in79@gmail.com'}
NF   = {'name': u'Noah Figg', 'email': 'eggmunkee@hotmail.com'}
JT   = {'name': u'Jonathan Thomas', 'email': 'jonathan@openshot.org'}
OG   = {'name': u'Olivier Girard', 'email': 'eolinwen@gmail.com'}
CP   = {'name': u'Cody Parker', 'email': 'cody@yourcodepro.com'}


#credits
CREDITS = {
    'code'          : [JT, NF, AF, CP, OG],
    'artwork'       : [JT],
    'documentation' : [JT],
    'translation'   : [OG],
}

SETUP   = {
    'name'              : NAME,
    'version'           : VERSION,
    'author'            : JT['name'] + ' and others',
    'author_email'      : JT['email'],
    'maintainer'        : JT['name'],
    'maintainer_email'  : JT['email'],
    'url'               : 'http://www.openshot.org/',
    'license'           : 'GNU GPL v.' + GPL_VERSION,
	'description'	   : 'Create and edit videos and movies',
	'long_description'  : "Create and edit videos and movies\n OpenShot Video Editor is a free, open-source, non-linear video editor.  It\n can create and edit videos and movies using many popular video, audio, and\n image formats.  Create videos for YouTube, Flickr, Vimeo, Metacafe, iPod,\n Xbox, and many more common formats!\n .\n Features include:\n  * Multiple tracks (layers)\n  * Compositing, image overlays, and watermarks\n  * Support for image sequences (rotoscoping)\n  * Key-frame animation\n  * Video and audio effects (chroma-key)\n  * Transitions (lumas and masks)\n  * 3D animation (titles and simulations)\n  * Upload videos (YouTube and Vimeo supported)",
		 

# see http://pypi.python.org/pypi?%3Aaction=list_classifiers
    'classifiers'       : [          
                           'Development Status :: 5 - Production/Stable',
                           'Environment :: X11 Applications',
                           'Environment :: X11 Applications :: GTK',
                           'Intended Audience :: End Users/Desktop',
                           'License :: OSI Approved :: GNU General Public License (GPL)',
                           'Operating System :: OS Independent',
                           'Operating System :: POSIX :: Linux',
                           'Programming Language :: Python',
                           'Topic :: Artistic Software',
                           'Topic :: Multimedia :: Video :: Non-Linear Editor',] +
                          ['Natural Language :: ' + language for language in SUPPORTED_LANGUAGES
                          ],
}
