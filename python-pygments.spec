%define tarname Pygments
%define module	pygments

Summary:	Syntax highlighting package written in Python
Name:		python-%{module}
Version:	2.14.0
Release:	2
Group:		Development/Python
License:	BSD
Url:		http://pygments.org/
Source0:	https://github.com/pygments/pygments/archive/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:  pkgconfig(python3)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(wheel)

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
%autosetup -p1 -n pygments-%{version}

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 doc/pygmentize.1 %{buildroot}%{_mandir}/man1

%files
%doc AUTHORS CHANGES LICENSE
%{_bindir}/pygmentize
%{py_sitedir}/pygments
%{py_sitedir}/Pygments-*
%{_mandir}/man1/pygmentize.*
