import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from fpdf import FPDF
import google.generativeai as genai
import threading

# ✅ Gemini API Key PLEASE ADD YOUR I CAN'T SHARE MINE WITH YOU SORRY
API_KEY = "YOUR API KEY" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

# 🧠 Prompt Builder
def build_prompt(data):
    return f"""
You are a clinical assistant AI for early detection of structural heart diseases (SHD), especially in low-resource settings.

User Demographics:
- Name: {data['name']}
- Age: {data['age']}
- Age Group: {data['age_group']}
- Gender: {data['gender']}
- Height: {data['height']} cm
- Weight: {data['weight']} kg
- City: {data['city']}

Vitals:
- Blood Pressure: {data['bp']}
- Heart Rate: {data['hr']} BPM
- SpO2: {data['spo2']}
- Allergies: {data['allergies']}

Lifestyle:
- Smoking: {data['smoking']}
- Alcohol: {data['alcohol']}
- Tobacco: {data['tobacco']}
- Hypertensive Drugs: {data['hypertensive']}
- Diabetes/High Sugar: {data['diabetes']}

SHD-Specific Symptoms:
- Cyanosis: {data['cyanosis']}
- Chest Pain: {data['chest_pain']}
- Fatigue: {data['fatigue']}
- Shortness of Breath: {data['sob']}
- Syncope (Fainting): {data['syncope']}
- Palpitations: {data['palpitations']}
- Family History of SHD: {data['family_history']}
- Feeding Issues (newborns only): {data['feeding']}

General Symptoms:
{data['symptoms']}

Your tasks:
1. Estimate risk score for structural heart disease (0-10).
2. Highlight if urgent cardiologist consult is needed.
3. Suggest next steps (tests like ECHO, ECG).
4. List possible SHD conditions (ASD, VSD, valve issues, etc.).
5. Suggest what to tell the doctor.
6. Show 3 cardiac hospitals in {data['city']} India.
7. If rural/low-resource, give alternative screening ideas.
8. Provide red flags & continuous care advice.
9. Doctor summary at the end.
"""

# 🔍 Analyze Function
def analyze():
    loading_label.config(text="Analyzing...")
    analyze_button.config(state="disabled")

    def worker():
        try:
            data = {
                'name': name_var.get(),
                'age': age_var.get(),
                'age_group': age_group_var.get(),
                'gender': gender_var.get(),
                'height': height_var.get(),
                'weight': weight_var.get(),
                'city': city_var.get(),
                'bp': bp_var.get(),
                'hr': hr_var.get(),
                'spo2': spo2_var.get(),
                'allergies': allergies_var.get(),
                'smoking': smoking_var.get(),
                'alcohol': alcohol_var.get(),
                'tobacco': tobacco_var.get(),
                'hypertensive': hypertensive_var.get(),
                'diabetes': diabetes_var.get(),
                'cyanosis': cyanosis_var.get(),
                'chest_pain': chest_pain_var.get(),
                'fatigue': fatigue_var.get(),
                'sob': sob_var.get(),
                'syncope': syncope_var.get(),
                'palpitations': palpitations_var.get(),
                'family_history': family_history_var.get(),
                'feeding': feeding_var.get(),
                'symptoms': symptoms_text.get("1.0", tk.END).strip()
            }

            prompt = build_prompt(data)
            response = model.generate_content(prompt)
            result = response.text

            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result)
            loading_label.config(text="Analysis Complete ✅")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            loading_label.config(text="")
        finally:
            analyze_button.config(state="normal")

    threading.Thread(target=worker).start()

# 📝 PDF Generator
def save_as_pdf():
    content = output_text.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Warning", "No analysis result to save.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in content.split("\n"):
        line = line.encode("ascii", "ignore").decode("ascii")  # remove emojis
        pdf.multi_cell(0, 10, line)

    pdf.output("SHD_AI_Report.pdf")
    messagebox.showinfo("Success", "PDF saved as SHD_AI_Report.pdf")

# 🎨 UI Setup
root = tk.Tk()
root.title("Structural Heart Disease Screening AI")
root.geometry("1200x900")

canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
frame = scrollable_frame

# 📋 Basic Fields
labels = [
    "Name", "Age", "Gender", "Height (cm)", "Weight (kg)", "City",
    "Blood Pressure", "Heart Rate", "SpO2", "Allergies"
]
vars = [tk.StringVar() for _ in labels]
(name_var, age_var, gender_var, height_var, weight_var, city_var,
 bp_var, hr_var, spo2_var, allergies_var) = vars

for i, (label, var) in enumerate(zip(labels, vars)):
    ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w", padx=10)
    ttk.Entry(frame, textvariable=var, width=50).grid(row=i, column=1, padx=10, pady=2)

# 🧒 Age Group
ttk.Label(frame, text="Age Group (Newborn/Child/Adult)").grid(row=10, column=0, sticky="w", padx=10)
age_group_var = tk.StringVar()
ttk.Combobox(frame, textvariable=age_group_var, values=["Newborn", "Child", "Adult"], width=48).grid(row=10, column=1, padx=10)

# 💉 Lifestyle Inputs
lifestyle_questions = [
    ("Smoking (Yes/No)", 'smoking_var'),
    ("Alcohol (Yes/No)", 'alcohol_var'),
    ("Tobacco (Yes/No)", 'tobacco_var'),
    ("Hypertensive Drugs (Yes/No)", 'hypertensive_var'),
    ("Diabetes/High Sugar (Yes/No)", 'diabetes_var'),
]
for i, (label, name) in enumerate(lifestyle_questions, start=11):
    globals()[name] = tk.StringVar()
    ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w", padx=10)
    ttk.Entry(frame, textvariable=globals()[name], width=50).grid(row=i, column=1, padx=10)

# ❤️ SHD Symptoms Section
symptom_questions = [
    ("Cyanosis (Blue lips/skin)", 'cyanosis_var'),
    ("Chest Pain", 'chest_pain_var'),
    ("Fatigue", 'fatigue_var'),
    ("Shortness of Breath", 'sob_var'),
    ("Syncope (Fainting)", 'syncope_var'),
    ("Palpitations", 'palpitations_var'),
    ("Family History of SHD", 'family_history_var'),
    ("Feeding Issues (newborn only)", 'feeding_var'),
]
for i, (label, name) in enumerate(symptom_questions, start=16):
    globals()[name] = tk.StringVar()
    ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w", padx=10)
    ttk.Entry(frame, textvariable=globals()[name], width=50).grid(row=i, column=1, padx=10)

# 🗒️ General Symptoms
ttk.Label(frame, text="Describe Other Symptoms").grid(row=24, column=0, sticky="nw", padx=10)
symptoms_text = scrolledtext.ScrolledText(frame, width=60, height=5)
symptoms_text.grid(row=24, column=1, padx=10)

# 🔘 Buttons
button_frame = ttk.Frame(frame)
button_frame.grid(row=25, column=1, sticky="w", pady=10, padx=10)

analyze_button = ttk.Button(button_frame, text="Analyze My Heart Health", command=analyze)
analyze_button.pack(side="left", padx=5)

ttk.Button(button_frame, text="Generate PDF", command=save_as_pdf).pack(side="left", padx=5)

loading_label = ttk.Label(frame, text="", foreground="blue")
loading_label.grid(row=26, column=1, pady=5)

# 🧠 Output
ttk.Label(frame, text="🧠 AI SHD Risk & Analysis").grid(row=27, column=0, sticky="nw", pady=10, padx=10)
output_text = scrolledtext.ScrolledText(frame, width=100, height=15, wrap=tk.WORD)
output_text.grid(row=27, column=1, pady=10, padx=10)

# ❌ Clear Button
def clear_all():
    for var in vars + [age_group_var, smoking_var, alcohol_var, tobacco_var, hypertensive_var,
                       diabetes_var, cyanosis_var, chest_pain_var, fatigue_var, sob_var,
                       syncope_var, palpitations_var, family_history_var, feeding_var]:
        var.set("")
    symptoms_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    loading_label.config(text="")

ttk.Button(frame, text="Clear", command=clear_all).grid(row=28, column=1, sticky="e", pady=5, padx=10)

root.mainloop()
