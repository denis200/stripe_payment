# Stripe Payment
## Стек проекта
Проект написан на Django + Django Rest Framework + PostgreSQL + Docker

## Описание проекта
Использование платежной системы stripe для оплаты списка товаров.Подробнее в [файле](https://github.com/denis200/stripe_payment/blob/main/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%BB%D1%8F%20Python%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0.pdf)

## Installation

Для начала переименуйте  ".env.example"  - > ".env" 

После создайте базу данных postgres и в данный файл введите соответствующие поля.
```
POSTGRES_DB=#db credentials
POSTGRES_PASSWORD=#db credentials
```
Также в .env файл нужно добавить stripe secret key

```
SKSTRIPE= #secret_key
```

Также в переменной stripe в файле templates/items нужно вставить свой public key

```
var stripe = Stripe('pk_test_...');
```

Чтобы поднять контейнер, выполните команду:
```
docker-compose up --build
```

Для того чтобы выполнить заполнение базы тестовыми данными: 

```
docker exec web_django python manage.py setup_test_data
```

Создать суперпользователя: 

```
docker exec -it web_django python manage.py setup_test_data
```

Открыть 127.0.0.1:8000/ чтобы увидеть список товаров
### P.S. Из-за выполнения дополнительных задач,произошло отклонение от изначального тз.


