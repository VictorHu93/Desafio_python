from django.core.management import call_command
from django.test import TestCase

class MigrationTestCase(TestCase):
    def test_makemigrations(self):
        try:
            call_command('makemigrations', check=True)
        except Exception as e:
            self.fail(f"Erro ao rodar makemigrations: {e}")

    def test_migrate(self):
        try:
            call_command('migrate', check=True)
        except Exception as e:
            self.fail(f"Erro ao rodar migrate: {e}")
