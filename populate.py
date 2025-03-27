import sqlite3
import random

def generate_room_number():
    """Generate a random room number in the required format."""
    prefixes = ['BH', 'KH', 'JK', 'AK', 'HM']
    number = random.randint(1, 99)  # XX in the range 01 to 99
    return f"{random.choice(prefixes)}-{number:02}"

def add_fake_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # License plates with specific constraints
    specific_plates = [
        "DL11SQ1048", "UP21DC3909", "UP81AM0613", "UP81BL6524", "UP11AN1360", 
        "UP81DF0922", "UP32DJ1817", "UP19A8802", "UP43AF9198", "UP81BF-7350", 
        "UP81AS9225", "UP81CW8776", "UP61J3718", "UP81BA1571", "UP83F4653", 
        "UP81BB3989", "UP81CW6632", "UP81DC1447", "UP81BE7376", "UP53DS8089", 
        "UP81K5539", "UP57AP1393", "UP20AM4903", "UP15CZ7054", "UP70FE6182", 
        "UP13BP7898", "UP81BK4505", "UP81BQ3021", "UP81CH4882", "UP13AY8560", 
        "UP81BY1921", "UP81AQ6452", "UP23AA6251"
    ]

    departments = [
        "Computer Engineering", "Mechanical Engineering", "Civil Engineering", 
        "Electrical Engineering", "Electronics Engineering", "Chemical Engineering", 
        "Petroleum Studies", "Architecture", "Applied Physics", "Applied Chemistry"
    ]

    names_male = [
        "Abdullah Khan", "Zaid Ahmad", "Ibrahim Malik", "Hamza Rahman", "Ali Sheikh",
        "Salman Farooq", "Faisal Khan", "Omar Qureshi", "Aamir Ansari", "Yusuf Khalid"
    ]

    # Add specific license plates
    students = []
    for plate in specific_plates:
        name = random.choice(names_male)
        department = random.choice(departments)
        room = generate_room_number()
        enrollment_no = f"GN{random.randint(1000, 9999)}"
        students.append((plate, name, enrollment_no, "Sir Shah Sulaiman Hall", room, department))

    # Generate additional records
    halls = [
        "Begum Sultan Jahan Hall", "Sir Syed Hall (North)", "Sir Syed Hall (South)",
        "Mohammad Habib Hall", "Abdullah Hall"
    ]

    names_female = [
        "Ayesha Siddiqui", "Fatima Noor", "Sara Khan", "Maryam Rahman", "Zara Qureshi", 
        "Hina Ansari", "Rida Malik", "Sania Ahmed", "Mehak Yusuf", "Zainab Khalid"
    ]

    for _ in range(150 - len(specific_plates)):
        plate = f"UP{random.randint(10, 99)}{random.choice(['AM', 'DC', 'BL', 'AS', 'CW'])}{random.randint(1000, 9999)}"
        name = random.choice(names_male + names_female)
        department = random.choice(departments)
        hall = random.choice(halls)
        room = generate_room_number()
        enrollment_no = f"GN{random.randint(1000, 9999)}"
        students.append((plate, name, enrollment_no, hall, room, department))

    cursor.executemany('''
    INSERT OR REPLACE INTO students (license_plate, name, enrollment_no, hall, room_no, department)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', students)

    conn.commit()
    conn.close()
    print(f"Successfully added {len(students)} records.")

if __name__ == "__main__":
    add_fake_students()
