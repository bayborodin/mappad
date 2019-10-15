# mappad.ru
Сервис хранения GPS треков
Позволяет зарегистрированным пользователям загружать GPS треки в различных форматах, сохранять их в личном кабинете, просматривать на карте, а также - видеть основные характеристики трека.
Сервис имеет социальную составляющую:
* Делиться GPS треками с другими пользователями (приватные и публичные GPS треки)
* Подписываться на треки других пользователей
* Оставлять коментарии к GPS треками других пользователей

В проекте используется интеграция со следующими внешними сервисами:
* OpenStreetMap
* Mapbox

## Запуск в Development режиме
```bash
export DATABASE_URI="postgresql://mappad:mappad@localhost/mappad" && export FLASK_ENV=development && export FLASK_DEBUG=1 && export export FLASK_APP=app && flask run
```

## Запуск Docker контейнера
```bash
docker build -t mappad:latest .
docker run --name mappad  -d -p 8000:5000 --rm -e DATABASE_URI=postgresql://mappad:q123Q123@mappad.ctixcsaspk7s.us-west-2.rds.amazonaws.com -e FLASK_DEBUG=1 -e SECRET_KEY=SXRnASFEbGkwdpFokZlDkgjeIuRqbPoZ  mappad:latest
```

## Интерфейс приложения
<div align="center">
<img src="documentation/layout_2.png" width=50%>
<img src="documentation/layout_1.png" width=50%>
</div>
