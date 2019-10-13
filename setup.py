from setuptools import setup, find_packages

long_description = "chiron"

setup(
    name='chiron-bot',

    version='0.9.0',
    description='chat bot that can look up ticket numbers on bugtrackers and return their names',
    long_description=long_description,
    url='https://github.com/sipb/chiron',

    author='Alex Dehnert and SIPB',
    author_email='chiron@mit.edu',

    #license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: MIT License',
	'Environment :: No Input/Output (Daemon)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat',
    ],

    packages=['chiron_bot'],

    install_requires=['lxml', 'requests[security]', 'backports.csv;python_version<"3"'],
    extras_require={
        #'zephyr': ['-r requirements.zephyr.txt'],
        'test': ['unittest-xml-reporting'],
        #'test': ['coverage'],
        'zulip': ['zulip'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'chiron=chiron_bot.main:main',
        ],
    },
)
