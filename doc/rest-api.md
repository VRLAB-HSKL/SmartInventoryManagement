# REST-API

The backend offers a REST-API with the following endpoints:
...


# Backlog
The following endpoints may be implemented in the future.

## Get user profile
- HTTP-Method: GET
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}`

## Update user profile
- HTTP-Method: PUT
- URL: `http://{IP-Host}:{port}/rest/profiles/{userID}`
- Request parameters:
- Body:
    ```
    {
        userName: <new user name>
    }
    ```

## Get all inventories of a user
- HTTP-Method: GET
- URL: `http://{IP-Host}:{port}/rest/{userID}/inventories/`

## Get specific inventory of a user
- HTTP-Method: GET
- URL: `http://{IP-Host}:{port}/rest/{userID}/inventories/{inventoryID}`

## Update specific inventory of a user
- HTTP-Method: PUT
- URL: `http://{IP-Host}:{port}/rest/{userID}/inventories/{inventoryID}`
- Request parameters:
- Body:
    ```
    {
      name: <new name>  
    }
    ```

## Add inventory for a user
- HTTP-Method: POST
- URL: `http://{IP-Host}:{port}/rest/{userID}/inventories/{inventoryID}`
- Request parameters:
- Body:
    ```
    {
      name: <new name>  
    }
    ```

## Delete specific inventory of a user
- HTTP-Method: DELETE
- URL: `http://{IP-Host}:{port}/rest/{userID}/inventories/{inventoryID}`
- Request parameters:
- Body:

## Get all items of a inventory
- HTTP-Method: GET
- URL: `http://{IP-Host}:{port}/rest/{userID}/inventories/{inventoryID}/items`

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
      email: <email>,
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
      email: <email>,
      expires_in: <expiration-time in seconds>,
      token: <jwt>,
      refresh_token: <refresh jwt>
    }
    ```



# Template for new endpoints
## Foo
- HTTP-Method: foo
- URL: `http://{IP-Host}:{port}/rest/foo`
- Request parameters:
- Body:

