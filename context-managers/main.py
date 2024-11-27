import psutil
import os
import time
from contextlib import contextmanager
from memory_profiler import profile
import sqlite3
from typing import List, Generator
import gc

# Context manager for database connection
@contextmanager
def db_connection() -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect('test.db')
    try:
        yield conn
    finally:
        conn.close()

# Context manager for memory measurement
@contextmanager
def measure_memory() -> Generator[None, None, None]:
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024 / 1024  # MB
    gc.collect()  # Force garbage collection before measurement
    
    yield
    
    gc.collect()  # Force garbage collection after operation
    mem_after = process.memory_info().rss / 1024 / 1024  # MB
    print(f"Memory used: {mem_after - mem_before:.2f} MB")

# Function without context manager
@profile
def process_data_without_cm(iterations: int) -> List[dict]:
    results = []
    for _ in range(iterations):
        # Create new connection each time
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        
        # Simulate some data processing
        cursor.execute("SELECT * FROM large_table")
        data = cursor.fetchall()
        
        # Process data
        processed = [{'id': row[0], 'value': row[1] * 2} for row in data]
        results.extend(processed)
        # get_open_db_conn()
        # Should close connection, but might forget or error might occur
        # conn.close()  # Commented out to simulate forgotten cleanup
    
    return results

# Function with context manager
@profile
def process_data_with_cm(iterations: int) -> List[dict]:
    results = []
    for _ in range(iterations):
        with db_connection() as conn:
            cursor = conn.cursor()
            
            # Simulate some data processing
            cursor.execute("SELECT * FROM large_table")
            data = cursor.fetchall()
            
            # Process data
            processed = [{'id': row[0], 'value': row[1] * 2} for row in data]
            results.extend(processed)
            # get_open_db_conn()

            
    return results

def setup_database() -> None:
    """Create test database with sample data"""
    with db_connection() as conn:
        cursor = conn.cursor()
        
        # Create test table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS large_table (
                id INTEGER PRIMARY KEY,
                value INTEGER
            )
        """)
        
        # Insert sample data
        cursor.execute("DELETE FROM large_table")
        cursor.executemany(
            "INSERT INTO large_table (value) VALUES (?)",
            [(i,) for i in range(10000)]
        )
        conn.commit()
    
def get_open_db_conn():
    process = psutil.Process(os.getpid())
    open_files = process.open_files()
    db_files = [f for f in open_files if 'test.db' in str(f.path)]
    print(f"Open database connections: {len(db_files)}")

def compare_memory_usage(iterations: int = 100) -> None:
    """Compare memory usage between the two approaches"""
    print("Testing function without context manager:")
    with measure_memory():
        process_data_without_cm(iterations)
        
    
    # Force cleanup before next test
    gc.collect()
    time.sleep(1)  # Allow time for system to stabilize
    
    print("\nTesting function with context manager:")
    with measure_memory():
        process_data_with_cm(iterations)
        

def main() -> None:
    # Setup test database
    setup_database()
    # import calculator/

    # Run memory comparison
    print("Running memory comparison...")
    print("=" * 50)
    compare_memory_usage(iterations=100000)
    
    # Check for remaining connections
    print("\nChecking for remaining database connections...")
    process = psutil.Process(os.getpid())
    open_files = process.open_files()
    db_files = [f for f in open_files if 'test.db' in str(f.path)]
    print(f"Open database connections: {len(db_files)}")

if __name__ == "__main__":
    main()