from setuptools import setup

package_name = 'py_srvcli'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='Python service and client example with custom interface',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = py_srvcli.server:main',  # server.py'deki main fonksiyonuna işaret ediyor
            'client = py_srvcli.client:main',  # client.py'deki main fonksiyonuna işaret ediyor
        ],
    },
)
