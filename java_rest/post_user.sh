curl -H "Content-Type: application/json" -X POST  \
    --data '{"firstName": "Joe", "lastName": "Smith", "zipcode": "97756", "email": "joe.smith@gmail.com"}' \
    http://localhost:8080/users
