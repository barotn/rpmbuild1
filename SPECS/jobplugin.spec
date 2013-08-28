%define installdir      /opt/glassfish/glassfish/lib
%global username        vidispine

Name:           JobPlugin-3.3.6-gbb2cc26-9635.jar
Version:        3.3
Release:        6
Summary:        Glassfish rabbitmq libraries

Group:          Other
License:        Proprietary
URL:            http://glassfish.java.net/
Source0:        JobPlugin-3.3.6-gbb2cc26-9635.jar
BuildRoot:      %{_tmppath}/%{name}-root
BuildArch:      noarch

#BuildRequires:
Requires:       glassfish

%description
Glassfish libraries required to make glassfish work.

%pre

%prep
cp -p %{SOURCE0} .

%build
#No build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{installdir}
%{__install} -m 0644 %{SOURCE0} ${RPM_BUILD_ROOT}%{installdir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%post

%files
%defattr(-,%{username},%{username},-)
%{installdir}

%changelog

* Tue Aug 27 2013 nilesh.barot@itv.com 

- initial rpm for glassfish
