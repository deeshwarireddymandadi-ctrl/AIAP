# ...existing code...

def greet_user(name: str, gender: str | None = None, preferred_title: str | None = None) -> str:
    """
    Return a greeting that uses a respectful title when requested.
    - gender can be 'male', 'female', 'nonbinary', 'neutral', 'other', or None/empty.
    - preferred_title, if provided, overrides the gender-based mapping.
    """
    # normalize inputs
    g = (gender or "").strip().lower()
    if preferred_title:
        title = preferred_title.strip()
    else:
        mapping = {
            "male": "Mr.",
            "female": "Ms.",
            "nonbinary": "Mx.",
            "non-binary": "Mx.",
            "nb": "Mx.",
            "neutral": "Mx.",
        }
        title = mapping.get(g, "")  # empty string means no title

    if title:
        return f"Hello, {title} {name}! Welcome."
    else:
        return f"Hello, {name}! Welcome."

if __name__ == "__main__":
    name = input("Enter name: ").strip() or "Guest"
    gender = input("Enter gender (male/female/nonbinary/neutral/other) [leave blank for none]: ").strip()
    preferred_title = None

    if gender.lower() in ("other", "custom"):
        preferred_title = input("Enter preferred title (e.g. Mx., Dr., Prof., none): ").strip()
        if preferred_title.lower() in ("none", ""):
            preferred_title = None
    elif not gender:
        choose = input("Would you like to provide a title? (y/N): ").strip().lower()
        if choose == "y":
            preferred_title = input("Enter preferred title (e.g. Mx., Dr., Prof.): ").strip()
            if preferred_title.lower() in ("none", ""):
                preferred_title = None

    print(greet_user(name, gender, preferred_title))
# ...existing code...