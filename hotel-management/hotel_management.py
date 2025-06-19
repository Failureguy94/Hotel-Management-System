import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword",
    database="hotel_db"
)
cursor = conn.cursor()
def add_guest(name, phone, room):
    cursor.execute("SELECT status FROM rooms WHERE room_number = %s", (room,))
    room_status = cursor.fetchone()

    if room_status and room_status[0] == "Available":
        cursor.execute("INSERT INTO guests (name, phone, room_number) VALUES (%s, %s, %s)", (name, phone, room))
        cursor.execute("UPDATE rooms SET status = 'Occupied' WHERE room_number = %s", (room,))
        conn.commit()
        return f"Guest {name} checked into Room {room}"
    else:
        return "Room is not available!"
def remove_guest(guest_id):
    cursor.execute("SELECT room_number FROM guests WHERE id = %s", (guest_id,))
    room = cursor.fetchone()

    if room:
        cursor.execute("DELETE FROM guests WHERE id = %s", (guest_id,))
        cursor.execute("UPDATE rooms SET status = 'Available' WHERE room_number = %s", (room[0],))
        conn.commit()
        return "Guest checked out successfully."
    else:
        return "Guest not found!"
def get_guests():
    cursor.execute("SELECT * FROM guests")
    return cursor.fetchall()
def get_rooms():
    cursor.execute("SELECT * FROM rooms")
    return cursor.fetchall()

