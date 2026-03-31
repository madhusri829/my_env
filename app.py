from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import gradio as gr
import matplotlib.pyplot as plt

# ---------------- EMAIL CONFIG ----------------
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"


def send_email(subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        return "Email sent"
    except Exception as e:
        return f"Email failed"


# ---------------- FEATURES ----------------

def detect_category(title):
    t = title.lower()
    if "python" in t or "study" in t:
        return "study"
    elif "hackathon" in t or "contest" in t:
        return "hackathon"
    elif "movie" in t:
        return "movies"
    elif "offer" in t or "free" in t or "click" in t:
        return "spam"
    return "others"


def detect_ads(title):
    return any(w in title.lower() for w in ["offer", "free", "buy", "sale"])


def detect_harmful(url):
    return "http://" in url or "spam" in url


def detect_cookie_risk(cookies):
    return any("track" in c.get("name", "") for c in cookies)


def get_month(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%B")
    except:
        return "Unknown"


def get_most_used(usage):
    return max(usage, key=usage.get)


def generate_reminder(category):
    if category == "study":
        return "Continue your learning today!"
    elif category == "hackathon":
        return "Don't miss your contest!"
    return "Check your activity"


def trust_score(url, title):
    score = 100
    if "http://" in url:
        score -= 40
    if any(w in title.lower() for w in ["free", "click", "offer"]):
        score -= 30
    if "spam" in url:
        score -= 30
    return max(score, 0)


def attention_flag(usage):
    return "High usage" if sum(usage.values()) > 10 else "Normal usage"


def detect_event(title):
    return "hackathon" in title.lower() or "contest" in title.lower()


# ---------------- MAIN LOGIC ----------------

def analyze(data):
    title = data.get("title", "")
    url = data.get("url", "")
    date = data.get("date", "2026-01-01")
    usage = data.get("usage_count", {"study": 1})
    cookies = data.get("cookies", [])

    category = detect_category(title)
    ads = detect_ads(title)
    harmful = detect_harmful(url)
    cookie_risk = detect_cookie_risk(cookies)
    month = get_month(date)
    most_used = get_most_used(usage)
    reminder = generate_reminder(category)
    trust = trust_score(url, title)
    attention = attention_flag(usage)
    event = detect_event(title)

    action = "remove" if (ads or harmful) else "keep"
    popup = "⚠ Harmful content!" if harmful else "Safe"
    privacy = "Tabs hidden"

    # Email (safe fail)
    email_status = "not_sent"
    if category in ["study", "hackathon"] or event:
        email_status = send_email(
            f"Reminder: {title}",
            f"{reminder}\n\nURL: {url}"
        )

    return {
        "category": category,
        "action": action,
        "harmful": harmful,
        "trust_score": trust,
        "reminder": reminder,
        "email_status": email_status,
        "privacy": privacy,
        "popup": popup
    }


# ---------------- UI FUNCTION ----------------

def ui_function(title, url, date, study_usage, hackathon_usage, cookie_name):
    data = {
        "title": title,
        "url": url,
        "date": date,
        "usage_count": {
            "study": study_usage,
            "hackathon": hackathon_usage
        },
        "cookies": [{"name": cookie_name}]
    }

    result = analyze(data)

    # Bar chart
    plt.figure()
    plt.bar(["Study", "Hackathon"], [study_usage, hackathon_usage])
    plt.title("Usage")
    bar_chart = plt.gcf()

    # Trend chart
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    plt.figure()
    plt.plot(months, [1, 2, 3, study_usage-1, study_usage])
    plt.plot(months, [0, 1, 2, hackathon_usage-1, hackathon_usage])
    plt.title("Trend")
    trend_chart = plt.gcf()

    return (
        result["category"],
        result["action"],
        result["harmful"],
        result["trust_score"],
        result["reminder"],
        result["email_status"],
        result["privacy"],
        result["popup"],
        bar_chart,
        trend_chart
    )


# ---------------- UI ----------------

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 AI Content Moderation")

    with gr.Row():
        with gr.Column():
            title = gr.Textbox(label="Title")
            url = gr.Textbox(label="URL")
            date = gr.Textbox(label="Date")
            study = gr.Number(value=1, label="Study Usage")
            hack = gr.Number(value=1, label="Hackathon Usage")
            cookie = gr.Textbox(label="Cookie")
            btn = gr.Button("Analyze")

        with gr.Column():
            cat = gr.Textbox(label="Category")
            act = gr.Textbox(label="Action")
            harm = gr.Textbox(label="Harmful")
            trust = gr.Textbox(label="Trust")
            rem = gr.Textbox(label="Reminder")
            email = gr.Textbox(label="Email")
            priv = gr.Textbox(label="Privacy")
            pop = gr.Textbox(label="Popup")

    bar = gr.Plot()
    trend = gr.Plot()

    btn.click(
        ui_function,
        inputs=[title, url, date, study, hack, cookie],
        outputs=[cat, act, harm, trust, rem, email, priv, pop, bar, trend]
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)