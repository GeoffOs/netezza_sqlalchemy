import os
import re

from setuptools import setup

v = open(os.path.join(os.path.dirname(__file__), 'sqlalchemy_netezza', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.rst')


setup(name='sqlalchemy_netezza',
      version=VERSION,
      description="Netezza for SQLAlchemy - from https://github.com/deontologician/netezza_sqlalchemy",
      long_description=open(readme).read(),
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: CPython',
      'Topic :: Database :: Front-Ends',
      ],
      keywords='SQLAlchemy Netezza',
      author='Geoff Osbaldestin',
      author_email='geoff@osbaldestin.net',
      license='MIT',
      packages=['sqlalchemy_netezza'],
      include_package_data=True,
      tests_require=['nose >= 0.11'],
      test_suite="nose.collector",
      zip_safe=False,
      entry_points={
         'sqlalchemy.dialects': [
              'netezza = sqlalchemy_netezza.pyodbc:NetezzaDialect_pyodbc',
              'netezza.pyodbc = sqlalchemy_netezza.pyodbc:NetezzaDialect_pyodbc',
              ]
        }
)