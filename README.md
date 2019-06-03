# PyChalk
This is a simple python package, which makes it very easy to colour up your terminal output via simple functions.

## Documentation
### Getting started:

Terminal:
```
    pip3 install git+https://github.com/Throvn/pychalk
```

Your python file:
```python
    import pychalk as chalk

    print("The instalation was a " + chalk.green("success!"))
```

### Colors & Background Colors

All right, now that you're all set up it is time to see what you can do.

> To use background colors just write:
```python
    print(chalk.bg.blue("I have a background color"))
    # or something like
    print(chalk.bg.bright.red("I have a background color"))
```

* Black
* Red
* Green
* Yellow
* Blue
* Magenta
* Cyan
* White

### Text Decoration

And for special purposes...

* Bold
* Underline
* Reversed

### Todos:
* Add more underline possibillities (e.g. ``chalk.bg.bright.red.underline("Test")``)