# splunkbeta-20090504-58411-Darwin-universal-manifest

for i in *-manifest; do
	echo $i
	S_BRANCH=$(echo $i |awk -F- '{print $1}')
	S_OS=$(echo $i | awk -F- '{print $4}')
	S_ARCH=$(echo $i | awk -F- '{print $5}')
done
if [ "$S_BRANCH" -a "$S_OS" -a "$S_ARCH" ]; then
	if [ "$S_BRANCH" == "splunkbeta" ]; then
		S_REAL_BRANCH="madonna-beta"
		# TODO: add support for non-beta (3.2, etc)
	else
		S_REAL_BRANCH="3.2"
	fi
	BUILD=$(python2.6 /Users/galbrecht/src/splunk/current/test/mambo/bin/splunkPlatform.py -B $S_REAL_BRANCH -o $S_OS -a $S_ARCH)
	if [ "$BUILD" ]; then
		curl -O $BUILD
	fi
	BUILD_FILE="$(echo $BUILD|awk -F/ '{print $NF}')"
	if [ -f "$BUILD_FILE" ]; then
		echo $BUILD_FILE
		tar --strip-components 1  -zxf $BUILD_FILE
	fi
fi
