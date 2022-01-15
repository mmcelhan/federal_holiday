from setuptools import setup

setup(name='federal_holiday',
      version='1.0',
      description='returns if a date is a US Federal Holiday',
      url='https://lamplightlab.com',
      author='Matthew McElhaney',
      author_email='matt@lamplightlab.com',
      license='MIT',
      packages=['federal_holiday'],
      install_requires=['datetime'],
      zip_safe=False)
