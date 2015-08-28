Name:           python-securepass
Version:        0.4.1
Release:        1%{?dist}
Summary:        SecurePass Python tools

Group:          Development/Libraries
License:        GPLv2+
URL:            https://github.com/garlsecurity/securepass-tools
Source0:      	https://github.com/garlsecurity/securepass-tools/archive/%{version}/securepass-tools-v%{version}.tar.gz  

BuildArch: 	noarch
BuildRequires:  python-pycurl
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:       python-pycurl

%description
The tools and libraries for accessing SecurePass platform.

Uses the SecurePass public APIs to manage.

%prep
%setup -qn securepass-tools-%{version}


%build
%{__python} setup.py build


%install
[ "%{buildroot}" != "/" ] && rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"


%clean
[ "%{buildroot}" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/*
%{_usr}/bin/*
%doc README.txt README.md securepass.conf.example contrib/extract_ssh_key.sh 

%if 0%{?rhel} <= 6
   %doc LICENSE 
%else 
   %license LICENSE
%endif

%changelog
* Fri Aug 28 2015 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4.1-1
- Added SSH key helper

* Tue Aug 25 2015 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4-1
- Support for extended attributes in users and realms
- Support for privacy bit in the APIs

* Fri Nov 14 2014 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.3.6-1 
- Initial RPM spec for securepass-tools
