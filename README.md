# ShortLinkDjango

## Environment setup

#### First run

To start using this project correctly You need to set up a few things.
First You need to open this directory in CommandLine, then run: 
```python -m venv venv``` or ```python3 -m venv venv```

If You want run Your virtual environment:  
MAC/Linux: run:```source venv/bin/activate```  
Windows: run: ```venv\Scripts\activate```

After activating your (venv) run:
```
pip install -r requirements.txt
```

You should make migrations before You start application:

```
python manage.py migrate
```

To run Django Project run command:

MAC/Linux: run: ```python manage.py runserver```
Windows: run: ```python manage.py runserver```

## Running App

MAC/Linux: run: ```python manage.py runserver```
Windows: run: ```python manage.py runserver```

## Tests
```
pytest -x -vv
```

## Code Audit
```
pylama
```