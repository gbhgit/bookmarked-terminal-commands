from setuptools import setup

with open("README.md","r",encoding="utf-8") as readme_file:
    long_description=readme_file.read()

setup(
    name="btc",
    version="1.0.0",
    description="Bookmarked terminal commands, DEB packge",
    long_description=long_description,
    license="MIT",
    packages=['btc'],
    package_dir={'btc':'btc/'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux"
    ],
    entry_points={
        'console_scripts':['btc=btc.btc:main']
    },
    data_files=[
        ('share/applications/',['btc.desktop']),
    ],
    keywords="bookmarked terminal commands",
    python_requires=">=2.7.18",
)