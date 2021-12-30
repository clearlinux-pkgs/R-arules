#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-arules
Version  : 1.7.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/arules_1.7-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/arules_1.7-2.tar.gz
Summary  : Mining Association Rules and Frequent Itemsets
Group    : Development/Tools
License  : GPL-3.0
Requires: R-arules-lib = %{version}-%{release}
Requires: R-generics
BuildRequires : R-generics
BuildRequires : buildreq-R

%description
manipulating and analyzing transaction data and patterns (frequent
    itemsets and association rules). Also provides
    C implementations of the association mining algorithms Apriori and Eclat.

%package lib
Summary: lib components for the R-arules package.
Group: Libraries

%description lib
lib components for the R-arules package.


%prep
%setup -q -c -n arules
cd %{_builddir}/arules

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640889343

%install
export SOURCE_DATE_EPOCH=1640889343
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arules
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arules
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arules
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc arules || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/arules/CITATION
/usr/lib64/R/library/arules/DESCRIPTION
/usr/lib64/R/library/arules/INDEX
/usr/lib64/R/library/arules/Meta/Rd.rds
/usr/lib64/R/library/arules/Meta/data.rds
/usr/lib64/R/library/arules/Meta/features.rds
/usr/lib64/R/library/arules/Meta/hsearch.rds
/usr/lib64/R/library/arules/Meta/links.rds
/usr/lib64/R/library/arules/Meta/nsInfo.rds
/usr/lib64/R/library/arules/Meta/package.rds
/usr/lib64/R/library/arules/Meta/vignette.rds
/usr/lib64/R/library/arules/NAMESPACE
/usr/lib64/R/library/arules/NEWS.md
/usr/lib64/R/library/arules/R/arules
/usr/lib64/R/library/arules/R/arules.rdb
/usr/lib64/R/library/arules/R/arules.rdx
/usr/lib64/R/library/arules/data/Adult.rda
/usr/lib64/R/library/arules/data/AdultUCI.rda
/usr/lib64/R/library/arules/data/Epub.rda
/usr/lib64/R/library/arules/data/Groceries.rda
/usr/lib64/R/library/arules/data/Income.rda
/usr/lib64/R/library/arules/data/IncomeESL.rda
/usr/lib64/R/library/arules/data/Mushroom.rda
/usr/lib64/R/library/arules/data/SunBai.rda
/usr/lib64/R/library/arules/data/datalist
/usr/lib64/R/library/arules/doc/arules.R
/usr/lib64/R/library/arules/doc/arules.Rnw
/usr/lib64/R/library/arules/doc/arules.pdf
/usr/lib64/R/library/arules/doc/index.html
/usr/lib64/R/library/arules/help/AnIndex
/usr/lib64/R/library/arules/help/aliases.rds
/usr/lib64/R/library/arules/help/arules.rdb
/usr/lib64/R/library/arules/help/arules.rdx
/usr/lib64/R/library/arules/help/paths.rds
/usr/lib64/R/library/arules/html/00Index.html
/usr/lib64/R/library/arules/html/R.css
/usr/lib64/R/library/arules/tests/testthat.R
/usr/lib64/R/library/arules/tests/testthat/test-apriori.R
/usr/lib64/R/library/arules/tests/testthat/test-associations.R
/usr/lib64/R/library/arules/tests/testthat/test-concise.R
/usr/lib64/R/library/arules/tests/testthat/test-confint.R
/usr/lib64/R/library/arules/tests/testthat/test-crossTable.R
/usr/lib64/R/library/arules/tests/testthat/test-discretize.R
/usr/lib64/R/library/arules/tests/testthat/test-extract.R
/usr/lib64/R/library/arules/tests/testthat/test-interestMeasures.R
/usr/lib64/R/library/arules/tests/testthat/test-itemCoding.R
/usr/lib64/R/library/arules/tests/testthat/test-itemMatrix.R
/usr/lib64/R/library/arules/tests/testthat/test-matrix.R
/usr/lib64/R/library/arules/tests/testthat/test-missing.R
/usr/lib64/R/library/arules/tests/testthat/test-read_write.R
/usr/lib64/R/library/arules/tests/testthat/test-ruleInduction.R
/usr/lib64/R/library/arules/tests/testthat/test-sets.R
/usr/lib64/R/library/arules/tests/testthat/test-tidLists.R
/usr/lib64/R/library/arules/tests/testthat/test-transactions.R
/usr/lib64/R/library/arules/tests/testthat/test-warm.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/arules/libs/arules.so
/usr/lib64/R/library/arules/libs/arules.so.avx2
/usr/lib64/R/library/arules/libs/arules.so.avx512
