
# (Temporary) Basic Documentation RemoteLab API


## Autentication

This enpoint return a Authorization Bearer Token to Access

```sh
POST: '/api/auth/'
JSON:
{
	"username": "admin",
    "password": "1234"
}
```

## Create a new User

This endpoint create a new User and return User created.

```sh
POST: '/api/users/'
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

## Get User by Id

This endpoint return user by id.

```sh
GET: '/api/users/<user_id: int>'

```

## Update a User by Id

This endpoint update a User and return User updated.

```sh
PUT: '/api/users/<user_id: int>'
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
GET: '/api/users/'

```

## List all User Types

This endpoint return All Users Types Array

```sh
GET: '/api/user-types/'

```

## Get User Type by Id

This endpoint return User Type by id.

```sh
GET: '/api/user-types/<user_type_id: int>'

```

## List all Institutes

This endpoint return All Institutes Array

```sh
GET: '/api/institutes/'

```

## Get Institute by Id

This endpoint return Institute by id.

```sh
GET: '/api/institutes/<institute_id: int>'

```

## List all Experiments

This endpoint return All Experiments Array

```sh
GET: '/api/experiments/'

```

## Get Experiment by Id

This endpoint return Experiment by id.

```sh
GET: '/api/experiments/<experiment_id: int>'

```