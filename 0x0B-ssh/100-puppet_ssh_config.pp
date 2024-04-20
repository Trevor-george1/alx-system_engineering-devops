# using puppet to make changes to the default ssh config file
# so that one can cponnect to a server without tyoing a password.

exec {'ssh_config':
    path    => '/bin',
    command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}