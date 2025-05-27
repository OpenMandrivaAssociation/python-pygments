%define tarname Pygments
%define module	pygments

Summary:	Syntax highlighting package written in Python
Name:		python-%{module}
Version:	2.19.1
Release:	1
Group:		Development/Python
License:	BSD
Url:		https://pygments.org/
Source0:	https://github.com/pygments/pygments/archive/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(hatchling)
BuildSystem:	python

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

%install -a
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 doc/pygmentize.1 %{buildroot}%{_mandir}/man1

%files
%doc AUTHORS CHANGES LICENSE
%{_bindir}/pygmentize
%{py_sitedir}/pygments
%{py_sitedir}/pygments*.*-info
%{_mandir}/man1/pygmentize.*
