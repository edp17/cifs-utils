Name:           cifs-utils
Version:        7.0
Release:        1
Summary:        Utilities for mounting and managing CIFS mounts
License:        GPLv3
URL:            https://github.com/edp17/cifs-utils
Source0:        %{name}-%{version}.tar.gz

%description
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains tools for mounting
shares on Linux using the SMB/CIFS protocol. The tools in this package
work in conjunction with support in the kernel to allow one to mount a
SMB/CIFS share onto a client and use it as if it were a standard Linux
file system.

%prep
%setup

%install
mkdir -p %{buildroot}/sbin

install -D -m644 config/mount.cifs %{buildroot}/sbin/mount.cifs
install -D -m644 config/cifsidmap.h %{buildroot}/usr/local/include/cifsidmap.h

%clean
rm -rf $RPM_BUILD_ROOT

%post
chmod +x /sbin/mount.cifs
ln -s /sbin/mount.cifs /sbin/mount.sbm3

%files
%defattr(-,root,root,-)
/sbin/mount.cifs
/usr/local/include/cifsidmap.h