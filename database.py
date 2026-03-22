import sqlite3 as sql

conn = sql.connect("JackHartfield.db")
conn.execute("PRAGMA foreign_keys = ON;")

## Create Membership table first (##
conn.execute("""
CREATE TABLE IF NOT EXISTS Membership (
    Membership_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Joining_Fee BOOL NOT NULL,
    Annual_Subscription BOOL NOT NULL,
    Monthly_Subscription BOOL NOT NULL
);
""")

## Create Member table ##
conn.execute("""
CREATE TABLE IF NOT EXISTS Member (
    Member_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Password VARCHAR(100) NOT NULL,
    Membership_ID INTEGER,
    FOREIGN KEY (Membership_ID) REFERENCES Membership(Membership_ID)
);
""")

## Create Room Hire table ##
conn.execute("""
CREATE TABLE IF NOT EXISTS Room_Hire (
    Room_Hire_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Member_ID INTEGER NOT NULL,
    Date DATETIME NOT NULL,
    Event_Type TEXT NOT NULL,
    FOREIGN KEY (Member_ID) REFERENCES Member(Member_ID)
);
""")

conn.commit()
conn.close()
