%define tarname Pygments
%define version	1.2.1
%define rel	1

Name:           python-pygments
Version:        %version
Release:        %mkrel %rel
Summary:        Syntax highlighting package written in Python
Group:          Development/Python
License:        BSD
URL:            http://pygments.org/
Source0:        http://pypi.python.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%py_requires -d
BuildRequires:	python-setuptools
BuildArch: 	noarch

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
%{__python} setup.py install --skip-build --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root,-)
%doc AUTHORS CHANGES LICENSE TODO docs/build/*.html
%dir %py_puresitedir/pygments/
