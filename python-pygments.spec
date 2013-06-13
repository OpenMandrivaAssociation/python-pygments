%define tarname Pygments
%define module	pygments

Name:           python-%{module}
Version:        1.6
Release:        1
Summary:        Syntax highlighting package written in Python
Group:          Development/Python
License:        BSD
URL:            http://pygments.org/
Source0:        http://pypi.python.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
%py_requires -d
Requires:       python-pkg-resources
BuildRequires:	python-setuptools
BuildArch:		noarch

%description
Pygments is a syntax highlighting package written in Python.  It is a
generic syntax highlighter for general use in all kinds of software
such as forum systems, wikis or other applications that need to
prettify source code.  Highlights are:

* a wide range of common languages and markup formats is supported
* special attention is paid to details, increasing quality by a fair amount
* support for new languages and formats are added easily
* a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI
  sequences
* it is usable as a command-line tool and as a library
* ... and it highlights even Brainf*ck!

%prep
%setup -q -n %{tarname}-%{version}

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --skip-build --root=%{buildroot}
mv docs/build html

%__mkdir -p %{buildroot}%{_mandir}/man1
%__sed -i 's/\/usr\/share\/doc\/python-pygments\//\/usr\/share\/doc\/python-pygments\/html\//' docs/pygmentize.1
%__install -m 644 docs/pygmentize.1 %{buildroot}%{_mandir}/man1

%files
%doc AUTHORS CHANGES LICENSE TODO html/
%_bindir/pygmentize
%py_sitedir/pygments/*
%py_sitedir/Pygments-*
%_mandir/man1/pygmentize.*



%changelog
* Sun Mar 11 2012 Lev Givon <lev@mandriva.org> 1.5-1mdv2012.0
+ Revision: 784062
- Update to 1.5.

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-2
+ Revision: 668025
- mass rebuild

* Tue Jan 18 2011 Lev Givon <lev@mandriva.org> 1.4-1
+ Revision: 631631
- Update to 1.4.

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.3.1-4mdv2011.0
+ Revision: 589997
- rebuild for python 2.7

* Mon May 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-3mdv2010.1
+ Revision: 541787
- add python-pkg-resources dependency

* Thu Apr 01 2010 Lev Givon <lev@mandriva.org> 1.3.1-2mdv2010.1
+ Revision: 530751
- Fix file inclusion.
- Update to 1.3.1.

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.2-1mdv2010.1
+ Revision: 488810
- update to new version 1.2.2

* Sun Jan 03 2010 Frederik Himpe <fhimpe@mandriva.org> 1.2.1-1mdv2010.1
+ Revision: 485874
- update to new version 1.2.1

* Mon Sep 14 2009 Lev Givon <lev@mandriva.org> 1.1-1mdv2010.0
+ Revision: 441076
- Update to 1.1.

* Thu May 07 2009 Michael Scherer <misc@mandriva.org> 1.0-2mdv2010.0
+ Revision: 372783
- fix missing directory, close bug #50659
- remove generation of .pyo

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 1.0-1mdv2009.1
+ Revision: 324274
- New upstream release

* Mon Dec 29 2008 Funda Wang <fwang@mandriva.org> 0.11.1-2mdv2009.1
+ Revision: 320911
- add BR
- rebuild for new python

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11.1-1mdv2009.1
+ Revision: 305851
- update to new version 0.11.1

* Tue Aug 19 2008 Lev Givon <lev@mandriva.org> 0.10-1mdv2009.0
+ Revision: 274019
- Update to 0.10.

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.9-5mdv2009.0
+ Revision: 259771
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9-4mdv2009.0
+ Revision: 247598
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9-2mdv2008.1
+ Revision: 171064
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Oct 21 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9-1mdv2008.1
+ Revision: 100733
- import python-pygments


