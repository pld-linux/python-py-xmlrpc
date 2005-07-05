Summary:	XMLRPC Python Library
#Summary(pl):	
Name:		python-py-xmlrpc
Version:	0.8.8.3
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/py-xmlrpc/py-xmlrpc-%{version}.tar.gz
# Source0-md5:	d2aa74615aa9cf23413975a68613ffc1
URL:		http://sourceforge.net/projects/py-xmlrpc
BuildRequires:	python
BuildRequires:	python-modules
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An extremely fast implementation of the xmlrpc spec for Python
(written in C). It supports both blocking and non-blocking clients
and servers on Windows and POSIX platforms. Version 0.8.1 is 100%
compliant with the www.xmlrpc.com validator.

#%description -l pl

%prep
%setup -q -n py-xmlrpc-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

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
