from distutils.core import setup
from setuptools import find_packages

setup(
  name='ModuleMaker',
  packages=find_packages(),
  version = '0.2',
  license='MIT',
  description = 'Makes creating PyPi modules much easier, and provides a number of helpful commands to publish and maintain your package.',
  author = 'KayLa Thomas',
  author_email = 'kaylathomas.dev@gmail.com',
  url = 'https://github.com/kaylathomas/ModuleMaker',
  download_url = 'https://github.com/kaylathomas/ModuleMaker/archive/refs/tags/v_0.2.tar.gz',
  keywords = ['module', 'python', 'pypi', 'generate', 'update', 'scaffold'],
  install_requires=[
      'FilesNFolders',
      'RailsStringMethods',
      'click'
  ],
  entry_points={
    'console_scripts': [
        'mm=module_maker_core:cli',
        'mm_new=new.main:new_command',
        'mm_export=export.main:export_command'
    ]
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.11',
  ],
)
