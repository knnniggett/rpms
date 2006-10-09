# $Id$
# Authority: matthias
# Dist: nodist

# We have only executables with no debugging symbols, so no need for an empty
# debuginfo package.
%define debug_package %{nil}

Summary: Regulatory Daemon for Intel® PRO/Wireless 3945 network adaptors
Name: ipw3945d
Version: 1.7.22
Release: 1
License: Distributable
Group: System Environment/Kernel
URL: http://bughost.org/ipw3945/
Source: http://bughost.org/ipw3945/daemon/ipw3945d-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
ExclusiveArch: i386 x86_64

%description
The regulatory daemon is responsible for controlling and configuring aspects
of the hardware required to operate the device within compliance of various
regulatory agencies.  This includes controlling which channels are allowed to
do active/passive scanning, transmit power levels, which channels are allowed
to be transmitted on, and support for IEEE 802.11h (DFS and TPC).


%prep
%setup


%build


%install
%{__rm} -rf %{buildroot}
%ifarch i386
%{__install} -D -p -m 0755 x86/ipw3945d %{buildroot}/sbin/ipw3945d
%endif
%ifarch x86_64
%{__install} -D -p -m 0755 x86_64/ipw3945d %{buildroot}/sbin/ipw3945d
%endif


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE.ipw3945d README.ipw3945d
/sbin/ipw3945d


%changelog
* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 1.7.22-1
- Update to 1.7.22.

* Thu Mar 30 2006 Matthias Saou <http://freshrpms.net/> 1.7.18-1
- Initial RPM release.

