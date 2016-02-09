all: repo org.gnome.Sdk.json
	rm -rf sdk
	xdg-app-builder --ccache --require-changes --repo=repo --subject="build of org.gnome.Sdk, `date`" ${EXPORT_ARGS} sdk org.gnome.Sdk.json

repo:
	ostree  init --mode=archive-z2 --repo=repo
