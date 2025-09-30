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

| Endpoint        | Method | Usage                                           | Request body | Response status | Response body | Params
|-----------------|--------|------------------------------------------------|--------------|-----------------|---------------|-------|
| `/books`        | GET    | Get list of books with search, filters, sort   | – | 200 OK | ```[{"id": 1, "name":"From blood and ash", "author":"Jennifer L. Armentrout", "publisher":"BookChef", "genre": "fantasy", "price": 450, "popularity": 34}]``` | search(name, author), filter(genre, publisher), sort(price_inc, price_dec, popularity, genre)
| `/books/id`     | GET    | Get detailed information about a book          | – | 200 OK | ```{"id": 1, "name": "From blood and ash", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 450, "popularity": 34}``` |
| `/books`        | POST   | Add a book                                     | ```{"name": "Kingdom of flesh and fire", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 500, "popularity": 29}``` | 201 Created | ```{"id": 2, "name": "Kingdom of flesh and fire", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 500, "popularity": 29}``` |
| `/books/id`     | PUT    | Edit a book                                    | ```{"name": "Kingdom of flesh and fire", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 550, "popularity": 29}``` | 200 OK | ```{"id": 2, "name": "Kingdom of flesh and fire", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 550, "popularity": 29}``` |
| `/books/id`     | DELETE | Delete a book                                  | – | 200 OK | ```{"id": 1, "name": "From blood and ash", "author": "Jennifer L. Armentrout", "publisher": "BookChef", "genre": "fantasy", "description": "...", "price": 450, "popularity": 34}``` |
| `/authors`      | GET    | Get list of authors                            | – | 200 OK | ```[{"id": 1, "name": "Jennifer L. Armentrout"}]``` |
| `/authors/id`   | GET    | Get detailed information about author & books  | – | 200 OK | ```{"id": 1, "name": "Jennifer L. Armentrout", "books": [{"id": 1, "name": "From blood and ash"}]}``` |
| `/authors`      | POST   | Add author                                     | ```{"name": "George Orwel"}``` | 201 Created | ```{"id": 2, "name": "George Orwel"}``` |
| `/authors/id`   | PUT    | Edit author                                    | ```{"id": 2, "name": "George Orwell"}``` | 200 OK | ```{"id": 2, "name": "George Orwell"}``` |
| `/authors/id`   | DELETE | Delete author                                  | – | 200 OK | ```{"id": 2, "name": "George Orwell"}``` |
| `/publishers`   | GET    | Get list of publishers                         | – | 200 OK | ```[{"id": 1, "name": "KSD"}]``` |
| `/publishers/id`| GET    | Get all publisher’s books                      | – | 200 OK | ```{"id": 1, "name": "KSD", "books": [{"id": 1, "name": "Red queen"}]}``` |
| `/publishers`   | POST   | Add publisher                                  | ```{"name": "Vivat"}``` | 201 Created | ```{"id": 2, "name": "Vivat"}``` |
| `/publishers/id`| PUT    | Edit publisher                                 | ```{"id": 2, "name": "Vivat/"}``` | 200 OK | ```{"id": 2, "name": "Vivat/"}``` |
| `/publishers/id`| DELETE | Delete publisher                               | – | 200 OK | ```{"id": 2, "name": "Vivat/"}``` |
| `/register`     | POST   | New user registration                          | ```{"username": "olya", "email": "olya@gmail.com", "password": "12345"}``` | 201 Created | ```{"id": 1, "username": "olya"}``` |
| `/login`        | POST   | User login (get token)                         | ```{"email": "olya@gmail.com", "password": "12345"}``` | 200 OK | ```{"token": "token"}``` |
| `/profile/id`   | GET    | Look over user’s profile & orders              | – | 200 OK | ```{"id": 1, "username": "olya", "email": "olya@gmail.com", "orders": [{"id": 1, "books": [{"id": 1, "name": "From blood and ash"}], "status": "completed"}]}``` |
| `/profile/id`   | PUT    | Edit profile                                   | ```{"id": 1, "username": "plusik", "email": "olya@gmail.com"}``` | 200 OK | ```{"id": 1, "username": "plusik", "email": "olya@gmail.com"}``` |
| `/cart`         | POST   | Add book to cart                               | ```{"bookId": 1, "quantity": 1}``` | 200 OK | ```{"bookId": 1, "quantity": 1}``` |
| `/cart`         | GET    | Look over the cart                             | – | 200 OK | ```[{"bookId": 1, "quantity": 1, "name": "From blood and ash", "price": 450}]``` |
| `/orders`       | POST   | Make an order                                  | ```{"cart": [{"bookId": 1, "quantity": 1}]}``` | 201 Created | ```{"id": 10, "cart": [{"bookId": 1, "quantity": 1}]}``` |
| `/about`        | GET    | Get information about shop                     | – | 200 OK | ```{"contacts": "bookstore@gmail.com", "delivery": "...", "returns": "..."}``` |

<img width="1310" height="732" alt="image" src="https://github.com/user-attachments/assets/12a731fa-220a-4209-af2c-5d941a8fae84" />
