# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
def load_count(filepath: str) -> pd.DataFrame:
    _df = pd.read_csv(filepath)
    _df['year_month'] = _df.apply(lambda x: pd.to_datetime(x['year_month'], format='%Y-%m-%d %H:%M:%S'), axis=1)
    return _df


def plot_count(dataframes: list[pd.DataFrame], legend=None, out="comments_count.png") -> None:
    plt.figure(figsize=(16, 9))
    plt.ticklabel_format(useOffset=False, style='plain')
    for _df in dataframes:
        plt.plot(_df['year_month'], _df['row_count'])
    plt.legend(legend)
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.ylabel('Number of comments')
    if out:
        plt.savefig(out)
    plt.show()


def plot_increase(dataframes: list[pd.DataFrame], legend=None, out="comments_increase.png") -> None:
    plt.figure(figsize=(16, 9))
    plt.ticklabel_format(useOffset=False, style='plain')
    for _df in dataframes:
        plt.plot(_df['year_month'], _df['row_count'] / _df['row_count'].max())
    plt.legend(legend)
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.ylabel('Increase in comments')
    if out:
        plt.savefig(out)
    plt.show()


def plot_count_by_year(dataframes: list[pd.DataFrame], legend=None, out="comments_count_by_year.png") -> None:
    plt.figure(figsize=(16, 9))
    plt.ticklabel_format(useOffset=False, style='plain')
    for _df in dataframes:
        _d = _df.groupby(_df['year_month'].dt.year).sum(True)
        plt.bar(_d.index, _d['row_count'])
    plt.legend(legend)
    plt.xlabel('Date')
    plt.ylabel('Number of comments')
    if out:
        plt.savefig(out)
    plt.show()

# %%
df_orig = load_count('csv/comments_count_orig.csv')
df_delete_deleted = load_count('csv/comments_count_1.csv')
df_select_longer_than_1000 = load_count('csv/comments_count_2.csv')

# %%
plot_count([df_orig, df_delete_deleted, df_select_longer_than_1000],
           legend=["Original", "DELETE FROM reddit WHERE body = '[deleted]'",
                   "SELECT INTO cleared FROM reddit WHERE length(body) > 1000"])

# %%
plot_increase([df_orig, df_delete_deleted, df_select_longer_than_1000],
              legend=["Original", "DELETE FROM reddit WHERE body = '[deleted]'",
                      "SELECT INTO cleared FROM reddit WHERE length(body) > 1000"])

# %%
plot_count_by_year([df_orig, df_delete_deleted, df_select_longer_than_1000],
                   legend=["Original", "DELETE FROM reddit WHERE body = '[deleted]'",
                           "SELECT INTO cleared FROM reddit WHERE length(body) > 1000"])

# %%
df_select_longer_than_1000['row_count'].sum() / df_orig['row_count'].sum()
