%define name dssh
%define version 0.1
%define release  %mkrel 5

Summary: Remote command via ssh
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Networking/Remote access
Url: http://dssh.subverted.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
requires: perl	

%description
Remote command via ssh.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/dssh/node_groups
cp -vf %{_builddir}/%name-%version/dssh %{buildroot}%{_bindir}
cp -vf %{_builddir}/%name-%version/dssh.1 %{buildroot}%{_mandir}/man1

cat > %{buildroot}%{_sysconfdir}/dssh/node_groups/ALL <<EOF
# username@host:port
# ex: root@n1:22
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README TODO 
%attr(755,root,root) %{_bindir}/dssh
%{_mandir}/man1/dssh.1*
%config(noreplace) %{_sysconfdir}/dssh/node_groups/ALL

