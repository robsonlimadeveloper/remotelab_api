
# Basic Documentation RemoteLab API


## create a new User

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

## list all Users

```sh
GET: 'http://localhost:4010/api/users/'

```