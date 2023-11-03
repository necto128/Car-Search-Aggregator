from drf_yasg import openapi

get_date_cars_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "title": openapi.Schema(
            type=openapi.TYPE_STRING, default="Skoda Octavia (III) 1,8TSI"
        ),
        "update_record": openapi.Schema(
            type=openapi.TYPE_STRING, default="3 часа назад"
        ),
        "body_type": openapi.Schema(type=openapi.TYPE_STRING, default="Лифтбэк"),
        "transmission": openapi.Schema(
            type=openapi.TYPE_STRING, default="Автоматическая"
        ),
        "engine_capacity": openapi.Schema(type=openapi.TYPE_STRING, default="1.8"),
        "mileage": openapi.Schema(type=openapi.TYPE_STRING, default="200000"),
        "year_manufacture": openapi.Schema(type=openapi.TYPE_STRING, default="2015"),
        "engine_drive": openapi.Schema(type=openapi.TYPE_STRING, default="Передний"),
        "type_price": openapi.Schema(type=openapi.TYPE_STRING, default="BYN"),
        "price": openapi.Schema(type=openapi.TYPE_STRING, default="41610"),
        "city": openapi.Schema(type=openapi.TYPE_STRING, default="Minsk"),
        "about": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.TYPE_STRING,
            default="""Автомобиль покупался новым у официального дилера в 2017 году. 
                    Один хозяин. Максимальная комплектация Style. Из дополнительных опций покупалась 
                    автоматическая диагональная парковка и парковка "гараж", заводской автономный отопитель с функцией дистанционного запуска,
                    комфортный бесключевой доступ, беспроводная зарядка для телефона. Автомобиль в идеальном состоянии.
                    На каско. 2 комплекта резины. Экономичный двигатель.""",
        ),
        "link_car": openapi.Schema(
            type=openapi.FORMAT_URI,
            default="https://ab.onliner.by/skoda/octavia/4923562",
        ),
    },
)
