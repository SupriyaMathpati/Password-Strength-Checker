import string
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🔐",
    layout="centered"
)


# Password analysis function
def check_password(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Character checks
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    number = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    if uppercase:
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if lowercase:
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if number:
        score += 1
    else:
        suggestions.append("Add a number.")

    if special:
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Repeated character check
    repeated = any(
        password[i] == password[i + 1]
        for i in range(len(password) - 1)
    )

    if repeated:
        score -= 1
        suggestions.append("Avoid repeated characters.")

    # Common pattern check
    patterns = ["password", "1234", "qwerty", "admin"]
    common = any(p in password.lower() for p in patterns)

    if common:
        score -= 2
        suggestions.append("Avoid common password patterns.")

    # Sequential character check
    sequential = any(
        ord(password[i + 1]) == ord(password[i]) + 1
        and ord(password[i + 2]) == ord(password[i + 1]) + 1
        for i in range(len(password) - 2)
    )

    if sequential:
        score -= 1
        suggestions.append("Avoid sequential characters.")

    # Strength classification
    if score >= 6 and len(password) >= 12 and not repeated:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    checks = {
        "At least 12 characters": len(password) >= 12,
        "Uppercase letter": uppercase,
        "Lowercase letter": lowercase,
        "Number": number,
        "Special character": special,
        "No repeated characters": not repeated,
        "No common patterns": not common,
        "No sequential characters": not sequential
    }

    return strength, score, suggestions, checks


# Create explanation
def explain_result(strength, checks):
    passed = []
    failed = []

    for requirement, result in checks.items():
        if result:
            passed.append(requirement)
        else:
            failed.append(requirement)

    explanation = []

    if passed:
        explanation.append(
            "It meets these checks: " + ", ".join(passed) + "."
        )

    if failed:
        explanation.append(
            "It needs improvement in: " + ", ".join(failed) + "."
        )

    if strength == "Strong":
        explanation.append(
            "The password meets the application's stronger "
            "security criteria."
        )
    elif strength == "Medium":
        explanation.append(
            "The password meets some security criteria but "
            "has areas that can be improved."
        )
    else:
        explanation.append(
            "The password has several characteristics that "
            "can make it easier to guess."
        )

    return " ".join(explanation)


# Clear input callback
def clear_password():
    st.session_state["password_input"] = ""


# User interface
st.title("🔐 Password Strength Checker")

st.write(
    "Analyze password strength and get security "
    "recommendations."
)

st.info(
    "Use a dummy password for testing. "
    "This application does not save your password."
)

password = st.text_input(
    "Enter your password",
    type="password",
    key="password_input",
    placeholder="Enter a test password"
)

col1, col2 = st.columns(2)

with col1:
    analyze = st.button(
        "🔍 Analyze Password",
        use_container_width=True
    )

with col2:
    st.button(
        "🗑️ Clear",
        on_click=clear_password,
        use_container_width=True
    )


if analyze:
    if not password:
        st.warning("Please enter a password.")

    else:
        strength, score, suggestions, checks = check_password(password)

        st.divider()
        st.subheader("📊 Analysis Result")

        # Strength result
        if strength == "Strong":
            st.success("🟢 Password Strength: Strong")

        elif strength == "Medium":
            st.warning("🟡 Password Strength: Medium")

        else:
            st.error("🔴 Password Strength: Weak")

        # Strength meter
        progress = max(0, min(score, 6)) / 6

        st.write("Strength Meter")
        st.progress(progress)

        st.caption(f"Analysis score: {score} / 6")

        # Why this result?
        st.subheader("💡 Why this result?")

        explanation = explain_result(strength, checks)

        st.write(explanation)

        # Requirements checklist
        st.subheader("✅ Password Requirements")

        for requirement, passed in checks.items():

            if passed:
                st.write(f"✅ {requirement}")

            else:
                st.write(f"❌ {requirement}")

        # Security recommendations
        st.subheader("🛡️ Security Recommendations")

        if suggestions:

            for suggestion in suggestions:
                st.write(f"• {suggestion}")

        else:
            st.success("No basic issues detected.")

        st.caption(
            "This is a basic rule-based assessment, "
            "not a guarantee of password security."
        )


st.divider()

st.subheader("🛡️ Basic Password Security Tips")

st.write("• Use long and unique passwords.")
st.write("• Avoid common words and predictable patterns.")
st.write("• Avoid reusing the same password across different accounts.")
st.write("• Do not share your passwords with others.")
st.write("• Do not store passwords as plain text.")
st.write("• Use appropriate password-hashing methods when passwords "
         "must be stored by an application.")

st.caption(
    "Cyber Security Internship Project | "
    "NexOrbiX Technologies"
)