from setuptools import setup

setup(
  name='parse_fdw',
  version='0.1.0',
  author='Kashif Rasul',
  author_email='kashif.rasul@gmail.com',
  license='Postgresql',
  packages=['parse_fdw'],
  url='https://github.com/spacialdb/parse_fdw',
  install_requires=['multicorn', 'parse_rest'],
  dependency_links=['https://github.com/dgrtwo/ParsePy/tarball/master#egg=parse_rest-0.2.20141004'],
  license='MIT',
  keywords='parse fdw postgresql'
)
