Name:           python-securepass
Version:        0.4.3
Release:        2%{?dist}
Summary:        SecurePass Python tools

Group:          Development/Libraries
License:        GPLv2+
URL:            https://github.com/garlsecurity/securepass-tools
Source0:        https://github.com/garlsecurity/securepass-tools/archive/v%{version}/securepass-tools-v%{version}.tar.gz  

BuildArch:      noarch
BuildRequires:  python-pycurl
BuildRequires:  python-argparse
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:       python-pycurl
Requires:       python-argparse

%description
The tools and python libraries for accessing SecurePass platform.

It uses the SecurePass public APIs.

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
%doc README.txt README.md 

%if 0%{?rhel} <= 6
   %doc LICENSE 
%else 
   %license LICENSE
%endif

%package -n securepass-tools
Requires:   python-securepass
Summary:    SecurePass Tools 
Group:      Applications/Internet 

%description -n securepass-tools
The official tools for accessing SecurePass platform.

It uses the SecurePass public APIs.

%files -n securepass-tools
%defattr(-,root,root,-)
%{_usr}/bin/*
%doc README.txt README.md securepass.conf.example contrib/extract_ssh_key.sh 

%if 0%{?rhel} <= 6
   %doc LICENSE 
%else 
   %license LICENSE
%endif

%changelog
* Sun Sep 13 2015 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4.3-2
- Package split 

* Sat Sep 12 2015 Alessio Treglia <alessio@debian.org> 0.4.3-1
- Drop optparse in favor of argparse
- Fix broken import statement in the Django module

* Fri Aug 28 2015 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4.1-1
- Added SSH key helper

* Tue Aug 25 2015 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4-1
- Support for extended attributes in users and realms
- Support for privacy bit in the APIs

* Fri Nov 14 2014 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.3.6-1 
- Initial RPM spec for securepass-tools
