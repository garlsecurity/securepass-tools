# For EPEL6
#%if 0%{?rhel} && 0%{?rhel} <= 7 
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
#%endif

Name:           python-securepass
Version:        0.4.6
Release:        1%{?dist}
Summary:        SecurePass Python tools

%if 0%{?suse_version}
Group: 			System Environment/Libraries
%endif

License:        GPLv2+
URL:            https://github.com/garlsecurity/securepass-tools
Source0:        https://github.com/garlsecurity/securepass-tools/archive/v%{version}/securepass-tools-v%{version}.tar.gz  
BuildRequires:  python-pycurl

%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  python2-devel
BuildArch:      noarch
%endif

%if 0%{?suse_version}
BuildRequires:  python-devel
%endif

# SLES11 don't want noarch

%if 0%{?suse_version} <= 1110
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%else
BuildArch:      noarch
%endif

%if 0%{?rhel} <= 6 || 0%{?suse_version}
BuildRequires:  python-argparse
%endif

Requires:       python-pycurl
%if 0%{?rhel} <= 6 || 0%{?suse_version}
Requires:       python-argparse
%endif

%description
The tools and python libraries for accessing SecurePass platform.

It uses the SecurePass public APIs.

# Subpackage tools (the bin)
%package -n securepass-tools
Summary:    SecurePass Tools 
Requires:   python-securepass

%if 0%{?suse_version}
Group:      System Environment/Libraries
%endif

%description -n securepass-tools
The official tools for accessing SecurePass platform.

It uses the SecurePass public APIs.

%prep
%setup -qn securepass-tools-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --prefix=%{_prefix} --root="%{buildroot}"


%files 
%defattr(-,root,root,-)
%{!?_licensedir:%global license %doc}
%{python2_sitelib}/*
%doc README.txt README.md 

%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
%license LICENSE
%endif 

%if 0%{?suse_version}
%doc LICENSE
%endif

%files -n securepass-tools
%{!?_licensedir:%global license %doc} 
%defattr(-,root,root,-)
%{_bindir}/*
%doc README.txt README.md securepass.conf.example contrib/extract_ssh_key.sh 

%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
%license LICENSE
%endif

%if 0%{?suse_version}
%doc LICENSE
%endif


%changelog
* Wed Feb 16 2016  Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4.4-2
- Fixes for SLES 11

* Tue Feb 16 2016  Giuseppe Paterno' <gpaterno@gpaterno.com> 0.4.4-1
- Reflect changes to the upstream package

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
