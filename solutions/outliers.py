lower = q1 - 1.5 * iqr
print(lower)
# ok, i dont need to worry about that!
outliers = df[df.SalePrice >= q3 + 1.5 * iqr]
