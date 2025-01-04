from setuptools import setup, find_packages

setup(
    name='social_media_post_generator',  # Replace with your package name
    version='0.1.0',  # Replace with your package version
    packages=find_packages(),
    install_requires=[
        'Flask',
        'meta-ai-api',
    ],  # List your project's dependencies
    entry_points={
        'console_scripts': [
            'generate_post = your_module:generate_post',  # Replace with your script entry point
        ],
    },
)