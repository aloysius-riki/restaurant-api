# restaurant-api
This restaurant API allows you to access and integrate with a restaurant-related database.

You can add, remove, update and search for restaurants and display information users want to know, such as:  cuisine type, location, ratings etc




A **Restaurant** has a:
- name;
- location;
- phone number;
- email;
- website;
- cuisine.


## Test

1. Get all restaurants details by ID (GET): https://riki-restaurant-api.herokuapp.com/restaurants/

2. Get all restaurants details by ID (GET): https://riki-restaurant-api.herokuapp.com/restaurants/{id} 

3. Create a restarant (POST): http://localhost:8080/api/v1/drone/register

Request body is given below:

  
Content-type: JSON.
```
{
   "name":"Marios spot",
   "location":"Sarit",
   "phone":"0722000002",
   "email":"info@mario.co.ke",
   "website":"http://mario.co.ke",
   "cuisine":"Italian"
}
```
4. Update a restaurant (PUT): https://riki-restaurant-api.herokuapp.com/restaurants/{id}

Request body is given below:


Content-type: JSON.
```
{
   "name":"Marios spot",
   "location":"Sarit Center",
   "phone":"0722123456",
   "email":"info@marios-spot.co.ke",
   "website":"http://marios-spot.co.ke",
   "cuisine":"Italian"
}
```

5. Remove Restaurant (DELETE): https://riki-restaurant-api.herokuapp.com/restaurants/{id}

