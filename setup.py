#
# Copyright 2013 Roman Mohr <roman@fenkhuber.at>
#
# This file is part of sphinx-server.
#
# sphinx-server is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='sphinx-server',
      version='0.1.0a1',
      description='simple wsgi spinx server',
      author='Roman Mohr',
      author_email='roman@fenkhuber.at',
      url='https://github.com/rmohr/sphinx-server',
      setup_requires=[],
      install_requires=['static', 'setuptools'],
      tests_require=['pytest', 'webtest'],
      cmdclass={'test': PyTest},
      packages=['sphinxserver'],
      entry_points={
          'paste.app_factory': ['main=sphinxserver:app_factory'],
      },
      )
