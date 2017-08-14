from setuptools import setup, find_packages


setup(
    name="punk",

    version="0.1.0",

    description="Primitives for Uncovering New Knowledge.",
    long_description="Machine Learning pipeline elements.",

    url="https://github.com/alejandrox1/punk",

    author="New Knowledge",
    author_email="alarcj137@gmail.com",

    license="MIT",

    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.6",
    ],

    keywords="TA1 primitive",


    packages=find_packages(exclude=['tests']),

    install_requires=["numpy", "scikit-learn", "scipy"],


)
