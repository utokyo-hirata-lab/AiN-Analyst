from setuptools import setup

setup(
    name='AiN-Analyst',
    version='0.1.2',
    author='Wataru Takahagi',
    author_email='watarut@eqchem.s.u-tokyo.ac.jp',
    url='https://github.com/utokyo-hirata-lab/Analyst',
    py_modules=['hrtlab_core'],
    description='Analysis tools for Attom, iCap TQ and Nu Plasma 2',
    keywords='visualization data-science',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
