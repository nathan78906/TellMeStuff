1. Visit signin page to get csrftoken cookie

`curl -v -s -c cookies.txt -b cookies.txt -e 127.0.0.1:8000/signin/ 127.0.0.1:8000/signin/`
   
2. `grep csrftoken cookies.txt | sed 's/^.*csrftoken\s*//'`
`A9FXnQoVHKBIukvx3UtCRgWY48yC7btkIlUGwjdkPz8hy4dQ3xByRUpimrUpK6Om`

3. Use X-CSRFToken header to signin and get session ID

`curl -v -s -c cookies.txt -b cookies.txt -e 127.0.0.1:8000/signin/ -H "Content-Type: application/json" -H "X-CSRFToken: A9FXnQoVHKBIukvx3UtCRgWY48yC7btkIlUGwjdkPz8hy4dQ3xByRUpimrUpK6Om" -d '{"username":"thierry","password":"asd"}' -X POST 127.0.0.1:8000/api/signin/`

4. Do any logged in request

`curl -v -s -c cookies.txt -b cookies.txt -e 127.0.0.1:8000/signin/ -H "Content-Type: application/json" -H "X-CSRFToken: A9FXnQoVHKBIukvx3UtCRgWY48yC7btkIlUGwjdkPz8hy4dQ3xByRUpimrUpK6Om" 127.0.0.1:8000/api/user/`
