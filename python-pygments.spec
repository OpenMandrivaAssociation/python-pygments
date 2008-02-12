%define shortname Pygments
Name:           python-pygments
Version:        0.9
Release:        %mkrel 1
Summary:        Pygments is a syntax highlighting package written in Python
Group:          Development/Python
License:        BSD
URL:            http://pygments.org/
Source0:        http://pypi.python.org/packages/source/P/%{shortname}/%{shortname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  python-devel

%description
Pygments is a syntax highlighting package written in Python.

It is a generic syntax highlighter for general use in all kinds of software
such as forum systems, wikis or other applications that need to prettify source
code.  Highlights are:

  * a wide range of common languages and markup formats is supported
  * special attention is paid to details, increasing quality by a fair amount
  * support for new languages and formats are added easily
  * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI
    sequences
  * it is usable as a command-line tool and as a library
  * ... and it highlights even Brainfuck!

%prep
%setup -q -n %{shortname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/pygmentize
%{py_platsitedir}/*
