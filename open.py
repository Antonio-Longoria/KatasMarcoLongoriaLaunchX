def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()
#Prueba y Excepto de los bloques
>>> try:
...     open('config.txt')
... except FileNotFoundError:
...     print("Couldn't find the config.txt file!")
...
Couldn't find the config.txt file!
