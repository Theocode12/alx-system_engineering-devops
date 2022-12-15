#A file to correct the 500 server error

exec { 'correct-spelling erroe':
    command => 'sed -i s/phpp/php/g "/var/www/html/wp-settings.php"'
}
