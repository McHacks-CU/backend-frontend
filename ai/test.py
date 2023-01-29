from model import classify

userinput = '''$username = $_POST['username'];
$password = $_POST['password'];

$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($conn, $query);
'''

if (not classify(userinput)):
    print("Bad code: output = ...")

else:
    print("Good code")