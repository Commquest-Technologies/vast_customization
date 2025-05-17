from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vast_customization/__init__.py
from vast_customization import __version__ as version

setup(
	name="vast_customization",
	version=version,
	description="Custom Apps for VAST Group",
	author="Commquest Technologies (Pty) Ltd.",
	author_email="info@commquest.co.za",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
