<html>
<head>
    <title>Game Details</title>
</head>
<body>
    <?php
    print_r(<h1><a href="{{ url_for('read_games', id=id) }}">Game ID: {{ games[0].game_id, games[0].title, games[0].developer, games[0].publisher, games[0].tag, games[0].platform }}</a></h1>)
    ?>
</body>
</html>