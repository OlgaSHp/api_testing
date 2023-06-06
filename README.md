### Развертывание проекта

1. Клонировать репозиторий:

   ```bash
   git clone git@github.com:OlgaSHp/api_testing.git
   ```

2. Перейти в папку с проектом:

   ```bash
   cd api_testing/
   ```

3. Установить виртуальное окружение для проекта:

   ```bash
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```bash
   # для OS Lunix и MacOS
   source venv/bin/activate

   # для OS Windows
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

### Запуск Docker

1. Откройте терминал или командную строку
2. Перейти в корневую папку проекта
3. Создайте Docker image:

   ```bash
   docker build -t api-testing .
   ```

4. Запустите контейнер

   ```bash
   docker run api-testing
   ```
