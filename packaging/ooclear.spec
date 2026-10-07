Name:           ooclear
Version:        0.1.0
Release:        1%{?dist}
Summary:        High-performance screen clearing and scrollback purge with VT100/ANSI compliance.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooclear
Source0:        ooclear-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooclear is a sovereign, capability-bounded BUFFER PURGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooclear
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooclear-uninstall

%files
/usr/bin/ooclear
/usr/bin/ooclear-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
