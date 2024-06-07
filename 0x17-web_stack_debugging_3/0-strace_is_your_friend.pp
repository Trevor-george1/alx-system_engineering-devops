# fixes Apache 500 error and apache

exec { 'fix-wordpress':
    command => 'sed -i s/phpp/php/g /var/www/html',
    path    => '/usr/local/bin/:/bin/'
}
