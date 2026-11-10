Name: redborder-sfacctd
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder sfacctd systemd unit running x2kafka.

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-sfacctd
Source0: %{name}-%{version}.tar.gz

Requires: x2kafka
Obsoletes: pmacct

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/sfacctd.service %{buildroot}/usr/lib/systemd/system/sfacctd.service

%pre

%post
systemctl daemon-reload

%files
%defattr(0644,root,root)
/usr/lib/systemd/system/sfacctd.service
%doc

%changelog
* Mon Nov 09 2026 Juan Soto <jsoto@redborder.com> - 1.0.0-1
- first spec version, sfacctd service runs x2kafka and replaces pmacct
