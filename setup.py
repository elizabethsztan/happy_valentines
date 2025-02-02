from setuptools import setup, find_packages

setup(
    name="happy_valentines",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>1.0.0",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "happy_valentines=happy_valentines.main:main",
        ],
    },
    author="Liz Tan",
    author_email="elizabethsztan@gmail.com",
    description="A package that generates daily love poems using gpt-4o.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)