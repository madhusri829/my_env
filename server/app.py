def main():
    import uvicorn
    # This tells the server to run on port 8000
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()