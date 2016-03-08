from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from core.tests.url_utils import version_ns, version_url
from .. import views


class UserUrlsTest(TestCase):
    def test_account_user(self):
        self.assertEqual(
            reverse(version_ns('accounts:user')),
            version_url('/account/')
        )

        resolved = resolve(version_url('/account/'))
        self.assertEqual(resolved.func.__name__, views.AccountUser.__name__)

    def test_account_register(self):
        self.assertEqual(
            reverse(version_ns('accounts:register')),
            version_url('/account/register/')
        )

        resolved = resolve(version_url('/account/register/'))
        self.assertEqual(resolved.func.__name__, views.AccountRegister.__name__)

    def test_account_login(self):
        self.assertEqual(
            reverse(version_ns('accounts:login')),
            version_url('/account/login/')
        )

        resolved = resolve(version_url('/account/login/'))
        self.assertEqual(resolved.func.__name__, views.AccountLogin.__name__)

    def test_account_activate(self):
        self.assertEqual(
            reverse(version_ns('accounts:activate')),
            version_url('/account/activate/')
        )

        resolved = resolve(version_url('/account/activate/'))
        self.assertEqual(resolved.func.__name__, views.AccountVerify.__name__)

    def test_password_reset(self):
        self.assertEqual(
            reverse(version_ns('accounts:password_reset')),
            version_url('/account/password/reset/')
        )

        resolved = resolve(version_url('/account/password/reset/'))
        self.assertEqual(resolved.func.__name__, views.PasswordReset.__name__)