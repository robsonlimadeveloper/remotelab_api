
# (Temporary) Basic Documentation RemoteLab API


## Autentication

This enpoint return a Authorization Bearer Token to Access

```sh
POST: 'http://localhost:4010/api/auth/'
JSON:
{
	"username": "admin",
    "password": "1234"
}
```

## Create a new User

```sh
POST: 'http://localhost:4010/api/users/'
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

```sh
GET: 'http://localhost:4010/api/users/'

```