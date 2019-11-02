import setuptools

setuptools.setup(
    name='initerm2',
    version='0.2.2',
    url='https://github.com/ken0x0a/itermocil',
    license='MIT',
    description=
    'Create pre-defined window/pane layouts and run commands in iTerm',
    author='Tom Anthony',
    author_email='',
    packages=setuptools.find_packages(),
    py_modules=['initerm2'],
    package_data={},
    classifiers=[],
    entry_points={'console_scripts': [
        'initerm2 = initerm2.itermocil:main',
    ]},
    install_requires=[
        'PyYAML',
    ])
