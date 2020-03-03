## Anastasiya Brytsikava

### Home task: 03 Classes and Packaging 

## Description of the package
This package displays the following host information:

>- Overall CPU load
>- Overall memory usage
>- Overall virtual memory usage
>- IO information
>- Network information 

## How to install package:

1) pip install wheel
2) cd *repository*
3) git clone *repository*
4) python3 setup.py bdist_wheel --universal
5) pip install dist/snapshot*.whl
6) Enter "snapshot"(or other version, you can find it below)
7) In your current directory will appear json/txt with info about host.

## How to uninstall package
1) Enter pip uninstall snapshot*.whl

## Examples of use:
+ snapshot txt 5
>
Every 5 second all information will be added in txt-file
+ snapshot json 100
>
Every 100 second all information will be added in json-file
