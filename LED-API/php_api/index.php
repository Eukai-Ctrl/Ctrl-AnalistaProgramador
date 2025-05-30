<?php
require __DIR__ . '/vendor/autoload.php';

use Dotenv\Dotenv;
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

// 1. Carga .env
$dotenv = Dotenv::createImmutable(__DIR__ . '/..');
$dotenv->load();

// 2. Conexión PDO
$host = 'db';
$port = '5432';
$db   = $_ENV['POSTGRES_DB'];
$user = $_ENV['POSTGRES_USER'];
$pass = $_ENV['POSTGRES_PASSWORD'];

$dsn = "pgsql:host=$host;port=$port;dbname=$db";
$pdo = new PDO($dsn, $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);

$app = AppFactory::create();

// Listar fichas
$app->get('/fichas', function (Request $request, Response $response) use ($pdo) {
    $stmt = $pdo->query('SELECT id, nombre, curso, diagnostico FROM fichas');
    $fichas = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $response->getBody()->write(json_encode($fichas));
    return $response->withHeader('Content-Type', 'application/json');
});

// Crear ficha
$app->post('/fichas', function (Request $request, Response $response) use ($pdo) {
    $data = json_decode($request->getBody()->getContents(), true);
    $sql = 'INSERT INTO fichas(nombre, curso, diagnostico) VALUES (:nombre, :curso, :diagnostico) RETURNING id';
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        'nombre'     => $data['nombre'],
        'curso'      => $data['curso'],
        'diagnostico'=> $data['diagnostico'] ?? null,
    ]);
    $id = $stmt->fetchColumn();
    $response->getBody()->write(json_encode(['id' => $id]));
    return $response->withHeader('Content-Type', 'application/json')->withStatus(201);
});

$app->run();
