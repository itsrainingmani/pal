import os
import json

LICENSE_FILE = "data/license-list.json"

# Function to get the path of the License Path
def get_license_file_path():
    projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    licensePath = os.path.join(projectPath, LICENSE_FILE)
    return licensePath


# Function to get a list of licenses from the license list file
def retrieve_license_list():
    licensePath = get_license_file_path()
    licenseList = []
    with open(licensePath, "r", encoding="utf-8") as licFile:
        licenses = json.load(licFile, encoding="utf-8")
        for lic in licenses:
            licenseList.append(lic["key"])
    return sorted(licenseList)


def main():
    pass


if __name__ == "__main__":
    # main()
    get_license_file_path()
