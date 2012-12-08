Summary:	Driver for the Samsung ML-85G and QL-85G winprinters
Name:		ml85p
Version:	0.2.0
Release:	%mkrel 12
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
# "ml85p" talks directly to the parallel port I/O 0x378, not to /dev/lp0
# Therefore SUID "root" is needed. Program only executable by "lp" & "root"
# (group-executable).
%attr(4750,root,sys) %{_bindir}/ml85p


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-10mdv2011.0
+ Revision: 666459
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-9mdv2011.0
+ Revision: 606651
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-8mdv2010.1
+ Revision: 520179
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2.0-7mdv2010.0
+ Revision: 426154
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-6mdv2009.1
+ Revision: 321039
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-5mdv2009.0
+ Revision: 223296
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 21 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.2.0-4mdv2008.1
+ Revision: 110964
- Fixing deps again. Should conflict with printer-utils and printer-filters <=
  2007, and not just = 2007. Closes: #35656

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdv2008.0
+ Revision: 75346
- fix deps (pixel)

* Thu Aug 16 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.2.0-2mdv2008.0
+ Revision: 64510
- Fix build (build_fix patch). cli/sti are not normal, and not even used
  anymore on kernel, and may be this ml85p should not be user space...
  anyway I fixed the build, but don't know if ml85p still works.

  + Oden Eriksson <oeriksson@mandriva.com>
    - use the new System/Printing RPM GROUP
    - Import ml85p



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdv2008.0
- initial Mandriva package
