if __name__ == "__main__":
    import uvicorn
    # This starts the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)