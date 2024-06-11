## API Endpoints
- An API endpoint (/api/advertisement/) that allows fetching details of an advertisement by its external ID. This endpoint requires an API key for access.
## Authentication and API Keys
Users can register and authenticate themselves to receive a unique API key.
The API key is used to authorize requests to the API endpoints.
## Getting Started
To set up the project locally, follow these steps:
1. Clone the repository:
```
git clone https://github.com/yourusername/it-solutions.git
cd it-solutions
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Apply migrations:
```
python manage.py migrate
```
4. Start the development server:
```
python manage.py runserver
```
## Usage
Accessing the Landing Page
Visit http://127.0.0.1:8000/ in your browser to view the landing page.
Admin user login `admin` password is `1`
### Using the API Endpoint
To fetch an advertisement, make a GET request to `/api/advertisement/?id=<EXTERNAL_ID>&api_key=<YOUR_API_KEY>`
