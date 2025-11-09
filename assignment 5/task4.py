# ...existing code...

from typing import Dict
import csv

EDU_SCORES = {
    "highschool": 40,
    "associate": 55,
    "bachelor": 70,
    "master": 85,
    "phd": 95
}

DEFAULT_WEIGHTS: Dict[str, float] = {
    "experience": 0.25,     # years -> capped/scaled
    "education": 0.20,      # mapped from EDU_SCORES
    "skills": 0.30,         # skill match percentage (0-100)
    "certifications": 0.05, # count -> small contribution
    "interview": 0.20       # interview score (0-10)
}

def normalize_weights(weights: Dict[str, float]) -> Dict[str, float]:
    total = sum(weights.values())
    if total == 0:
        return DEFAULT_WEIGHTS.copy()
    return {k: v / total for k, v in weights.items()}

def score_applicant(features: Dict[str, float], weights: Dict[str, float]) -> float:
    """
    Compute a 0-100 score using weighted sum of sub-scores.
    features keys:
      - experience: years (float)
      - education: one of EDU_SCORES keys (str)
      - skills: skill match percent (0-100)
      - certifications: integer count
      - interview: interview rating (0-10)
    """
    w = normalize_weights(weights)
    # map features to 0-100 sub-scores
    exp_score = min(features.get("experience", 0) / 10 * 100, 100)  # 10+ years -> 100
    edu_key = str(features.get("education", "")).lower()
    edu_score = EDU_SCORES.get(edu_key, 50)  # unknown education -> neutral 50
    skills_score = max(0.0, min(features.get("skills", 0), 100))
    cert_score = min(features.get("certifications", 0) * 10, 100)   # each cert ~10 points
    interview_score = min(max(features.get("interview", 0) * 10, 0), 100)  # 0-10 -> 0-100

    total = (
        exp_score * w["experience"] +
        edu_score * w["education"] +
        skills_score * w["skills"] +
        cert_score * w["certifications"] +
        interview_score * w["interview"]
    )
    return round(total, 2)

def rating_from_score(score: float) -> str:
    if score >= 85:
        return "Strong"
    if score >= 70:
        return "Good"
    if score >= 50:
        return "Consider"
    return "Weak"

def prompt_float(prompt: str, default: float = 0.0) -> float:
    s = input(f"{prompt} [{default}]: ").strip()
    if not s:
        return default
    try:
        return float(s)
    except ValueError:
        print("Invalid number, using default.")
        return default

def main():
    print("Applicant scoring system (no protected attributes used).")
    print("Default weights:", DEFAULT_WEIGHTS)
    use_custom = input("Customize weights? (y/N): ").strip().lower() == "y"
    weights = DEFAULT_WEIGHTS.copy()
    if use_custom:
        for k in list(DEFAULT_WEIGHTS.keys()):
            val = prompt_float(f"Weight for {k} (current {weights[k]}):", weights[k])
            weights[k] = max(0.0, val)
        weights = normalize_weights(weights)

    n = int(prompt_float("Number of applicants to score", 1))
    results = []
    for i in range(1, n + 1):
        print(f"\nApplicant #{i}:")
        name = input("  Name: ").strip() or f"Applicant_{i}"
        experience = prompt_float("  Years of experience", 0)
        education = input("  Education (highschool/associate/bachelor/master/phd): ").strip().lower()
        skills = prompt_float("  Skill match percent (0-100)", 50)
        certifications = int(prompt_float("  Number of certifications", 0))
        interview = prompt_float("  Interview rating (0-10)", 5)

        features = {
            "experience": experience,
            "education": education,
            "skills": skills,
            "certifications": certifications,
            "interview": interview
        }
        score = score_applicant(features, weights)
        rating = rating_from_score(score)
        print(f"  Score: {score} / 100   Rating: {rating}")
        results.append({"name": name, "score": score, "rating": rating})

    save = input("\nSave results to CSV? (y/N): ").strip().lower() == "y"
    if save:
        path = input("Enter output CSV path [applicant_scores.csv]: ").strip() or "applicant_scores.csv"
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "score", "rating"])
            writer.writeheader()
            writer.writerows(results)
        print(f"Saved to {path}")

if __name__ == "__main__":
    main()
# ...existing code...