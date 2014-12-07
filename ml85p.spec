Summary:	Driver for the Samsung ML-85G and QL-85G winprinters
Name:		ml85p
Version:	0.2.0
Release:	19
License:	GPLv2
Group:		System/Printing
Url:		http://www.pragana.net/gdiprinters.html
Source0:	http://www.pragana.net/%{name}-%{version}.tar.gz
Patch0:		ml85p-0.2.0-build_fix.patch
Exclusivearch:	%{ix86} x86_64

%description
Driver for the Samsung ML-85G and QL-85G winprinters.

%prep

%setup -q
%apply_patches

# fix attribs
chmod 644 *

# path hack
sed -i -e "s|/usr/local/bin|%{_bindir}|g" *

%build
rm -f ml85p
%{__cc} %{optflags} %{ldflags} -o ml85p ml85p.c

%install
install -d %{buildroot}%{_bindir}
install -m0755 ml85p %{buildroot}%{_bindir}/

%files
%doc COPYING NEWS README THANKS ml85-print ml85-test printcap
# "ml85p" talks directly to the parallel port I/O 0x378, not to /dev/lp0
# Therefore SUID "root" is needed. Program only executable by "lp" & "root"
# (group-executable).
%attr(4750,root,sys) %{_bindir}/ml85p

