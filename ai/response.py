import os
import cohere
from dotenv import load_dotenv

def respond(code):
    load_dotenv()

    co = cohere.Client(os.getenv("API_KEY"))
    prompt = '''This program generates tips on how to fix code that is vulnerable to sql injection.

    Prompt: The following code is vulnerable to SQL injection. How can it be fixed?
    ```
    $username = $_POST['username'];
    $password = $_POST['password'];

    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    $result = mysqli_query($connection, $query);
    ```

    Suggestion 1: Use prepared statements with parameterized queries to automatically escape any user input.
    Suggestion 2: Use the mysqli_real_escape_string() function to escape any special characters in user input before using it in an SQL query.
    Suggestion 3: Use an ORM (Object-Relational Mapping) library like Doctrine or Eloquent to handle the SQL queries, which provide a more secure way to handle user input.
    --  
    Prompt: "The following code is vulnerable to SQL injection. How can it be fixed?
    ```
    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
    ```
    Suggestion 1: Use prepared statements with parameterized queries instead of concatenating user input into the SQL query.
    Suggestion 2: Use a library like pg-escape to escape any special characters in user input before using it in an SQL query.
    Suggestion 3: Use an ORM (Object-Relational Mapping) library like Sequelize or TypeORM to handle the SQL queries, which provide a more secure way to handle user input.
    --  
    Prompt: The following code is vulnerable to SQL injection. How can it be fixed?
    ```
    string query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";

    SqlCommand command = new SqlCommand(query, connection);
    SqlDataReader reader = command.ExecuteReader();
    ```
    Suggestion 1: Use prepared statements with parameterized queries to automatically escape any user input.
    Suggestion 2: Use the SqlCommand.Parameters.AddWithValue() method to add user input as a parameter to the SQL query.
    Suggestion 3: Use an ORM (Object-Relational Mapping) library like Entity Framework or NHibernate to handle the SQL queries, which provide a more secure way to handle user input.
    --  
    Prompt: The following code is vulnerable to SQL injection. How can it be fixed?
    ```
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
    result = cursor.fetchall()
    ```
    
    Suggestion 1: Use prepared statements with parameterized queries to automatically escape any user input.
    Suggestion 2: Use the psycopg2.extras.execute_values() method to pass a tuple of values to be used in the query instead of concatenating user input into the SQL query.
    Suggestion 3: Use an ORM (Object-Relational Mapping) library like SQLAlchemy or Django ORM to handle the SQL queries, which provide a more secure way to handle user input.
    -- 
    Prompt: The following code is vulnerable to SQL injection. How can it be fixed?
    ```
    String query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
    
    PreparedStatement statement = connection.prepareStatement(query);
    ResultSet result = statement.executeQuery();
    ```
    Suggestion 1: Use prepared statements with parameterized queries to automatically escape any user input.
    Suggestion 2: Use the PreparedStatement.setString() method to set user input as a parameter to the SQL query instead of concatenating it into the query string.
    Suggestion 3: Use an ORM (Object-Relational Mapping) library like Hibernate or EclipseLink to handle the SQL queries, which provide a more secure way to handle user input.
    --
    Prompt: The following code is vulnerable to SQL injection. How can it be fixed? \n```''' + code + '```'

    response = co.generate(
        model='xlarge',
        prompt = prompt,
        max_tokens=150,
        end_sequences=["--"],
        temperature=0.75)

    return response.generations[0].text
    
