cd SPECS
rpmbuild -ba ERPXE.spec
cd ..
cd SRPMS
rpm -ivh ERPXE*.rpm
cd ..
cd RPMS
cd i386