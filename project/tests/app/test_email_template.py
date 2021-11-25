from django.core import mail
from django.test import TestCase


class EmailTest(TestCase):
    def test_send_email_template(self):
        # Send message.
        mail.send_mail(
            'Test Subject', 'Test message',
            'test@example.com', ['user@example.com'],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Test Subject')

        # Verify that the message body is correct.
        self.assertEqual(mail.outbox[0].body, 'Test message')
