# REST-API

The backend offers a REST-API with the following endpoints:
...


# Backlog
The following endpoints may be implemented in the future.

## Get user profile
- HTTP-Method: GET
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}`
- Header:
  - Authorization: `Bearer {jwt}`

## Update user profile
- HTTP-Method: PUT
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}`
- Header:
  - Authorization: `Bearer {jwt}`
- Body:
    ```
    {
        nickname: <new nickname>,
        email: <new email>,
        password: <new password>
    }
    ```

## Sign up
- HTTP-Method: POST
- URL: `http://{IP-Host}:{port}/rest/sign-up`
- Body:
  ```
    {
      nickname: <nickname>,
      email: <email>,
      password: <password>
    }
  ```
- Response:
  ```
    {
      userId: <userId>,
      expires_in: <expiration-time in seconds>,
      token: <jwt>,
      refresh_token: <refresh jwt>
    }
  ```

## Sign in
- HTTP-Method: POST
- URL: `http://{IP-Host}:{port}/rest/sign-in`
- Body:
  ```
  {
    email: <email>,
    password: <password>
  }
  ```
- Response:
    ```
    {
      userId: <userId>,
      expires_in: <expiration-time in seconds>,
      token: <jwt>,
      refresh_token: <refresh jwt>
    }
    ```
---

## Get all inventories of an user
- HTTP-Method: GET
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/`
- Header:
  - Authorization: `Bearer {jwt}`

## Get specific inventory of an user
- HTTP-Method: GET
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/{inventoryID}`
- Header:
  - Authorization: `Bearer {jwt}`
- Response:
  ```
  {
    name: <name>,
    items: [items]
  }
  ```

## Add inventory for an user
- HTTP-Method: POST
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/`
- Header:
  - Authorization: `Bearer {jwt}`
- Body:
    ```
    {
      name: <new name>  
    }
    ```

## Update specific inventory of an user
- HTTP-Method: PUT
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/{inventoryID}`
- Header:
  - Authorization: `Bearer {jwt}`
- Body:
    ```
    {
      name: <new name>
    }
    ```
    
## Delete specific inventory of an user
- HTTP-Method: DELETE
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/{inventoryID}`
- Header:
  - Authorization: `Bearer {jwt}`

---

## Add item for an inventory
- HTTP-Method: POST
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/{inventoryID}/items`
- Header:
  - Authorization: `Bearer {jwt}`
- Body:
    ```
    {
      name: <new name>,
      count: <new count>,
      unit: <new unit>
    }
    ```

## Update specific item of an inventory
- HTTP-Method: PUT
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/{inventoryID}/items/{itemID}`
- Header:
  - Authorization: `Bearer {jwt}`
- Body:
    ```
    {
      name: <new name>,
      count: <new count>,
      unit: <new unit>
    }
    ```

## Delete specific item of an inventory
- HTTP-Method: DELETE
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}/inventories/{inventoryID}/items/{itemID}`
- Header:
  - Authorization: `Bearer {jwt}`

---

# Template for new endpoints
## Foo
- HTTP-Method: foo
- URL: `http://{IP-Host}:{port}/rest/foo`
- Request parameters:
- Body:
- Reponse:

