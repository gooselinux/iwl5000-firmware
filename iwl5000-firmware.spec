%define iwl5000_v1         5.4.A.11
%define iwl5000_v2         8.24.2.12
%define iwl5000_list       %{iwl5000_v1} %{iwl5000_v2}

Name:           iwl5000-firmware
Version:        %{iwl5000_v2}
Release:        3%{?dist}
Summary:        Firmware for Intel® PRO/Wireless 5000 A/G/N network adaptors

Group:          System Environment/Kernel
License:        Redistributable, no modification permitted
URL:            http://intellinuxwireless.org/
Source0:        http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-%{iwl5000_v1}.tar.gz
Source1:        http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-%{iwl5000_v2}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch


%description
This package contains the firmware required by the iwl5000 driver for Linux.
Usage of the firmware is subject to the terms and conditions contained
inside the provided LICENSE file. Please read it carefully.

%prep
%setup -c -q
%setup -c -q -D -T -a 1

pushd iwlwifi-5000-ucode-%{version}
# Change encoding
sed -i 's/\r//'  LICENSE.iwlwifi-5000-ucode README.iwlwifi-5000-ucode
# Rename docs
mv LICENSE.iwlwifi-5000-ucode ../LICENSE
mv README.iwlwifi-5000-ucode ../README
# Preserve timestamp
touch -r *.ucode ../LICENSE ../README
popd


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
for f in %{iwl5000_list} ; do
pushd iwlwifi-5000-ucode-$f
install -pm 0644 *.ucode $RPM_BUILD_ROOT/lib/firmware/
popd
done


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README
/lib/firmware/*.ucode

%changelog
* Thu Jan  7 2010 John W. Linville <linville@redhat.com> - 8.24.2.12-3
- Add dist tag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.24.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 John W. Linville <linville@redhat.com> - 8.24.2.12-1
- Add v2 firmware

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.A.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  5 2008 kwizart < kwizart at gmail.com > - 5.4.A.11-3
- Remove ppc/ppc64 from ExcludedArches

* Mon Jul 28 2008 kwizart < kwizart at gmail.com > - 5.4.A.11-2
- Add LICENSE.iwlwifi-5000-ucode README.iwlwifi-5000-ucode as %%doc

* Fri Jul 11 2008 kwizart < kwizart at gmail.com > - 5.4.A.11-1
- Initial package
