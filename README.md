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

###Books list
GET /books
Usage: getting list of books with opportunity of sorting and searching by params.
Params: search(name, author), filter(genre, publisher), sort(price_inc, price_dec, popularity, genre)
  Response body: 
```json
[
{
“id”: 1,
“name”: “From blood and ash”,
“author”: “Jennifer L. Armentrout”,
“publisher”: “BookChef”,
“genre”: “fantasy”, 
“price”: 450,
“popularity”: 34
},
…
]
```
###Book details
GET /books/id
Usage: getting detailed information about book
Response body: 
```json
{
“id”: 1,
“name”: “From blood and ash”,
“author”: “Jennifer L. Armentrout”,
“publisher”: “BookChef”,
“genre”: “fantasy”, 
“description”: “…”,
“price”: 450,
“popularity”: 34
}
```
###Add book
POST /books
Usage: adding a book
Request body:
```json
{
“name”: “Kingdom of flesh and fire”,
“author”: “Jennifer L. Armentrout”,
“publisher”: “BookChef”,
“genre”: “fantasy”, 
“description”: “…”,
“price”: 500,
“popularity”: 29
}
```
Response body: 
```json
{
“id”: 2,
“name”: “Kingdom of flesh and fire”,
“author”: “Jennifer L. Armentrout”,
“publisher”: “BookChef”,
“genre”: “fantasy”, 
“description”: “…”,
“price”: 500,
“popularity”: 29
}
```
###Edit book
PUT /books/id
Usage: editing a book 
Request body: 
```json
{
“name”: “Kingdom of flesh and fire”,
“author”: “Jennifer L. Armentrout”,
“publisher”: “BookChef”,
“genre”: “fantasy”, 
“description”: “…”,
“price”: 550,
“popularity”: 29
}
```
Response body: 
```json
{
“id”: 2,
“name”: “Kingdom of flesh and fire”,
“author”: “Jennifer L. Armentrout”,
“publisher”: “BookChef”,
“genre”: “fantasy”, 
“description”: “…”,
“price”: 550,
“popularity”: 29
}
```
###Delete book
DELETE /books/id
Usage: deleting a book
Response body: 
```json
{
“id”: 1,
“name”: “From blood and ash”,
“author”: “Jennifer L. Armentrout”,
“publisher”: “BookChef”,
“genre”: “fantasy”, 
“description”: “…”,
“price”: 450,
“popularity”: 34
}
```
###Authors list
GET /authors
Usage: getting list of authors
Response body: 
```json
[
{“id”: 1, “name”: “Jennifer L. Armentrout”},
…
]
```
###Author details
GET /authors/id
Usage: getting detailed information about author and his books
Response body: 
```json
{
“id”: 1,
“name”: “Jennifer L. Armentrout”,
“books”: [
	{“id”: 1, “name”: “From blood and ash”},
	…
]
}
```
###Add author
POST /authors
Usage: adding author
Request body: 
```json
{
“name”: “George Orwel”,
}
Response body: {
“id”: 2,
“name”: “George Orwel”,
}
```
###Edit author
PUT /authors/id
Usage: editing author’s information  
Request body: 
```json
{
“id”: 2,
“name”: “George Orwell”,
}
```
Response body: 
```json{
“id”: 2,
“name”: “George Orwell”,
}
```
###Delete author
DELETE /authors/id
Usage: deleting an author
Response body: 
```json{
“id”: 2,
“name”: “George Orwell”,
}
```
###Publishers list
GET /publishers
Usage: getting list of publishers
Response body: 
```json
[
{“id”: 1, “name”: “KSD”},
…
]
```
###Publisher details
GET /publisher/id
Usage: getting all publisher’s books
Response body: 
```json
{
“id”: 1,
“name”: “KSD”,
“books”: [
	{“id”: 1, “name”: “Red queen”},
	…
]
}
```
###Add publisher
POST /publisher
Usage: adding publisher
Request body: 
```json
{
“name”: “Vivat”,
}
```
Response body: 
```json
{
“id”: 2,
“name”: “Vivat”,
}
```
###Edit publisher
PUT /publishers/id
Usage: editing publisher’s information 
Request body: 
```json{
“id”: 2,
“name”: “Vivat/”,
}
```
Response body: 
```json{
“id”: 2,
“name”: “Vivat/”,
}
```
###Delete publisher
DELETE /publishers/id
Usage: deleting publisher
Response body: 
```json
{
“id”: 2,
“name”: “Vivat/”,
}
```
###Registration 
POST /register
Usage: new user registration
Request body: 
```json
{
“username”: “olya”,
“email”: “olya@gmail.com”,
“password”: “12345”
}
```
Response body: 
```json
{
“id”: 1,
“username”: “olya”,
}
```
###Login
POST /login
Usage: getting a token for authorization 
Request body: 
```json
{
“email”: “olya@gmail.com”,
“password”: “12345”
}
```
Response body: 
```json
{
“token”: “token”
}
```
###Profile
GET /profile/id
Usage: look over user’s profile and orders
Response body: 
```json
{
"id": 1,
"username": "olya",
"email": "olya@gmail.com",
"orders": [
{
"id": 1,
     	"books": [ { "id": 1, "name": "From blood and ash" } ],
      	"status": "completed"
}
]
}
```
###Edit profile
PUT /profile/id
Usage: editing user’s profile
Request body: 
```json
{
“id”: 1,
“username”: “plusik”,
“email”: “olya@gmail.com”
}
```
Response body: 
```json
{
“id”: 1,
“username”: “plusik”,
“email”: “olya@gmail.com”
}
```
###Add book to cart
POST /cart
Usage: adding book to cart
Request body: 
```json
{“bookId”: 1, “quantity”: 1}
```
Response body: 
```json
{“bookId”: 1, “quantity”: 1}
```
###Cart
GET /cart
Usage: look over the cart
Response body: 
```json
[
{“bookId”: 1, “quantity”: 1, “name”: “From blood and ash”, “price”: 450}
]
```
###Buy
POST /orders
Usage: make an order 
Request body: 
```json
{
"cart": [
{ "bookId": 1, "quantity": 1 }
]
}
```
Response body: 
```json{
“id”: 10,
"cart": [
{ "bookId": 1, "quantity": 1 }
]
}
```
###Page “about”
GET /about
Usage: getting information about shop
Response body: 
```json
{
"contacts": "bookstore@gmail.com",
"delivery": "…",
"returns": "…",
}
```
