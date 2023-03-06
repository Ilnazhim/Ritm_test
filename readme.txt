Клонируем репозиторий

git clone https://github.com/Ilnazhim/Ritm_test.git

Переходим в рабочий каталог

cd \Ritm_test

Устанавливаем виртуальное окружение

py -m venv venv

Активируем его

venv\Scripts\activate.bat

Устанавливаем зависимости

pip install -r requirements.txt

Запуск тестов с отчетом Allure

py -m pytest --alluredir=test_results

Вывод отчета
allure serve test_results

