from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requires = []
    for line in f:
        req = line.strip()
        if "#egg=" in req:
            req_url, req_name = req.split("#egg=")
            req_str = f"{req_name} @ {req_url}"
        else:
            req_str = req
        requires.append(req_str)

setup(
    name="ondewo-vtsi-client",
    version='6.5.0',
    author="Ondewo GbmH",
    author_email="office@ondewo.com",
    description="exposes the ondewo-vtsi endpoints in a user-friendly way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ondewo/ondewo-vtsi-client-python",
    packages=[
        np
        for np in filter(
            lambda n: n.startswith('ondewo.') or n == 'ondewo',
            find_packages()
        )
    ],
    include_package_data=True,
    package_data={
        'ondewo.vtsi': ['py.typed', '*.pyi'],
        'ondewo.nlu': ['py.typed', '*.pyi'],
        'ondewo.qa': ['py.typed', '*.pyi'],
        'ondewo.s2t': ['py.typed', '*.pyi'],
        'ondewo.t2s': ['py.typed', '*.pyi'],
        'ondewo.csi': ['py.typed', '*.pyi'],
        'ondewo.sip': ['py.typed', '*.pyi'],
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3',
    install_requires=requires,
)
