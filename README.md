# redborder-sfacctd

Systemd unit that runs [x2kafka](https://github.com/redBorder/x2kafka) as the `sfacctd` service (sflow collector, UDP 6343).

The configuration (`/etc/sfacctd/config.json`) is rendered by Chef. This package replaces the legacy `pmacct` package.
