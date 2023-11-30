from RailsStringMethods import underscore

def render_setup_py(module_name):
    content = f"""
    from distutils.core import setup

    setup(
        name='{module_name}',
        packages=[],
        version = '0.1',
        license='MIT',
        description = 'Write your package description here!',
        author = 'Your Name',
        author_email = 'yourname@email.com',
        url = 'https://github.com/username/{module_name}',
        download_url = 'https://github.com/username/{module_name}/archive/refs/tags/v_0.1.tar.gz',
        keywords = [],
        install_requires=[],
        {f"""
        entry_points='''
                [console_scripts]
                for={module_name.underscore()}:cli
            ''',
        """}
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
    """

    return content