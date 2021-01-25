import pathlib
from setuptools import setup, find_packages

import versioneer

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

install_requires = [
            'pandas==1.1.5',
        ]

from happy_python_utils import version

setup(
  name="my_happy_modin",
  version=versioneer.get_version(),
  description="The simple version for modin.",
  long_description=README,
  long_description_content_type="text/markdown",
  license="Apache 2",
  url="https://github.com/ggservice007/my-happy-modin",
  author="ggservice007",
  author_email="ggservice007@126.com",
  packages=find_packages(where="src"),
  package_dir={"": "src"},
  install_requires=install_requires,
  include_package_data=True,
  zip_safe=False,
  python_requires=">=3.7.7"
)
