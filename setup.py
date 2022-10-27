import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="nie",
    version="0.0.1",
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
    entry_points={
        'console_scripts': [
            'douyin_image=douyin_image:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ]
)
