# URL Shortener Service

This project provides a URL shortening service using Flask and SQLAlchemy. It allows users to shorten long URLs and manage expiration dates for those shortened links.

## Features

- **Shorten URL Endpoint:** `/shorten`
  - Method: POST
  - JSON Payload: `{ "original_url": "https://example.com" }`
  - Returns: `{ "short_url": "http://127.0.0.1:8590/<short_code>" }`

- **Redirect Short URL Endpoint:** `/<short_code>`
  - Redirects to the original URL if found, otherwise returns a 404 error.

- **Expiration Handling:**
  - Shortened URLs expire automatically after 30 days by default.
  - Expired entries are removed using a background task (`expire_remove.py`).

## Setup

1. **Clone the repository:**
   ```bash
   git clone <git@github.com:sinmajidi/link-shortener.git>
   cd url-shortener
   ```
2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
3. **Database Initialization:**


* The SQLite database file (link_shortener.db) will be created automatically upon running the application.
4. **Run the Application:**


    ```bash
    python main.py
    ```
* This will start the Flask application on http://127.0.0.1:8590/.


# Usage

Send a POST request to /shorten endpoint with JSON payload containing original_url.

Example:

```bash

curl -X POST -H "Content-Type: application/json" -d '{"original_url": "https://example.com"}' http://127.0.0.1:8590/shorten
```
Response:
```json

{
  "short_url": "http://127.0.0.1:8590/<short_code>"
}
```

# Access Shortened URL
Navigate to http://127.0.0.1:8590/<short_code> in a browser to be redirected to the original URL.

Expiration Management
Expired entries are automatically removed. To manually run expiration check and cleanup, execute `expire_remove.py`.

```bash

python expire_remove.py
```
### Contributing
Feel free to fork this repository, submit issues, and pull requests.


This project design is inspired by Sina Majidi at [Afra IoT](https://afraiot.org).