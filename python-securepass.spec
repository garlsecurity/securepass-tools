# For EPEL6
%if 0%{?rhel} && 0%{?rhel} <= 7
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-securepass
Version:        0.4.3
Release:        4%{?dist}
Summary:        SecurePass Python tools

License:        GPLv2+
URL:            https://github.com/garlsecurity/securepass-tools
Source0:        https://github.com/garlsecurity/securepass-tools/archive/v%{version}/securepass-tools-v%{version}.tar.gz  

BuildArch:      noarch
BuildRequires:  python-pycurl
BuildRequires:  python2-devel
%if 0%{?rhel} <= 6
BuildRequires:  python-argparse
%endif

Requires:       python-pycurl
%if 0%{?rhel} <= 6
Requires:       python-argparse
%endif

%description
The tools and python libraries for accessing SecurePass platform.

It uses the SecurePass public APIs.

# Subpackage tools (the bin)
%package -n securepass-tools
Summary:    SecurePass Tools 
Requires:   python-securepass

%description -n securepass-tools
The official tools for accessing SecurePass platform.

It uses the SecurePass public APIs.

%prep
%setup -qn securepass-tools-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root="%{buildroot}"


%files 
%defattr(-,root,root,-)
%{!?_licensedir:%global license %doc}
%{python2_sitelib}/*
%doc README.txt README.md 
%license LICENSE

%files -n securepass-tools
%{!?_licensedir:%global license %doc}
%defattr(-,root,root,-)
%{_bindir}/*
%doc README.txt README.md securepass.conf.example contrib/extract_ssh_key.sh 
%license LICENSE

%changelog
* Wed Sep 16 2015 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4.3-4
- Fixed my own fedora-review errors

* Wed Sep 16 2015 Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4.3-3
- Fixed the SPEC file to honor Fedora polices
- Stick to python2 until the sources are ready

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
