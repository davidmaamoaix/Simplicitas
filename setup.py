''' Installer for the package. '''

import pathlib
from setuptools import find_packages, setup

PATH = pathlib.Path(__file__).parent

README = (PATH / "README.md").read_text()

setup(
	name = 'simplicitas',
	version = '1.0.0',
	description = 'A simple yet useful desktop util.',
	long_description = README,
	long_description_content_type = "text/markdown",
	url = 'https://github.com/davidmaamoaix/Simplicitas',
	author = 'David Ma',
	author_email = "davidma@davidma.cn",
	license = 'MIT',
	packages = find_packages(),
	include_package_data = True,
)