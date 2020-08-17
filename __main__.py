from app import  app
import settings


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=settings.PORT)
    except:
        logger.error(f"Could not start service : {e}")
        
    