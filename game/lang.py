# Add this at the beginning of your script.rpy file or in a separate Python file

init -10 python:
    # Import locale module to detect system language
    import locale
    
    # Try to get the user's system locale
    try:
        system_lang, _ = locale.getdefaultlocale()
        system_lang = system_lang.lower() if system_lang else None
    except:
        system_lang = None
    
    # Set default language based on system locale
    if system_lang:
        if system_lang.startswith('ru'):
            # Set to Russian (None in your case since Russian is the default)
            config.language = None
        elif system_lang.startswith('en'):
            # Set to English
            config.language = "english"
        # You can add more languages here if needed