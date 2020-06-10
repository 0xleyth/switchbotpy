from distutils.core import setup
setup(
    name='switchbotpy',
    packages=['switchbotpy'],
    version='0.1',
    license='MIT',
    description='An API for Switchbots that allows to control actions, settings and timers (also password protected)',
    author='Nicolas Küchler',
    author_email='nico.kuechler@protonmail.com',
    url='https://github.com/RoButton/switchbotpy',
    download_url='https://github.com/RoButton/switchbotpy/archive/v_01.tar.gz',
    keywords=['Switchbot', 'Ble', 'Button', 'Actions', 'Settings', 'Timers'],
    install_requires=['pygatt',],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)