from router.router import router as api_router
from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI(title="Calculator API")

# Include the router
app.include_router(api_router)


# Run with: uvicorn app:app --reload
@app.get("/")
async def root():
    return {"message": "Welcome to the Calculator API!"}