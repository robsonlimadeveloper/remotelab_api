
# (Temporary) Basic Documentation RemoteLab API


## Autentication

This enpoint return a Authorization Bearer Token to Access

```sh
POST: 'http://45.233.12.76:4010/api/auth/'
JSON:
{
	"username": "admin",
    "password": "1234"
}
```

## Create a new User

This endpoint create a new User and return User created.

```sh
POST: 'http://45.233.12.76:4010/api/users/'
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
GET: 'http://45.233.12.76:4010/api/users/'

```