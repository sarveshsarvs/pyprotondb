# ProtonDB Python Wrapper

This Python wrapper provides a simple interface to interact with ProtonDB, a custom TCP-based NoSQL database.  
It wraps ProtonDB commands into Python method calls, allowing you to execute database, collection, document, user, and utility commands through a consistent API.

---

## Complete Command Reference

## 1. Initialization
from ProtonDBclient import ProtonDBClient
client = ProtonDBClient("localhost", 9090, "admin420", "1234")  # Connect
client.close()  # Disconnect

## 2. 🗃️ Database Commands
client.driver.execute("db.create('mydb')")      # Create database
client.driver.execute("db.drop('mydb')")        # Delete database
client.driver.execute("db.use('mydb')")         # Switch to database
client.driver.execute("db.list()")               # List all databases

## 3.📁 Collection Commands
client.driver.execute("collection.create('users')")  # Create collection
client.driver.execute("collection.drop('users')")    # Delete collection
client.driver.execute("collection.list()")            # List collections

## 4. 📄  Document Commands

Insert Documents:
client.driver.execute('users.insert({"name":"John"})')                    # Insert single document
client.driver.execute('users.insert([{"name":"Alice"}, {"name":"Bob"}])') # Insert multiple documents

Query Documents:
client.driver.execute("users.print()")                   # Print all documents
client.driver.execute("users.print(age >= 18)")          # Print documents with filter

Update Documents:
client.driver.execute('users.update(add, {"role":"admin"}, name="John")')  # Add field "role":"admin" to docs where name="John"
client.driver.execute('users.update(drop, "temp_field")')                  # Remove field "temp_field" from all documents

Delete Documents:
client.driver.execute("users.remove(age < 18)")          # Remove documents matching condition
client.driver.execute("users.remove()")                  # Remove all documents

## 5. 👤 Profile (User) Commands
client.driver.execute('profile.create("user1", "pass123", "user")')  # Create user
client.driver.execute('profile.delete("user1")')                     # Delete user
client.driver.execute('profile.grant("user1", "mydb")')             # Grant access to database
client.driver.execute('profile.revoke("user1", "mydb")')            # Revoke access
client.driver.execute("profile.list()")                             # List all users

## 6. 🧰 Utility Commands
client.driver.execute("--help")      # Show help
client.driver.execute("--version")   # Show version
client.driver.execute("cls")         # Clear screen

## 7. 🧾Multi-line Insert Example
client.driver.execute('''users.insert(.
  {"name": "John", "age": 25},
  {"name": "Alice", "age": 30}
.)''')


## 8.📝Notes:
- Use client.driver.execute("<command>") to send any ProtonDB command string.
- Keep the command strings exactly as ProtonDB expects (quotes, parentheses, etc.).
- Close connection with client.close() after your operations to free resources.

