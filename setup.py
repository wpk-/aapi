import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='aapi',
    version='0.1.1',
    description='Een typed interface voor de data API van de Gemeente'
                ' Amsterdam.',
    long_description=read('README.md'),
    url='https://github.com/wpk-/aapi',
    author='Paul Koppen',
    author_email='p.koppen@amsterdam.nl',
    keywords=['api', 'amsterdam'],
    license='MIT',
    packages=['aapi'],
    install_requires=[
        'orjson',
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Dutch',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Database :: Front-Ends',
        'Topic :: Scientific/Engineering'
            ' :: Interface Engine/Protocol Translator',
        'Topic :: System :: Networking',
        'Typing :: Typed',
    ]
)
