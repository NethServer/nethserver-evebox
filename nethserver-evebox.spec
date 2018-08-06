Summary: NethServer configuration for EveBox
Name: nethserver-evebox
Version: 1.0.2
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-suricata
Requires: evebox

BuildRequires: nethserver-devtools 

%description
NethServer configuration for EveBox

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist
mkdir -p %{buildroot}/var/lib/evebox

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%dir %attr(0755, suricata, suricata) /var/lib/evebox

%changelog
* Mon Aug 06 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Storage Location of  GeoLite2-City.mmdb.gz - NethServer/dev#5559

* Mon Apr 30 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Evebox: update to release 0.9.0 - NethServer/dev#5472

* Fri Oct 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- EveBox NethServer/dev#5346

