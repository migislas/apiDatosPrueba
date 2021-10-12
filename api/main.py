import uvicorn

from src.app import app

if __name__ == "__main__":
    """
        To debug in Development Environment, set var DEBUG=True.
    """

    uvicorn.run(
        'main:app',
        host= "0.0.0.0",
        port=8000,
        debug=False,
        reload=False,
        access_log=False
    )