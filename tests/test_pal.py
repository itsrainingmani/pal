# Content of test_helpers.py

import sys
import pal.app as pal
from pathlib import Path


def test_get_license_file_path():
    homePath = str(Path.home())
    if sys.platform.startswith("linux"):
        # Linux-specific path
        testPath = homePath + "/repos/pal/data/license-list.json"
    elif sys.platform.startswith("win"):
        testPath = homePath + "\\dev\\pal\\data/license-list.json"
    assert testPath == pal.get_license_file_path()


def test_retrieve_license_list():
    testLicenseList = sorted(
        [
            "mpl-2.0",
            "mit",
            "lgpl-3.0",
            "gpl-2.0",
            "bsd-2-clause",
            "apache-2.0",
            "unlicense",
            "lgpl-2.1",
            "bsd-3-clause",
            "epl-2.0",
            "gpl-3.0",
            "agpl-3.0",
        ]
    )

    assert testLicenseList == pal.retrieve_license_list()
