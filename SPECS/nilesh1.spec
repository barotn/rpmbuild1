Name: nilesh
Version: 1
Release:        1%{?dist}
Summary: Test rpm to copy files

Group: My Invention
License: GPL
#URL:   
Source0: nilesh-1.tar.gz
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
This is the first rpm package

%prep
%setup -q

%build
#No build

%install
install -m 0755 -d $RPM_BUILD_ROOT/home/nilesh/opt/nilesh-1
install -m 0755 myscript.sh $RPM_BUILD_ROOT/home/nilesh/opt/nilesh-1/myscript.sh
install -m 0644 install.log $RPM_BUILD_ROOT/home/nilesh/opt/nilesh-1/install.log
install -m 0644 install.log.syslog $RPM_BUILD_ROOT/home/nilesh/opt/nilesh-1/install.log.syslog

%clean
rm -rf %{buildroot}

%post
echo " "
echo "This will display after rpm installs the package!"

%files
#%defattr(-,root,root,-)
#%doc
%dir /home/nilesh/opt/nilesh-1
/home/nilesh/opt/nilesh-1/myscript.sh
/home/nilesh/opt/nilesh-1/install.log
/home/nilesh/opt/nilesh-1/install.log.syslog

%changelog
