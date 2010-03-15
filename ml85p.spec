Summary:	Driver for the Samsung ML-85G and QL-85G winprinters
Name:		ml85p
Version:	0.2.0
Release:	%mkrel 8
License:	GPL
Group:		System/Printing
URL:		http://www.pragana.net/gdiprinters.html
Source0:	http://www.pragana.net/%{name}-%{version}.tar.gz
Patch:  	ml85p-0.2.0-build_fix.patch
Conflicts:	printer-utils <= 2007
Conflicts:	printer-filters <= 2007
Exclusivearch:	%{ix86} x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Driver for the Samsung ML-85G and QL-85G winprinters.

%prep

%setup -q
%patch -p1 -b .build_fix

# fix attribs
chmod 644 *

# path hack
perl -pi -e "s|/usr/local/bin|%{_bindir}|g" *

%build
rm -f ml85p
%{__cc} %{optflags} %{ldflags} -o ml85p ml85p.c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 ml85p %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING NEWS README THANKS ml85-print ml85-test printcap
%attr(0755,root,root) %{_bindir}/*
# "ml85p" talks directly to the parallel port I/O 0x378, not to /dev/lp0
# Therefore SUID "root" is needed. Program only executable by "lp" & "root"
# (group-executable).
%attr(4750,root,sys) %{_bindir}/ml85p
