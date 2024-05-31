from setuptools import setup, find_packages

setup(
    name='otp',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'sqlmodel',
        'pyotp',
        'pydantic-settings'
    ],
    entry_points={
        'console_scripts': [
            'otp = otp_generator.cli.entrypoint:otp',
        ],
    },
)
