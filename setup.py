from setuptools import setup, find_packages

setup(
    name="itchat_desktop",
    version="1.2",
    description="wechat sdk",
    long_description="desktop mod for itchat",
    license="MIT Licence",
    url="https://github.com/eatmoreapple/itchat_desktop",

    author="eatmoreapple",
    author_email="eatmoreorange@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "itchat",
    ],

    scripts=[],
)
