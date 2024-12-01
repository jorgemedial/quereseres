#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""

import os
import sys

def main():
    """Main entry point for Django administrative tasks."""
    if os.environ.get('DEBUGGER_SCRIPT', 'False') == 'True' and os.environ.get('RUN_MAIN', None):
        import debugpy
        port = 5678
        debugpy.listen(('0.0.0.0', port))
        print(f"Debugpy is listening on port {port}")
        debugpy.wait_for_client()
        print("Debug working")

    # Set default Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quereseres.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it is installed and available on your "
            "PYTHONPATH environment variable. Did you forget to activate a virtual environment?"
        ) from exc

    # Execute the command-line utility
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
