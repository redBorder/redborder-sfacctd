# redborder-sfacctd

Systemd unit that runs [x2kafka](https://github.com/redBorder/x2kafka) as the `sfacctd` service (sflow collector, UDP 6343).

The configuration (`/etc/sfacctd/config.json`) is rendered by Chef.

The unit is installed in `/etc/systemd/system`, so it takes precedence over the `sfacctd.service` of the legacy `pmacct` package, which stays installed because `rb-exporter` needs its `pmacctd`. Do not remove `pmacct` while this service runs: its uninstall script disables and stops `sfacctd.service`.
