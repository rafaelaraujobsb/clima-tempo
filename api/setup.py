import io
import re

from setuptools import find_packages, setup


dev_requirements = [
    'bandit',
    'pylama',
    'isort',
    'pytest',
]

unit_test_requirements = [
    'pytest',
]

run_requirements = [
    "uvicorn[standard]==0.13.4",
    "gunicorn==20.1.0",
    "loguru==0.5.3",
    "urllib3==1.26.4",
    "fastapi==0.63.0",
    "pymongo==3.11.3",
]

with io.open('./api_clima_tempo/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="api_clima_tempo",
    version=version,
    author="Rafael Araujo",
    author_email="bsb.rafaelaraujo@gmail.com.br",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="https://github.com/rafaelaraujobsb/clima-tempo",
    license="COPYRIGHT",
    description="O projeto é para capturar dados do tempo dos municípios cadastrados e expor os"
                " dados através de uma API",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
    },
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8'
    ],
    keywords=()
)
