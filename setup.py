from setuptools import setup

setup(
    name="gf-utils",
    version="1.0",
    description="A module includes various tools relates to the game girls frontline",
    author="ZeroRin",
    author_email="pptxp@qq.com",
    packages=["gf_utils"],
    install_requires=[
        "tqdm",
        "pycryptodome",
        "logger_tt",
    ],
)
