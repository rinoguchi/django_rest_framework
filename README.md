# Django Rest Framework Sample

## ライブラリインストール

```sh
poetry install
```

## DB 起動

```sh
docker-compose up -d
```

## マイグレーション実行

```sh
cd apps/
poetry run python manage.py migrate
```

## アプリ起動

```sh
poetry run python manage.py runserver
```

## URL

- 管理画面
  - http://127.0.0.1:8000/admin/
- 素の Django で作った API
  - 質問一覧 API
    - GET http://127.0.0.1:8000/polls/questions/
  - 質問 API
    - GET http://127.0.0.1:8000/polls/questions/1/
  - 投票 API
    - POST http://127.0.0.1:8000/polls/questions/1/vote/
- DRF で作った API
  - 質問一覧 API
    - GET http://127.0.0.1:8000/drfpolls/questions/
  - 質問 API
    - GET http://127.0.0.1:8000/drfpolls/questions/1/
  - 投票 API
    - POST http://127.0.0.1:8000/drfpolls/questions/1/vote/
