import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requires = f.read().splitlines()

setuptools.setup(
    name="ONDEWO VTSI Client Python",
    version="1.2.1",
    author="Ondewo GbmH",
    author_email="info@ondewo.com",
    description="sends deployment commands to the Ondewo VTSI Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ondewo/ondewo-vtsi-client-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.0.1",
    install_requires=requires,
)
