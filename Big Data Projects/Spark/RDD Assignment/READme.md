
## Avg (Friends) by Age - Spark RDDs

Spark project to analyze dataset of social network users to compute the **average number of friends per age group** using **pure RDD operations**.

---

### File Structure

```
.
├── average_friends_by_age.csv   # Output file
├── RDD_Assignment.ipynb
├── rdd_assignment.py            #Script
├── fakefriends.csv              # Input dataset
└── READme.md
```

### Dataset

**File:** `fakefriends.csv`

**Columns:**
1. ID
2. Name
3. Age
4. Number of Friends

### Goal

Compute analysis:

```
(age, average_number_of_friends)
```

### Technologies Used

* Apache Spark (RDD API)
* Google Colab
* Python (PySpark)
* CSV I/O

---

### How It Works

* Transform: (age, num_friends) → (age, (num_friends, 1))
* Reduce: (age, (sum_friends, count)) by age
* Average: (age, (sum, count)) → (age, avg)

### How `mapValues` and `reduceByKey` Work Together

To **compute the average number of friends per age**:

#### `mapValues(lambda x: (x, 1))`

* Transforms each record from `(age, num_friends)` into `(age, (num_friends, 1))`
* Purpose: Track both the **sum of friends** and the **count of people** per age

\| Input: `(21, 100)` → Output: `(21, (100, 1))` |

---

####  `reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))`

* Aggregates all values for each age:

  * Adds up all friend counts (`x[0] + y[0]`)
  * Adds up all person counts (`x[1] + y[1]`)

\| Example: |

```python
(21, (100, 1))  
(21, (200, 1))  
⇒ reduceByKey ⇒ (21, (300, 2))
```

---

#### `mapValues(lambda x: round(x[0] / x[1], 2))`

* Calculates the average for each age:

  * `x[0]` = total friends
  * `x[1]` = total people
  * Returns average rounded to 2 decimal places

\| Input: `(21, (300, 2))` → Output: `(21, 150.0)` |

---

### Sample Output

```
(18, 343.38)
(19, 213.27)
(20, 165.0)
(21, 350.88)
(22, 206.43)
(23, 246.3)
(24, 233.8)
...
```
---

### Run the Script

1. Place `fakefriends.csv` in the same directory.
2. Run with Spark:

```bash
spark-submit rdd_assignment.py
```
