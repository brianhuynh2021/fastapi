- Go to localhost:8000/docs to see docs API
- How to run the app? It is easy just open terminal and use commands: <uvicorn app.main:app> then hit enter
- Password for database postgres: 54321
- Connect Postgres database to Python: 
    <!-- conn = psycopg2.connect(
    host="localhost",
    database="fastapi",
    user="postgres",
    password="54321",
    cursor_factory=RealDictCursor) -->
- Use ORM (Object relational mapper) for management database
- File database.py is a file for connection database (here we using posgresql) and backend