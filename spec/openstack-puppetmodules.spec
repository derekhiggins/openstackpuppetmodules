
%global git_revno %GIT_REVNO%

Name:           openstack-puppetmodules
Version:        2012.2.1
#Release:       1%{?dist}
Release:        1dev%{git_revno}%{?dist}
Summary:        Puppet modules for Openstack

Group:          Applications/System
License:        ASL 2.0
URL:            https://github.com/derekhiggins/openstackpuppetmodules
#Source0:        https://github.com/downloads/derekhiggins/openstackpuppetmodules/openstackpuppetmodules-%{version}.tar.gz
Source0:        https://github.com/downloads/derekhiggins/openstackpuppetmodules/openstackpuppetmodules-%{version}dev%{git_revno}.tar.gz

BuildArch:      noarch

%description
A collection of puppet modules suitable for installing openstack

%prep
#%setup -n openstackpuppetmodules-%{version}
%setup -n openstackpuppetmodules-%{version}dev%{git_revno}

# Sanitizing a lot of the files in the puppet modules, they come from seperate upstream projects
find modules \( -name .fixtures.yml -o -name .gemfile -o -name ".travis.yml" -o -name .rspec \) -exec rm {} \;
find modules \( -name "*.py" -o -name "*.rb" -o -name "*.sh" -o -name "*.pl" \) -exec sed -i '/^#!/{d;q}' {} \; -exec chmod -x {} \;
find modules -name site.pp -size 0 -exec rm {} \;

%build

%install

rm -rf  %{buildroot}
mkdir -p %{buildroot}/etc/puppet/modules
mv modules/* %{buildroot}%{_sysconfdir}/puppet/modules

%files
%doc LICENSE README
%{_sysconfdir}/puppet/modules

%changelog
* Tue Dec 04 2012 Derek Higgins <derekh@redhat.com> 
- Initial version

