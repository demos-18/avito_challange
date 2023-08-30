# avito_challange
Для запуска теста из интерпретатора можно использовать следующие команды:
pytest tests\tests.py - запускает все тесты из файла tests.py
pytest tests\tests.py::add_to_favorite - запускает выбранный тест add_to_favorite из файла tests.py
pytest tests\tests.py -m ui - запускает все тесты из с маркировкой @pytest.mark.ui из файла tests.py
Для запуска тестов из командной строки можно использовать следующие команды:
python -m pytest tests\tests.py - запускает все тесты из файла tests.py
python -m pytest tests\tests.py::add_to_favorite - запускает выбранный тест add_to_favorite из файла tests.py
python -m pytest tests\tests.py -m ui - запускает все тесты из с маркировкой @pytest.mark.ui из файла tests.py

