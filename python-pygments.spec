%define tarname Pygments
%define version	1.3.1

Name:           python-pygments
Version:        1.3.1
Release:        %mkrel 3
Summary:        Syntax highlighting package written in Python
Group:          Development/Python
License:        BSD
URL:            http://pygments.org/
Source0:        http://pypi.python.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
%py_requires -d
Requires:       python-pkg-resources
BuildRequires:	python-setuptools
BuildArch: 	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --skip-build --root=%{buildroot} --record=FILELIST
mv docs/build html

%__mkdir -p %{buildroot}%{_mandir}/man1
%__sed -i 's/\/usr\/share\/doc\/python-pygments\//\/usr\/share\/doc\/python-pygments\/html\//' docs/pygmentize.1
%__install -m 644 docs/pygmentize.1 %{buildroot}%{_mandir}/man1

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root,-)
%doc AUTHORS CHANGES LICENSE TODO html/
%dir %py_puresitedir/pygments/
%_mandir/man1/pygmentize.*
