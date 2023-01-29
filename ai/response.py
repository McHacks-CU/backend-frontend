import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("API_KEY"))

response = co.generate(
    model='command-medium-nightly',
    prompt = '''This program generates tips on how to fix code that is vulnerable to sql injection.

Prompt: "The following code is vulnerable to SQL injection. How can it be fixed?
$username = $_POST['username'];
$password = $_POST['password'];

$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($connection, $query);

if (mysqli_num_rows($result) > 0) {
    // login successful
} else {
    // login failed
}
"
Completion 1: Use prepared statements with parameterized queries to automatically escape any user input.
Completion 2: Use the mysqli_real_escape_string() function to escape any special characters in user input before using it in an SQL query.
Completion 3: Use an ORM (Object-Relational Mapping) library like Doctrine or Eloquent to handle the SQL queries, which provide a more secure way to handle user input.
--  
Prompt: "The following code is vulnerable to SQL injection. How can it be fixed?
const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

client.query(query, (err, res) => {
    if (err) {
        console.log(err.stack)
    } else {
        if (res.rows.length > 0) {
            // login successful
        } else {
            // login failed
        }
    }
});
"
Completion 1: Use prepared statements with parameterized queries instead of concatenating user input into the SQL query.
Completion 2: Use a library like pg-escape to escape any special characters in user input before using it in an SQL query.
Completion 3: Use an ORM (Object-Relational Mapping) library like Sequelize or TypeORM to handle the SQL queries, which provide a more secure way to handle user input.
--  
Prompt: "The following code is vulnerable to SQL injection. How can it be fixed?
string query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";

SqlCommand command = new SqlCommand(query, connection);
SqlDataReader reader = command.ExecuteReader();

if (reader.HasRows)
{
    // login successful
}
else
{
    // login failed
}
"
Completion 1: Use prepared statements with parameterized queries to automatically escape any user input.
Completion 2: Use the SqlCommand.Parameters.AddWithValue() method to add user input as a parameter to the SQL query.
Completion 3: Use an ORM (Object-Relational Mapping) library like Entity Framework or NHibernate to handle the SQL queries, which provide a more secure way to handle user input.
--  
Prompt: "The following code is vulnerable to SQL injection. How can it be fixed?
cursor.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
result = cursor.fetchall()

if len(result) > 0:
    # login successful
else:
    # login failed
"
Completion 1: Use prepared statements with parameterized queries to automatically escape any user input.
Completion 2: Use the psycopg2.extras.execute_values() method to pass a tuple of values to be used in the query instead of concatenating user input into the SQL query.
Completion 3: Use an ORM (Object-Relational Mapping) library like SQLAlchemy or Django ORM to handle the SQL queries, which provide a more secure way to handle user input.
--  
Prompt: "The following code is vulnerable to SQL injection. How can it be fixed?
query = "SELECT * FROM users WHERE username = '#{username}' AND password = '#{password}'"
result = connection.exec(query)

if result.ntuples > 0
    # login successful
else
    # login failed
end
"
Completion 1: Use prepared statements with parameterized queries to automatically escape any user input.
Completion 2: Use the pg gem's escape() method to escape any special characters in user input before using it in an SQL query.
Completion 3: Use an ORM (Object-Relational Mapping) library like ActiveRecord or Sequel to handle the SQL queries, which provide a more secure way to handle user input.
--
Prompt: "The following code is vulnerable to SQL injection. How can it be fixed?
String query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";

PreparedStatement statement = connection.prepareStatement(query);
ResultSet result = statement.executeQuery();

if (result.next()) {
    // login successful
} else {
    // login failed
}
"
Completion 1: Use prepared statements with parameterized queries to automatically escape any user input.
Completion 2: Use the PreparedStatement.setString() method to set user input as a parameter to the SQL query instead of concatenating it into the query string.
Completion 3: Use an ORM (Object-Relational Mapping) library like Hibernate or EclipseLink to handle the SQL queries, which provide a more secure way to handle user input.
--
"The following code is vulnerable to SQL injection. How can it be fixed?
    const username = "testuser";
const password = "testpassword";
const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

connection.query(query, (error, result) => {
    if (error) {
        console.log(error);
    } else {
        if (result.length > 0) {
            console.log("login successful");
        } else {
            console.log("login failed");
        }
    }
});
"
''',
    max_tokens=400,
    stop_sequences=["--"],
    temperature=0.75)

output = response.generations[0].text
print(output)
