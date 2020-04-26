from setuptools import setup, find_packages


def version():
    with open('v3iofs/__init__.py') as fp:
        for line in fp:
            if '__version__' in line:
                _, version = line.split('=')
                return version.replace("'", '').strip()


def load_deps(file_name):
    """Load dependencies from requirements file"""
    deps = []
    with open(file_name) as fp:
        for line in fp:
            line = line.strip()
            if not line or line[0] == '#':
                continue
            deps.append(line)
    return deps


install_requires = load_deps('requirements.txt')
tests_require = load_deps('dev-requirements.txt')

with open('README.md') as fp:
    long_desc = fp.read()

setup(
    name='v3iofs',
    version=version(),
    description='fsspec driver for v3io',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Iguazio',
    author_email='yaronh@iguazio.com',
    license='MIT',
    url='https://github.com/v3io/v3iofs-py',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    tests_require=tests_require,
)