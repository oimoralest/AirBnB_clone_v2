# this Puppet manifest configures a web server
package { 'nginx':
  ensure => installed,
}
exec { 'configuration':
  command  => '
  mkdir -p /data/web_static/releases/test
  mkdir -p /data/web_static/shared
  echo "Testing" > /data/web_static/releases/test/index.html
  ln -sf /data/web_static/releases/test /data/web_static/current
  chown -R ubuntu:ubuntu /data/
  sed -i "/listen 80 default_server;/a \ \tlocation \/hbnb_static {\n\t\talias
  \/data\/web_static\/current\/;\n}" /etc/nginx/sites-available/default
  service nginx restart',
  provider => 'shell'
}
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => package['nginx']
}
