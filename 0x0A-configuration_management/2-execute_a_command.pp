# Manifest that kills a process

exec { 'kill process':
  command => '/bin/pkill killmenow',
}
