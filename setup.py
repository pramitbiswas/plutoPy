from setuptools import setup, find_packages
setup(
    name="plutoPy",
    version="0.1.4",
    packages=['plutoPy', 'plutoPy.model'],
	install_requires=['sqlalchemy', 'pypyodbc'],
)