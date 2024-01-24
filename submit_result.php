<?php
// Database connection parameters
$host = 'localhost';
$username = 'crypto';
$password = 'kx)BKAuM/gUFXYly';
$database = 'blockchain';

// File to store the balance
$balanceFile = 'balance.txt';

// Get the result from the POST request
$result = $_POST['result'];

// Read the current balance from the file
$currentBalance = (float)file_get_contents($balanceFile);

// Update the balance
$newBalance = $currentBalance + 1;

// Update the balance in the file
file_put_contents($balanceFile, $newBalance);

// Update the balance in the MySQL database
$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Update the balance in the database
$sql = "UPDATE balance SET balance = $newBalance WHERE user = test"; // Adjust user_id according to your database structure

if ($conn->query($sql) === TRUE) {
    echo "Received Result: " . $result . "<br>";
    echo "Updated Balance: " . $newBalance;
} else {
    echo "Error updating balance: " . $conn->error;
}

// Close the database connection
$conn->close();
?>
