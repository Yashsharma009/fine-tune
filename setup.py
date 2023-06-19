from setuptools import setup, find_packages

setup(
    name="streamlit-app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "torch",
        "transformers",
    ],
    entry_points={
        "console_scripts": [
            "streamlit-app = app:main",
        ]
    },
)
