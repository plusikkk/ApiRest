<h1>Project documentation</h1>

| Endpoint | Method | Authorization | Request body | Response body |
|-----------|--------|--------------|--------------------------|--------------------------|
| `/books` | `GET` | AllowAny | – | ``` [{"id": 1, "name":"From blood and ash", "author":"Jennifer L. Armentrout", "publisher":"BookChef", "genre": "fantasy", "price": 450, "popularity": 34}, ...] ``` |
| `/books` | `POST` | IsAdminUser | ``` {"name": "Kingdom of flesh and fire", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 500, "popularity": 29} ``` | ```{"id": 2, "name": "Kingdom of flesh and fire", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 500, "popularity": 29} ``` |
| `/books/<id>` | `GET` | IsAuthenticated | – | ```{"id": 1, "name":"From blood and ash", "author":"Jennifer L. Armentrout", "publisher":"BookChef", "genre": "fantasy", "price": 450, "popularity": 34} ``` |
| `/books/<id>` | `PUT` | IsAdminUser | ```{"id": 1, "name":"From blood and ash", "author":"Jennifer L. Armentrout", "publisher":"BookChef", "genre": "fantasy", "price": 350, "popularity": 34} ``` | ```{"id": 1, "name":"From blood and ash", "author":"Jennifer L. Armentrout", "publisher":"BookChef", "genre": "fantasy", "price": 350, "popularity": 34} ``` |
| `/books/<id>` | `DELETE` | IsAdminUser | ```{"id": 1, "name":"From blood and ash", "author":"Jennifer L. Armentrout", "publisher":"BookChef", "genre": "fantasy", "price": 450, "popularity": 34}``` | `204 No Content` |
| `/authors` | `GET` | AllowAny | – | ```[{"id": 1, "name": "Jennifer L. Armentrout"}, ...] ``` |
| `/authors` | `POST` | IsAdminUser | ```{"name": "George Orwel", "description": "..."} ``` | ```{"id": 2, "name": "George Orwel", "description": "..."} ``` |
| `/authors/<id>` | `GET` | IsAuthenticated | – | ```{"id": 2, "name": "George Orwel", "description": "..."} ``` |
| `/authors/<id>` | `PUT` | IsAdminUser | ```{"id": 2, "name": "George Orwell", "description": "..."}``` | ```{"id": 2, "name": "George Orwell", "description": "..."} ``` |
| `/authors/<id>` | `DELETE` | IsAdminUser | ```{"id": 2, "name": "George Orwell", "description": "..."}``` | `204 No Content` or ```json { "error": "Неможливо видалити автора, бо на сайті є його книги." } ``` |
| `/publishers` | `GET` | AllowAny | – | ``` [ { "id": 3, "name": "А-БА-БА-ГА-ЛА-МА-ГА" } ] ``` |
| `/publishers` | `POST` | IsAdminUser | ``` { "name": "Ранок", "description": "..." } ``` | ```json { "id": 3, "name": "Ранок", "description": "..." } ``` |
| `/publishers/<id>` | `GET` | IsAuthenticated | – | ```{ "id": 3, "name": "Ранок", "description": "..." } ``` |
| `/publishers/<id>` | `PUT` | IsAdminUser | ```{ "id": 3, "name": "Ранок", "description": "ooooooooooo" } ``` | ```{ "id": 3, "name": "Ранок", "description": "ooooooooooo" } ``` |
| `/publishers/<id>` | `DELETE` | IsAdminUser | ```{ "id": 3, "name": "Ранок", "description": "ooooooooooo" }``` | `204 No Content` or ```json { "error": "Неможливо видалити видавництво, бо на сайті є його книги." } ``` |
| `/user/register` | `POST` | AllowAny | ```{ "username": "test", "email": "test@gmail.com", "password": "Complexpass1", "passwordcheck": "Complexpass1", "first_name": "olya", "last_name": "neolya" } ``` | ```{"id": 1, "username": "test", "email": "test@gmail.com", "password": "Complexpass1", "passwordcheck": "Complexpass1", "first_name": "olya", "last_name": "neolya" } ``` |
| `/api/token/` | `POST` | AllowAny | ```{ "username": "test", "password": "Complexpass1" } ``` | ```json { "refresh": "<refresh_token>", "access": "<access_token>" } ``` |
| `/api/token/refresh/` | `POST` | IsAuthenticated | ```{ "refresh": "<refresh_token>" } ``` | ```json { "access": "<new_access_token>" } ``` |

