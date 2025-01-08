<?php
session_start();

// Liste des administrateurs autorisés
$admins = [
    "Rodrigo" => "Rodri06?!", // Nom d'utilisateur => mot de passe
    "Noé" => "Noé_boom",
];

// Récupérer les données du formulaire
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

// Vérifier si l'utilisateur est un administrateur valide
if (isset($admins[$username]) && $admins[$username] === $password) {
    $_SESSION['admin'] = $username;
    header('Location: admin_dashboard.php');
    exit;
} else {
    header('Location: admin_login.php?error=Identifiants incorrects.');
    exit;
}
?>
