# 28.1 Итоговый проект по автоматизации тестирования:

## Объект тестирования: https://b2c.passport.rt.ru

## Ссылка на тест-кейсы и баг-репорт: https://docs.google.com/spreadsheets/d/15qnO8_zDAruvlLGXp2PpH__IdV0rq8BU0pQ1mojQbcA/edit?usp=sharing

Техническое задание:
1. Протестировать требования.
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)

## Методы:

Для разработки автотестов применялись библиотеки pytest и selenium, описанные в файле requirements.txt

Для составления и написания тест-кейсов применены техники тест-дизайна: классы эквивалентности, анализ граничных значений, предугадывание ошибок, тестирование состояний и переходов


## Структура:

auth_page содержит код авторизации

base_page содержит реализацию шаблона PageObject для Python

test_rt содержит автоматизированные тесты для объекта тестирования

и др.

## Запуск автотестов:

python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_rt.py

## Окружение: Windows 10, Chrome ver 115.0.5790.173 (Официальная сборка), (64 бит)
