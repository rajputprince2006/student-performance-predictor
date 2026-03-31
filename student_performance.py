import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 90],
    "sleep_hours": [5, 6, 6, 7, 7, 8, 8, 9],
    "marks": [40, 45, 50, 55, 60, 70, 75, 90]
}

df = pd.DataFrame(data)
X = df[["study_hours", "attendance", "sleep_hours"]]
y = df["marks"]

model = LinearRegression().fit(X, y)

def predict_grade():
    print("Hi! Let's take a look at your study routine.")
    
    try:
        study = float(input("How many hours do you study daily? "))
        att = float(input("What's your attendance percentage? "))
        sleep = float(input("How many hours of sleep are you getting? "))

        input_data = pd.DataFrame([[study, att, sleep]],
                                  columns=["study_hours", "attendance", "sleep_hours"])

        prediction = model.predict(input_data)
        score = max(0.0, min(100.0, float(prediction[0])))

        print(f"\nPredicted Score: {score:.1f}%")
        
        print("\nAdvice for you:")
        tips = []
        
        if study < 5:
            tips.append("Try adding an extra hour of study to your day.")
        if att < 75:
            tips.append("Try to attend more classes to stay on track.")
        if sleep < 7:
            tips.append("Prioritize 7-8 hours of sleep; your brain needs it.")
        
        if not tips:
            print("Your habits look solid! Keep it up.")
        else:
            for tip in tips:
                print(f"- {tip}")

    except ValueError:
        print("Error: Please enter numbers only.")

if __name__ == "__main__":
    predict_grade()
