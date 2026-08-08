import matplotlib.pyplot as plt
import pandas as pd

def choose_chart(df):

    if df.empty:
        return None

    cols = df.columns

    if len(cols) == 1:
        if pd.api.types.is_numeric_dtype(df[cols[0]]):
            return "hist"

    elif len(cols) == 2:

        col1 = df[cols[0]]
        col2 = df[cols[1]]

        num1 = pd.api.types.is_numeric_dtype(col1)
        num2 = pd.api.types.is_numeric_dtype(col2)

        if not num1 and num2:

            if len(df) <= 6:
                return "pie"

            return "bar"

        if num1 and num2:
            return "scatter"

    return "bar"


def draw_chart(df):

    chart = choose_chart(df)

    if chart is None:
        return None

    fig, ax = plt.subplots(figsize=(8,5))

    if chart == "bar":

        ax.bar(df.iloc[:,0], df.iloc[:,1])
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel(df.columns[1])

    elif chart == "line":

        ax.plot(df.iloc[:,0], df.iloc[:,1], marker="o")
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel(df.columns[1])

    elif chart == "pie":

        ax.pie(
            df.iloc[:,1],
            labels=df.iloc[:,0],
            autopct="%1.1f%%"
        )

    elif chart == "scatter":

        ax.scatter(
            df.iloc[:,0],
            df.iloc[:,1]
        )

        ax.set_xlabel(df.columns[0])
        ax.set_ylabel(df.columns[1])

    elif chart == "hist":

        ax.hist(df.iloc[:,0], bins=10)
        ax.set_xlabel(df.columns[0])

    ax.set_title(f"Auto Chart ({chart.upper()})")

    plt.tight_layout()

    return fig