import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nphiesify",
    version="0.0.2",
    author="Jassim Abdul Latheef",
    author_email="jassim@glance.care",
    description="Nphies FHIR middleware",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/groa-inc/nphiesify",
    project_urls={"Bug Tracker": "https://github.com/groa-inc/nphiesify/issues"},
    license="MIT",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.11",
    install_requires=["pydantic", "python_dateutil", "typing_extensions", "eval_type_backport"],
)
