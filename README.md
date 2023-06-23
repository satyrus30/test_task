# test_task

Venv:
---
* ### create:
      python -m venv venv
* ### activate:
      venv\Scripts\activate   

Install Python packages:
---
* ### update pip:
      python.exe -m pip install --upgrade pip
* ### install requirements:
      pip install -r requirements.txt

Allure:
---
Инструкция по установке - https://docs.qameta.io/allure/

Скачать zip архив - https://github.com/allure-framework/allure2/releases

- разархивировать для удобства в проект 

- файлы для запуска 
- - path\to\file\allure (для Linux) 
- - path\to\file\allure.bat (для win) 

## Сформировать отчет
    pytest .\tests

## Генерация результата
    path\to\file generate .\allure-results\

- раскрыть dropdown директория allure-report
- dbl click index.html
- выбрать браузер (chrome)
