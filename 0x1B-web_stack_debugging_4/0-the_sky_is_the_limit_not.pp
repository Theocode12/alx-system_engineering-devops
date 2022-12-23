# fix for file limit(ulimit) tasks

exec { 'ulimit fix':
  command => '/bin/sed -i "s/ULIMIT/# ULIMIT/g" "/etc/default/nginx"; /usr/sbin/service nginx restart'
}
