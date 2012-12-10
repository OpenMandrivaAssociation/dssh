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
cp -vf $RPM_BUILD_DIR/%name-%version/dssh %{buildroot}%{_bindir}
cp -vf $RPM_BUILD_DIR/%name-%version/dssh.1 %{buildroot}%{_mandir}/man1

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdv2011.0
+ Revision: 617903
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2010.0
+ Revision: 428389
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2009.0
+ Revision: 244552
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 04 2007 Thierry Vignaud <tv@mandriva.org> 0.1-1mdv2008.1
+ Revision: 115008
- use %%mkrel
- import dssh


* Wed May 26 2004 Aginies <aginies@n2.mandrakesoft.com> 0.1-1mdk
- first Mandrakesoft release
