"""
Basic usage example for Logger class

Demonstrates:
- Initial setup
- Different log levels
- File logging
- Error handling
- Dynamic configuration changes
"""

import os
import tempfile
from upd_logger import Logger 

def main():
    # 1. Настройка логирования с очисткой старых логов
    print("=== Basic Setup ===")
    log_dir = "C:\\TestLogFiles"
    success, msg = Logger.setupLogging(
        log_dir=log_dir,
        write_to_file=True,
        max_log_size=1024 * 1024 * 1024,  # 1 MB
        max_log_age_days=1
    )
    
    if not success:
        print(f"Warning: {msg}")
    
    Logger("Application started", "info")

    # 2. Примеры различных уровней логирования
    print("\n=== Log Levels ===")
    Logger("This is an INFO message", "info")
    Logger("This is a WARNING message", "warn")
    Logger("This is a DEBUG message", "debug")
    Logger("This is an ERROR message", "error")
    Logger("This is a CRITICAL message", "crit")

    # 3. Пример обработки ошибок
    print("\n=== Error Handling ===")
    try:
        1 / 0
    except Exception as e:
        Logger(f"Division error occurred: {str(e)}", "error")

    # 4. Динамическое изменение конфигурации
    print("\n=== Reconfiguration ===")
    Logger("Switching to console-only logging...", "info")
    Logger.setupLogging(write_to_file=False)
    Logger("This message goes only to console", "debug")
    
    for i in range(5):
        Logger(f"Test log message {i}", "info")

    # 6. Завершение работы
    Logger("Application shutting down", "info")
    print(f"\nLog files can be found in: {log_dir}")

if __name__ == "__main__":
    main()