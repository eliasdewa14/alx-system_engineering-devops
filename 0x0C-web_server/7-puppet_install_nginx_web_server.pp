# Install nginx web server using puppet
package { 'nginx':
	ensure => installed,
}
file_line { 'install':
	ensure => 'present',
	path   => '/etc/nginx/sites-available/default',
	after  => 'listen 80 default_server;',
	line   => 'rewrite ^/redirect_me https://www.youtube.com/channel/UC0ypST9g7cIDMjgGq9cgkJg permanent;',
}
file { '/etc/nginx/html/index.html':
	content => 'Hello World!',
} 
