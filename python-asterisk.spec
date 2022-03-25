# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	asterisk
Summary:	A Python Interface to Asterisk
Name:		python-%{module}
Version:	0.4.9
Release:	6
License:	PSF
Group:		Libraries/Python
Source0:	https://github.com/rdegges/pyst2/archive/%{version}.tar.gz
# Source0-md5:	f9a99a43008ca9b6d5ef6ff6e1b60712
URL:		https://pypi.python.org/pypi/pyst2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyst2 consists of a set of interfaces and libraries to allow
programming of Asterisk from python. The library currently supports
AGI, AMI, and the parsing of Asterisk configuration files. The library
also includes debugging facilities for AGI.

%package -n python3-%{module}
Summary:	A Python Interface to Asterisk
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
pyst2 consists of a set of interfaces and libraries to allow
programming of Asterisk from python. The library currently supports
AGI, AMI, and the parsing of Asterisk configuration files. The library
also includes debugging facilities for AGI.

%prep
%setup -q -n pyst2-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/pyst2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/pyst2-%{version}-py*.egg-info
%endif
