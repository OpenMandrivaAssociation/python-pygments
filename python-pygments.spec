%define tarname Pygments
%define module	pygments

%bcond_without python2

Summary:	Syntax highlighting package written in Python
Name:		python-%{module}
Version:	2.7.4
Release:	1
Group:		Development/Python
License:	BSD
Url:		http://pygments.org/
Source0:	https://github.com/pygments/pygments/archive/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:  pkgconfig(python3)
%if %{with python2}
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
%endif

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

%package -n python2-%{module}
Summary:	Pygments syntax highlighter for Python 2.x
Group:		Development/Python
Requires:	python2-pkg-resources

%description -n python2-%{module}
Pygments syntax highlighter for Python 2.x

%prep
%autosetup -p1 -n pygments-%{version}
%if %{with python2}
mkdir python2
cp -a `ls |grep -v python2` python2/
%endif

%build
%{__python} setup.py build

%if %{with python2}
cd python2
python2 setup.py build
%endif

%install
# python2 first, so the default build can overwrite files in %_bindir
%if %{with python2}
cd python2
PYTHONDONTWRITEBYTECODE=yes python2 setup.py install --skip-build --root=%{buildroot}
cd ..
%endif

PYTHONDONTWRITEBYTECODE=yes %{__python} setup.py install --skip-build --root=%{buildroot}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 doc/pygmentize.1 %{buildroot}%{_mandir}/man1

%files
%doc AUTHORS CHANGES LICENSE
%{_bindir}/pygmentize
%{py_sitedir}/pygments
%{py_sitedir}/Pygments-*
%{_mandir}/man1/pygmentize.*

%if %{with python2}
%files -n python2-pygments
%{py2_puresitedir}/pygments
%{py2_puresitedir}/Pygments-*
%endif
