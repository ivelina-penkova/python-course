#Черно и бяло


За целта на това предизвикателство ще трябва да се поразровите малко и да откриете начин да обърнем нормална картинка до черно-бяла такава (grayscale). Ще очакваме да напишете декоратор grayscale, за функциите rotate_left, rotate_right, invert, darken и lighten от първа задача.
##Пример:

Написали сме си rotate_left от първа задача (ако не сте, можете да използвате някое решение на ваш колега, тъй като са вече публични) и изглежда така:

```python
def rotate_left(image):
    return list(zip(*image))[::-1]
```

Ще използваме отново снимка на една малка панда:

![alt text](https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda.jpg)

И ако я подадем на rotate_left използвайки render.py:

```python
python render.py panda.jpg rotate_left
```

получаваме:

![alt text](https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda_rotate_left.jpg)

Ако обаче декорираме rotate_left с @grayscale:

```python
@grayscale
def rotate_left(image):
    return list(zip(*image))[::-1]
```

резултатът ще бъде:

![alt text](https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda_rotate_left_grayscale.jpg)
