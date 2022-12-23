# fix for holberton user tasks

exec { 'holberton user fix':
  command => '/bin/sed -i "s/holberton/# holberton/g" "/etc/security/limits.conf"'
}
