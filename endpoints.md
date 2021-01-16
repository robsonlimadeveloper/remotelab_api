
# (Temporary) Basic Documentation RemoteLab API


## Autentication

This enpoint return a Authorization Bearer Token to Access

```sh
POST: 'http://189.126.106.53:4010/api/auth/'
JSON:
{
	"username": "admin",
    "password": "1234"
}
```

## Create a new User

This endpoint create a new User and return User created.

```sh
POST: 'http://189.126.106.53:4010/api/users/'
JSON:
{
    "name": "Test",
    "username": "test",
    "email": "test@test.com",
    "phone": "(83) 99999-9999",
    "date_of_birth": "2021-01-12",
    "password": "1234"
}

```

## Update a new User

This endpoint update a User and return User updated.

```sh
PUT: 'http://189.126.106.53:4010/api/users/'
JSON:
{
    "name": "Test",
    "username": "test",
    "email": "test@test.com",
    "phone": "(83) 99999-9999",
    "date_of_birth": "2021-01-12",
    "password": "1234"
}

```

## List all Users

This endpoint return All Users Array

```sh
GET: 'http://189.126.106.53:4010/api/users/'

```