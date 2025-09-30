# Book store
## Description 
  The website will have a page with a list of books, including a search field by title and author, as well as filters by publisher and genre. It will also be possible to sort the results by lowest price, highest price, popularity, or genre. There will be a separate book page with more detailed information.
  There will be a page with authors whose books are available. When navigating to an author’s page, all available books by this author will be displayed.
  There will be a page with publishers. When navigating to a publisher’s page, all their available books will be displayed.
  It will also be possible to add data (books, authors, publishers), edit, and delete them.
  Users will be able to register and log in.
  For authorized users, there will be a profile page. In the profile, users can view their order history with books and edit their personal information.
  An authorized user can add items to the shopping cart and then click “Buy” to create an order.
  There will also be an “About Us” page with contact details, delivery information, and return policy.

| Endpoint        | Method | Usage                                           | Request body | Response status | Response body |
|-----------------|--------|------------------------------------------------|--------------|-----------------|---------------|
| `/books`        | GET    | Get list of books with search, filters, sort   | – | 200 OK | ```json\n[\n  {\n    "id": 1,\n    "name": "From blood and ash",\n    "author": "Jennifer L. Armentrout",\n    "publisher": "BookChef",\n    "genre": "fantasy",\n    "price": 450,\n    "popularity": 34\n  }\n]\n``` |
| `/books/id`     | GET    | Get detailed information about a book          | – | 200 OK | ```json\n{\n  "id": 1,\n  "name": "From blood and ash",\n  "author": "Jennifer L. Armentrout",\n  "publisher": "BookChef",\n  "genre": "fantasy",\n  "description": "...",\n  "price": 450,\n  "popularity": 34\n}\n``` |
| `/books`        | POST   | Add a book                                     | ```json\n{\n  "name": "Kingdom of flesh and fire",\n  "author": "Jennifer L. Armentrout",\n  "publisher": "BookChef",\n  "genre": "fantasy",\n  "description": "...",\n  "price": 500,\n  "popularity": 29\n}\n``` | 201 Created | ```json\n{\n  "id": 2,\n  "name": "Kingdom of flesh and fire",\n  "author": "Jennifer L. Armentrout",\n  "publisher": "BookChef",\n  "genre": "fantasy",\n  "description": "...",\n  "price": 500,\n  "popularity": 29\n}\n``` |
| `/books/id`     | PUT    | Edit a book                                    | ```json\n{\n  "name": "Kingdom of flesh and fire",\n  "author": "Jennifer L. Armentrout",\n  "publisher": "BookChef",\n  "genre": "fantasy",\n  "description": "...",\n  "price": 550,\n  "popularity": 29\n}\n``` | 200 OK | ```json\n{\n  "id": 2,\n  "name": "Kingdom of flesh and fire",\n  "author": "Jennifer L. Armentrout",\n  "publisher": "BookChef",\n  "genre": "fantasy",\n  "description": "...",\n  "price": 550,\n  "popularity": 29\n}\n``` |
| `/books/id`     | DELETE | Delete a book                                  | – | 200 OK | ```json\n{\n  "id": 1,\n  "name": "From blood and ash",\n  "author": "Jennifer L. Armentrout",\n  "publisher": "BookChef",\n  "genre": "fantasy",\n  "description": "...",\n  "price": 450,\n  "popularity": 34\n}\n``` |
| `/authors`      | GET    | Get list of authors                            | – | 200 OK | ```json\n[\n  { "id": 1, "name": "Jennifer L. Armentrout" }\n]\n``` |
| `/authors/id`   | GET    | Get detailed information about author & books  | – | 200 OK | ```json\n{\n  "id": 1,\n  "name": "Jennifer L. Armentrout",\n  "books": [ { "id": 1, "name": "From blood and ash" } ]\n}\n``` |
| `/authors`      | POST   | Add author                                     | ```json\n{\n  "name": "George Orwel"\n}\n``` | 201 Created | ```json\n{\n  "id": 2,\n  "name": "George Orwel"\n}\n``` |
| `/authors/id`   | PUT    | Edit author                                    | ```json\n{\n  "id": 2,\n  "name": "George Orwell"\n}\n``` | 200 OK | ```json\n{\n  "id": 2,\n  "name": "George Orwell"\n}\n``` |
| `/authors/id`   | DELETE | Delete author                                  | – | 200 OK | ```json\n{\n  "id": 2,\n  "name": "George Orwell"\n}\n``` |
| `/publishers`   | GET    | Get list of publishers                         | – | 200 OK | ```json\n[\n  { "id": 1, "name": "KSD" }\n]\n``` |
| `/publishers/id`| GET    | Get all publisher’s books                      | – | 200 OK | ```json\n{\n  "id": 1,\n  "name": "KSD",\n  "books": [ { "id": 1, "name": "Red queen" } ]\n}\n``` |
| `/publishers`   | POST   | Add publisher                                  | ```json\n{\n  "name": "Vivat"\n}\n``` | 201 Created | ```json\n{\n  "id": 2,\n  "name": "Vivat"\n}\n``` |
| `/publishers/id`| PUT    | Edit publisher                                 | ```json\n{\n  "id": 2,\n  "name": "Vivat/"\n}\n``` | 200 OK | ```json\n{\n  "id": 2,\n  "name": "Vivat/"\n}\n``` |
| `/publishers/id`| DELETE | Delete publisher                               | – | 200 OK | ```json\n{\n  "id": 2,\n  "name": "Vivat/"\n}\n``` |
| `/register`     | POST   | New user registration                          | ```json\n{\n  "username": "olya",\n  "email": "olya@gmail.com",\n  "password": "12345"\n}\n``` | 201 Created | ```json\n{\n  "id": 1,\n  "username": "olya"\n}\n``` |
| `/login`        | POST   | User login (get token)                         | ```json\n{\n  "email": "olya@gmail.com",\n  "password": "12345"\n}\n``` | 200 OK | ```json\n{\n  "token": "token"\n}\n``` |
| `/profile/id`   | GET    | Look over user’s profile & orders              | – | 200 OK | ```json\n{\n  "id": 1,\n  "username": "olya",\n  "email": "olya@gmail.com",\n  "orders": [ { "id": 1, "books": [ { "id": 1, "name": "From blood and ash" } ], "status": "completed" } ]\n}\n``` |
| `/profile/id`   | PUT    | Edit profile                                   | ```json\n{\n  "id": 1,\n  "username": "plusik",\n  "email": "olya@gmail.com"\n}\n``` | 200 OK | ```json\n{\n  "id": 1,\n  "username": "plusik",\n  "email": "olya@gmail.com"\n}\n``` |
| `/cart`         | POST   | Add book to cart                               | ```json\n{ "bookId": 1, "quantity": 1 }\n``` | 200 OK | ```json\n{ "bookId": 1, "quantity": 1 }\n``` |
| `/cart`         | GET    | Look over the cart                             | – | 200 OK | ```json\n[\n  { "bookId": 1, "quantity": 1, "name": "From blood and ash", "price": 450 }\n]\n``` |
| `/orders`       | POST   | Make an order                                  | ```json\n{\n  "cart": [ { "bookId": 1, "quantity": 1 } ]\n}\n``` | 201 Created | ```json\n{\n  "id": 10,\n  "cart": [ { "bookId": 1, "quantity": 1 } ]\n}\n``` |
| `/about`        | GET    | Get information about shop                     | – | 200 OK | ```json\n{\n  "contacts": "bookstore@gmail.com",\n  "delivery": "...",\n  "returns": "..."\n}\n``` |

<img width="1310" height="732" alt="image" src="https://github.com/user-attachments/assets/12a731fa-220a-4209-af2c-5d941a8fae84" />
