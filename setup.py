from setuptools import setup

setup(name='federalholiday',
      version='1.0',
      description='returns if a date is a US Federal Holiday',
      url='https://lamplightlab.com',
      author='Matthew McElhaney',
      author_email='matt@lamplightlab.com',
      license='MIT',
      packages=['federalholiday'],
      install_requires=['datetime'],
      zip_safe=False)
