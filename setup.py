# ----------------------------------------------------------------------------
# Copyright (c) 2024, Stephanie Hereira.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = (
    "Shorter description"
)

setup(
    name="q2-dwq2",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="Stephanie Hereira",
    author_email="shereirap@gmail.com",
    description=description,
    url="https:://example.com",
    entry_points={
        "qiime2.plugins": [
            "q2_dwq2="
            "q2_dwq2"
            ".plugin_setup:plugin"]
    },
    package_data={
        "q2_dwq2": ["citations.bib"],
        "q2_dwq2.tests": ["data/*"],
    },
    zip_safe=False,
)
