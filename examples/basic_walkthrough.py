"""Minimal example of XGBDistribution on Boston Housing dataset"""

from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

from xgboost_distribution import XGBDistribution


def plot_residuals(y_true, y_pred, y_err):
    fig, ax = plt.subplots()
    ax.errorbar(
        y_true,
        y_true - y_pred,
        yerr=y_err,
        marker="o",
        linestyle="None",
        c="k",
        markersize=2.5,
        linewidth=0.5,
    )
    ax.axhline(0, c="k", linestyle="--")
    ax.set_xlabel("y_test")
    ax.set_ylabel("y_test - y_pred")
    plt.show()


def main():
    data = fetch_california_housing()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    X_train, X_eval, y_train, y_eval = train_test_split(
        X_train, y_train, random_state=0
    )

    model = XGBDistribution(
        distribution="normal",
        natural_gradient=True,
        max_depth=2,
        n_estimators=500,
        early_stopping_rounds=10,
    )
    model.fit(
        X_train,
        y_train,
        eval_set=[(X_eval, y_eval)],
        verbose=False,
    )
    preds = model.predict(X_test)
    plot_residuals(y_true=y_test, y_pred=preds.loc, y_err=preds.scale)


if __name__ == "__main__":
    main()
