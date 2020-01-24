import os

from setuptools import setup, find_packages


_HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_HERE, 'README.md'), 'r') as f:
    long_desc = f.read()

setup(
    name='hyp3lib',
    use_scm_version=True,
    description='HyP3 common library plugin',
    long_description=long_desc,
    long_description_content_type='text/markdown',

    url='https://github.com/asfadmin/hyp3-lib',

    author='ASF APD/Tools Team',
    author_email='uaf-asf-apd@alaska.edu',

    license='GPLv3',
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        ],

    install_requires=[
        'importlib_metadata',
    ],

    packages=find_packages(),

    # TODO: add all scripts with optparse or argparse parsers
    # entry_points={'console_scripts': [
    #     'hyp3_autorift = hyp3_autorift.__main__:main',
    #     ]
    # },

    zip_safe=False,
)
