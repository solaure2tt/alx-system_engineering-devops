# create a manifest that kills a process named killmenow
exec { 'Kill a process killmenow',
  command => 'pkill -f killmenow',
  provider => shell,
}
