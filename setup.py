from setuptools import setup, find_packages
setup(
    name="plutoPy",
    version="1.0.3",
    packages=['plutoPy', 'plutoPy.model'],
	install_requires=['sqlalchemy', 'plutoDbPy'],
)