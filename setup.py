from setuptools import setup

setup(name='pykazi',
      version='0.1',
      description='Python connector for Kazi smart contract.',
      url='http://github.com/onepercentclub/pykazi',
      author='Loek van Gent',
      author_email='loek@onepercentclub.com',
      license='MIT',
      packages=['pykazi'],
      install_requires=[
          'ethereum-ipc-client',
      ],
      zip_safe=False)

