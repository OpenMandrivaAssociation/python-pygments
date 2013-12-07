%define tarname Pygments
%define module	pygments

Summary:	Syntax highlighting package written in Python
Name:		python-%{module}
Version:	1.6
Release:	2
Group:		Development/Python
License:	BSD
Url:		http://pygments.org/
Source0:	http://pypi.python.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d
Requires:	python-pkg-resources

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
%setup -qn %{tarname}-%{version}

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --skip-build --root=%{buildroot}
mv docs/build html

mkdir -p %{buildroot}%{_mandir}/man1
sed -i 's/\/usr\/share\/doc\/python-pygments\//\/usr\/share\/doc\/python-pygments\/html\//' docs/pygmentize.1
install -m 644 docs/pygmentize.1 %{buildroot}%{_mandir}/man1

%files
%doc AUTHORS CHANGES LICENSE TODO html/
%{_bindir}/pygmentize
%{py_sitedir}/pygments/*
%{py_sitedir}/Pygments-*
%{_mandir}/man1/pygmentize.*

