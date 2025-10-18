from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_table_data(table_name):
    table_name=table_name.strip()
    """
    Fetch all rows from the given Supabase table.
    """
    try:
        response = supabase.table(table_name).select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error fetching data from table {table_name}: {e}")
        return []

def insert_table_data(table_name, data: dict):
    """
    Insert a new row into the specified table.
    """
    try:
        response = supabase.table(table_name).insert(data).execute()
        return response.data
    except Exception as e:
        print(f"Error inserting data into table {table_name}: {e}")
        return []

def update_table_data(table_name, row_id, data: dict):
    """
    Update a row by id.
    """
    try:
        response = supabase.table(table_name).update(data).eq("id", row_id).execute()
        return response.data
    except Exception as e:
        print(f"Error updating table {table_name}: {e}")
        return []

def delete_table_data(table_name, row_id):
    """
    Delete a row by id.
    """
    try:
        response = supabase.table(table_name).delete().eq("id", row_id).execute()
        return response.data
    except Exception as e:
        print(f"Error deleting from table {table_name}: {e}")
        return []
def printhello():
    print("Hello World")