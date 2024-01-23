#!/usr/bin/puppet

# Ensure pip3 is up-to-date
exec { 'update-pip3':
  command => 'pip3 install --upgrade pip',
  path    => ['/usr/bin', '/usr/local/bin'],
}

# Install Flask (2.1.0) and upgrade Werkzeug
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['update-pip3'],
}

# Upgrade Werkzeug to a version compatible with Flask 2.1.0
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Exec['update-pip3'],
}
