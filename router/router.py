from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from service.calculator import Calculator

router = APIRouter()

# Use dict as the return type hint, or omit it and use Response if needed
@router.get("/health")
def health_check() -> dict: 
    try:
        # Return a Python dict. FastAPI handles the 200 status and JSON serialization.
        return {"message": "API is healthy"}
    except Exception as e:
        # To return a non-200 status on exception, you still need to use JSONResponse
        # OR raise an HTTPException, which is the preferred FastAPI way.
        return JSONResponse(content={"message": "API is unhealthy", "Error": str(e)}, status_code=500)
        
@router.post("/calculate")
async def _calculator_(request: Request):
    data = await request.json()
    
    if not isinstance(data, dict):
        return JSONResponse(content={"message":f"Data type is not json or dict. type: {type(data)}"}, status_code=400)
    
    try:
        cal_obj = Calculator(data)
        result = cal_obj.calculate_()
        return {"message": result} 
        
    except Exception as e:
        return JSONResponse(content={"message": "API Error", "Error":str(e)}, status_code=500)