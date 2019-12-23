from setuptools import setup, find_packages
import os

fname = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(fname) as f:
    install_requires = [l.strip() for l in f.readlines()]

setup(
    name='autox',
    version='0.2.1',
    url='https://github.com/zatena/autox.git',
    packages=find_packages(exclude=['autox.case']),
    author='echoz',
    keywords='automatic api test python',
    author_email='zatena@163.com',
    description='api test',
    long_description='an automatic test platform',
    install_requires=install_requires,
    include_package_data=True,

)
