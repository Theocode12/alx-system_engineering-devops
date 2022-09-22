# A puppet manifest to configure ubuntu

file { 'index.html':
  path => '/var/www/html/index.html',
  content => 'Hello World!',
  ensure => 'present',
}

exec { 'install nginx':
  command => "/bin/bash apt-get update;/bin/bash apt-get install nginx",
}

exec { 'redirect':
  command => '/usr/bin/sed -i "/server_name _;/a \\\n\tlocation /redirect_me {\n\t\treturn 301 https://github.com/odelolajosh;\n\t}" /etc/nginx/sites-available/default; service nginx start',
}
