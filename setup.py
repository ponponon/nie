import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pynie",
    version="0.0.2",
    author="ponponon",
    author_email="1729303158@qq.com",
    maintainer='ponponon',
    maintainer_email='1729303158@qq.com',
    license='MIT License',
    platforms=["all"],
    description="Generic library for storage level operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ponponon/nie",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ]
)
