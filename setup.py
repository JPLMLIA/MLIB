from setuptools import find_packages, setup
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
if __name__ == '__main__':
    setup(
        name='mlib',
        version='1.0.0',
        license='CalTech',
        author='Lukas Mandrake',
        author_email='lukas.mandrake@jpl.caltech.edu',
        url='https://github.com/JPLMLIA/MLIB',
        download_url='THIS IS A STUB',
        packages=find_packages(),
        include_package_data=True,
        package_data={},
        install_requires=requirements,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Indended Audience :: Science/Research',
            'Indended Audience :: Education',
            'License :: CalTech License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.6 :: Only',
            'Topic :: Utilities'
        ])