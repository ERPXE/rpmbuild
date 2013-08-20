#
# spec file for erpxe
#
Summary: ERPXE is a complete PXE solution featuring a broad range of recovery tools and various OS installations in one box.
Name: tftpboot
Version: 1.1
Release: 8
License: GPL
Group: Applications/System
Source: https://github.com/ERPXE/tftpboot/archive/1.1.tar.gz
URL: http://www.erpxe.org
Vendor: ERPXE
Packager: Etay Cohen-Solal <et@erpxe.com>

%description
ERPXE is a complete PXE solution featuring a broad range 
of recovery tools and various OS installations in one box.
The idea of ERPXE came out of the need for a simple PXE solution 
that would be easy to implement in a short amount of time and money.
Founded in 2007 for internal use, ERPXE was developed in the field 
creating simple solutions for growth in Information Technology.

%prep
%setup
echo Building %{name}-%{version}-%{release}

%build

%install

%clean

%files

%changelog
