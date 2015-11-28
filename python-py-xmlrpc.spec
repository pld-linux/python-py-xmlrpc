Summary:	XMLRPC Python Library
Summary(pl.UTF-8):	Biblioteka XMLRPC dla Pythona
Name:		python-py-xmlrpc
Version:	0.8.8.3
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/py-xmlrpc/py-xmlrpc-%{version}.tar.gz
# Source0-md5:	d2aa74615aa9cf23413975a68613ffc1
URL:		http://sourceforge.net/projects/py-xmlrpc/
BuildRequires:	python
BuildRequires:	python-modules
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An extremely fast implementation of the XMLRPC spec for Python
(written in C). It supports both blocking and non-blocking clients
and servers on Windows and POSIX platforms. Version 0.8.1 is 100%
compliant with the www.xmlrpc.com validator.

%description -l pl.UTF-8
Bardzo szybka implementacja specyfikacji XMLRPC dla Pythona (napisana
w C). Wspiera zarówno blokujących jak i nieblokujących klientów i
serwery na platformach Windows i POSIX. Wersja 0.8.1 jest w 100%
zgodna z walidatorem www.xmlrpc.com .

%prep
%setup -q -n py-xmlrpc-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%{_examplesdir}/%{name}-%{version}
