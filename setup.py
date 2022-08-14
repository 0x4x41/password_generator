import setuptools

setuptools.setup(
    name="pgen",
    version="0.0.1",
    description="A basic password generator",
    url="https://github.com/0x4x41/password_generator",
    author="Mark Sercombe",
    packages=setuptools.find_packages(),
    entry_points = {'console_scripts': ['pgen = pgen:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]

)