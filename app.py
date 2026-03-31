import gradio as gr
import matplotlib.pyplot as plt
from datetime import datetime

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


def detect_harmful(url):
    return "http://" in url or "spam" in url


def get_month(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%B")
    except:
        return "Unknown"


def get_most_used(usage):
    return max(usage, key=usage.get)


def generate_reminder(category):
    if category == "study":
        return "📘 Continue your learning today!"
    elif category == "hackathon":
        return "💻 Don't miss your contest!"
    return "🔔 Check your activity"


def trust_score(url, title):
    score = 100
    if "http://" in url:
        score -= 40
    if any(w in title.lower() for w in ["free", "click", "offer"]):
        score -= 30
    if "spam" in url:
        score -= 30
    return max(score, 0)


# ---------------- MAIN FUNCTION ----------------

def analyze(title, url, date, study_usage, hackathon_usage, cookie_name):

    usage = {
        "study": study_usage,
        "hackathon": hackathon_usage
    }

    category = detect_category(title)
    harmful = detect_harmful(url)
    month = get_month(date)
    most_used = get_most_used(usage)
    reminder = generate_reminder(category)
    trust = trust_score(url, title)

    action = "remove" if harmful else "keep"
    popup = "⚠ Harmful content detected!" if harmful else "Safe content"
    privacy = "Tabs hidden from others"

    # 📊 Bar Chart
    plt.figure()
    plt.bar(["Study", "Hackathon"], [study_usage, hackathon_usage])
    plt.title("Current Usage")
    bar_chart = plt.gcf()

    # 📈 Trend Chart
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    plt.figure()
    plt.plot(months, [1, 2, 3, max(study_usage-1, 0), study_usage])
    plt.plot(months, [0, 1, 2, max(hackathon_usage-1, 0), hackathon_usage])
    plt.title("Monthly Trend")
    trend_chart = plt.gcf()

    return (
        category,
        action,
        harmful,
        trust,
        reminder,
        privacy,
        popup,
        bar_chart,
        trend_chart
    )


# ---------------- UI ----------------

with gr.Blocks() as demo:

    gr.Markdown("# 🚀 AI Content Moderation Dashboard")

    with gr.Row():
        with gr.Column():
            title = gr.Textbox(label="Title")
            url = gr.Textbox(label="URL")
            date = gr.Textbox(label="Date (YYYY-MM-DD)")

            study = gr.Number(label="Study Usage", value=1)
            hack = gr.Number(label="Hackathon Usage", value=1)

            cookie = gr.Textbox(label="Cookie Name")

            btn = gr.Button("🔍 Analyze")

        with gr.Column():
            category = gr.Textbox(label="Category")
            action = gr.Textbox(label="Action")
            harmful = gr.Textbox(label="Harmful")
            trust = gr.Textbox(label="Trust Score")
            reminder = gr.Textbox(label="Reminder")
            privacy = gr.Textbox(label="Privacy")
            popup = gr.Textbox(label="Popup")

    gr.Markdown("## 📊 Usage Analytics")
    bar_chart = gr.Plot()

    gr.Markdown("## 📈 Monthly Trend")
    trend_chart = gr.Plot()

    btn.click(
        analyze,
        inputs=[title, url, date, study, hack, cookie],
        outputs=[
            category, action, harmful, trust,
            reminder, privacy, popup,
            bar_chart, trend_chart
        ]
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)