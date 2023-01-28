# Install nginx web server using puppet
package { 'nginx':
	ensure => 'present',
}
execute { 'install':
	command => 'sudo apt-get update; sudo apt-get -y install nginx',
}
execute { 'Hello':
	command => 'echo "Hello World!" > /var/www/html/index.html'
}
file_line { 'sudo sed -i':
	path   => '/etc/nginx/sites-available/default',
	after  => 'listen 80 default_server;',
	line   => 'rewrite ^\/redirect_me return 301 Moved Permanently https:\/\/www.youtube.com\/@eliasd342 permanent;',
}
execute { 'run':
	command => 'sudo service nginx restart',
}
