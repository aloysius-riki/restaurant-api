# restaurant-api
This restaurant API allows you to access and integrate with a restaurant-related database.

You can add, remove, update and search for restaurants and display information users want to know, such as:  cuisine type, location, phone number etc




A **Restaurant** has a:
- name;
- location;
- phone number;
- email;
- website;
- cuisine.


## How To Use The API

The endpoints of the API are listed below. You can use [this Postman Collection](https://www.postman.com/aerospace-administrator-59946073/workspace/restaurant-api/collection/21537138-29b922ed-4471-4657-82ef-6416d55d9613?action=share&creator=21537138) to easily engage with the API. Alternatively you can use the browser interface or consume the API with your favorite programming language.

1. Get all restaurants details by ID (GET): https://riki-restaurant-api.herokuapp.com/restaurants/

2. Get all restaurants details by ID (GET): https://riki-restaurant-api.herokuapp.com/restaurants/{id} 

3. Create a restaurant (POST): https://riki-restaurant-api.herokuapp.com/restaurants/

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

