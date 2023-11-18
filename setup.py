from distutils.core import setup

setup(
  name='ModuleMaker',
  packages=['export', 'new', 'push', 'setup', 'support'],
  version = '0.1',
  license='MIT',
  description = 'Makes creating PyPi modules much easier, and provides a number of helpful commands to publish and maintain your package.',
  author = 'KayLa Thomas',
  author_email = 'kaylathomas.dev@gmail.com',
  url = 'https://github.com/kaylathomas/ModuleMaker',
  download_url = 'https://github.com/kaylathomas/ModuleMaker/archive/refs/tags/v_0.1.tar.gz',
  keywords = ['module', 'python', 'pypi', 'generate', 'update', 'scaffold'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
