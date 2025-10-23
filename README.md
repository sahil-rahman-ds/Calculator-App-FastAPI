# Calculator API

A FastAPI-based Calculator API that provides basic arithmetic operations through RESTful endpoints.

## Project Structure

```
CALCULATOR-APP-FASTAPI/
├── config/                  # Configuration files
│   └── config.py
├── router/                  # API endpoints definition
│   └── router.py            # Contains FastAPI router definitions
├── service/                 # Business logic layer
│   └── calculator.py        # The core Calculator class logic
├── venv/                    # Python virtual environment
├── app.py                   # Main FastAPI application entry point
└── requirements.txt         # Project dependencies
```

## Features

- Basic arithmetic operations (Addition, Subtraction, Multiplication, Division)
- Health check endpoint
- Error handling for invalid operations
- JSON-based request/response format

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/sahil-rahman-ds/Calculator-App-FastAPI.git
cd Calculator-App-FastAPI
```

### 2. Create and activate a virtual environment:

**Create venv**
```bash
python -m venv venv
```

**Activate venv (Windows)**
```bash
.\venv\Scripts\activate
```

**Activate venv (macOS/Linux)**
```bash
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
uvicorn app:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Access the interactive API documentation at `http://localhost:8000/docs`

## API Endpoints

### Health Check
```
GET /health
```
Returns the health status of the API.

### Calculate
```
POST /calculate
```
Performs arithmetic calculations based on the provided input.

Request body format:
```json
{
    "a": number,
    "b": number,
    "operator": string
}
```

Supported operators:
- `"add"` - Addition
- `"subtract"` - Subtraction
- `"multiply"` - Multiplication
- `"divide"` - Division

Example request:
```json
{
    "a": 10,
    "b": 5,
    "operator": "add"
}
```

Example response:
```json
{
    "message": 15
}
```

## Error Handling

The API includes error handling for:
- Invalid JSON format
- Division by zero
- Invalid operators
- Server errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the LICENSE [LICENSE] file included in the repository.

## Author

[sahil-rahman-ds](https://github.com/sahil-rahman-ds)
