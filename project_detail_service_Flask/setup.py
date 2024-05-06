from setuptools import setup, find_packages

setup(
    name='project_detail_service_Flask',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'sqlalchemy',
    ],
)