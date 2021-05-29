
from setuptools import setup, find_packages


setup(
    long_description=open("README.md", "r").read(),
    name="loraspi",
    version="1.5",
    description="library for ",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/nbdy/loraspi",
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License'
    ],
    keywords="wardriving tool raspberry pi",
    packages=find_packages(),
    install_requires=[
        "scapy", "gpsd-py3", "loguru", "btpy", "spidev", "Pillow", "dataset", "pyrunnable", "pyclsload"
    ],
    entry_points={
        'console_scripts': [
            'pwnpy = pwnpy.__main__:main'
        ]
    },
    package_data={
        "pwnpy": ["modules/*"]
    },
    long_description_content_type="text/markdown",
)