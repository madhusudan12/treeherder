import pytest

from treeherder.middleware import CustomWhiteNoise

URLS_IMMUTABLE = [
    # Assets generated by Neutrino.
    '/assets/2.379789df.css',
    '/assets/dancing_cat.fa5552a5.gif',
    '/assets/fontawesome-webfont.af7ae505.woff2',
    '/assets/fontawesome-webfont.fee66e71.woff',
    '/assets/index.1d85033a.js',
    '/assets/index.1d85033a.js.map',
    '/assets/perf.d7fea1e4.css',
    '/assets/perf.d7fea1e4.css.map',
    '/assets/treeherder-logo.3df97cff.png',
]

URLS_NOT_IMMUTABLE = [
    '/',
    '/contribute.json',
    '/perf.html',
    '/revision.txt',
    '/tree_open.png',
    '/docs/schema.js',
    # The unhashed Neutrino/webpack output if using `yarn build --mode development`.
    '/assets/runtime.js',
    '/assets/vendors~index.js',
    # The unhashed Django static asset originals (used in development).
    '/static/debug_toolbar/assets/toolbar.css',
    '/static/rest_framework/docs/js/jquery.json-view.min.js',
]


@pytest.mark.parametrize('url', URLS_IMMUTABLE)
def test_immutable_file_test_matches(url):
    assert CustomWhiteNoise().immutable_file_test('', url)


@pytest.mark.parametrize('url', URLS_NOT_IMMUTABLE)
def test_immutable_file_test_does_not_match(url):
    assert not CustomWhiteNoise().immutable_file_test('', url)
