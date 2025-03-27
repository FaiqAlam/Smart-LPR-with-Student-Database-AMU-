import sqlite3

def get_student_info(license_plate):
    """
    Retrieve student information based on license plate
    
    Args:
        license_plate (str): License plate to search for
    
    Returns:
        tuple: Student information or None if not found
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        
        # Execute query to find student by license plate
        cursor.execute('''
            SELECT name, enrollment_no, hall, room_no, department 
            FROM students 
            WHERE license_plate = ?
        ''', (license_plate,))
        
        # Fetch the result
        student = cursor.fetchone()
        
        # Close the connection
        conn.close()
        
        # Return student info if found, else None
        return student
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def normalize_license_plate(plate):
    """
    Normalize license plate for more flexible matching
    
    Args:
        plate (str): Raw license plate string
    
    Returns:
        str: Normalized license plate
    """
    # Remove spaces, convert to uppercase
    return plate.replace(' ', '').upper()