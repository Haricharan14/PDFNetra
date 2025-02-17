```
Exam : Quiz 1
Subject: MLT
Total Marks : 50.00
QP: 2024 Oct27: IIT M AN EXAM QDD2

1.  THIS IS QUESTION PAPER FOR THE SUBJECT "DIPLOMA LEVEL : MACHINE
    LEARNING TECHNIQUES (COMPUTER BASED EXAM)" ARE YOU SURE YOU HAVE
    TO WRITE EXAM FOR THIS SUBJECT? CROSS CHECK YOUR HALL TICKET TO
    CONFIRM THE SUBJECTS TO BE WRITTEN. (IF IT IS NOT THE CORRECT SUBJECT,
    PLS CHECK THE SECTION AT THE TOP FOR THE SUBJECTS REGISTERED BY YOU)
    OPTIONS:
    (a) YES, (b) NO

2.  Let x = $\begin{bmatrix} x1 \\ x2 \end{bmatrix}$ and y = $\begin{bmatrix} y1 \\ y2 \end{bmatrix}$ be vectors in R². Define the functions k₁ and k₂ as:

    $k_1(x, y) = x_1y_1 + x_2y_2 + (x_1 + x_2)(y_1 + y_2)$
    $k_2(x, y) = x_1y_1 + x_2y_2 + (x_1^2 + y_2^2) + 3$

    Which of the following statements is true?
    OPTIONS:
    (a) Both $k_1$ and $k_2$ are valid kernels., (b) $k_1$ is a valid kernel, but $k_2$ is not a valid kernel., (c) $k_2$ is a valid kernel, but $k_1$ is not a valid kernel., (d) Neither $k_1$ nor $k_2$ is a valid kernel.

3.  Consider the following kernel:

    $k: \mathbb{R}^2 \times \mathbb{R}^2 \rightarrow \mathbb{R}$
    $k(x, y) = (x^Ty)^2 + 1$

    Which of the following transformation mapping $\phi$ may correspond to the kernel $k$?
    OPTIONS:
     (a) $\phi([x_1, x_2]^T) = [x_1^2, \sqrt{2}x_1x_2, x_2^2, 1]^T$, (b) $\phi([x_1, x_2]^T) = [x_1^2, x_1 + x_2, x_2^2, 1]^T$, (c) $\phi([x_1, x_2]^T) = [x_1, \sqrt{2}x_1x_2^2, 1]^T$, (d)  $\phi([x_1, x_2]^T) = [x_1, x_1x_2, x_2, 1]^T$

4.  Given $n$ data points in a $d$-dimensional space with a non-linear relationship,
    we apply kernel PCA to reduce the dimensionality and select the first $k$ principal
    components. Is it possible for $k$ to be greater than $d$?
    OPTIONS:
    (a) yes, (b) No

5.  Which of the following expressions is the reconstruction error for a dataset of
    $n$ points, with respect to a line passing through the origin represented by the vector w.
    Note that $||w|| = 1$.
    OPTIONS:
    (a) $\frac{1}{n}\sum_{i=1}^{n} ||x_i - (x_i^Tw)w||^2$, (b) $\frac{1}{n}\sum_{i=1}^{n} [x_i - (x_i^Tw)w]^T[x_i - (x_i^Tw)w]$, (c) $\frac{1}{n}\sum_{i=1}^{n} [x_i^Tx_i - (x_i^Tw)^2]$, (d) $\frac{1}{n}\sum_{i=1}^{n} (x_i^Tw)^2$

6.  Let $X_1, X_2, ..., X_n$ be n i.i.d. samples with parameter $\theta$, which follows one
    of the following PDFs:
    For $\theta = -1$, we have

    $f(x | \theta) = \begin{cases}
    5x^4, & \text{if } 0 < x < 1 \\
    0, & \text{otherwise}
    \end{cases}$

    For $\theta = 1$, we have

    $f(x | \theta) = \begin{cases}
    1, & \text{if } 0 < x < 1 \\
    0, & \text{otherwise}
    \end{cases}$

    Suppose we wish to find the maximum likelihood estimate of $\theta$, then which among the
    following are true?
    OPTIONS:
    (a) If $\prod_{i=1}^{n} 5x_i^4 < 1$, then $\hat{\theta}_{MLE} = 1$, (b) If $\prod_{i=1}^{n} 5x_i^4 > 1$, then $\hat{\theta}_{MLE} = 1$, (c) If $\prod_{i=1}^{n} 5x_i^4 < 1$, then $\hat{\theta}_{MLE} = -1$, (d) If $\prod_{i=1}^{n} 5x_i^4 > 1$, then $\hat{\theta}_{MLE} = -1$

7.  The eigenvalues of the covariance matrix of a centered dataset in $\mathbb{R}^5$ are
    30, 10, 10, 0, 0. Standard PCA is performed on this dataset. What is the variance
    captured by the top two principal components expressed as a percentage of total
    variance?
    Answer (Numeric): 80

8.  Consider the following data points for k-means clustering.
    (-1,0), (-1, 1), (-1,-1), (2, 0), (3, 1), (3, -1), (4, 0)
    In the initialization step of k-means with k = 2, suppose $\mu_1^0 = (-1,0)$ and $\mu_2^0 = (2,0)$.
    Distances of datapoints from initial cluster means is tabulated below:

    | $x_i$     | $||x_i - \mu_1^0||^2$ | $||x_i - \mu_2^0||^2$ |
    | --------- | --------------------- | --------------------- |
    | (-1,0)    | 0                     | 3                     |
    | (-1,1)    | 1                     | 10                    |
    | (-1,-1)   | 1                     | 10                    |
    | (2,0)     | 3                     | 0                     |
    | (3,1)     | 17                    | 2                     |
    | (3,-1)    | 17                    | 2                     |
    | (4,0)     | 5                     | 2                     |

    As per these cluster centers, the data points are then assigned to either cluster 1 or
    cluster 2. After this assignment, what will be the value of the objective function?
    Note: Objective function is given by

    $F(z_1, z_2, ..., z_n) = \sum_{i=1}^{n} ||x_i - \mu_{z_i}||^2$
   Answer (Numeric): 6

9.  Consider a GMM for 5 points:

    $x_1 = 1, x_2 = 1.2, x_3 = 2, x_4 = 1.5, x_5 = 0.5$

    At some time-step in the EM algorithm, following are the values of $\lambda_i^k$ for the k-th
    mixture after the E-step:

    $\lambda_1^1 = 0.3, \lambda_2^1 = 0.1, \lambda_3^1 = 2.5, \lambda_4^1 = 0.6, \lambda_5^1 = 0.8$

    What is the estimate of $\mu_k$ after the M-step? Enter your answer correct to two decimal
    places.
    Answer (Numeric): 1.50 to 1.60

10. Consider a dataset with 100 total data points. Each data point is classified as
    either type A or type B. We model this using a Bernoulli distribution, where p is the
    probability of a data point being type A. If the maximum likelihood estimate (MLE)
    of p based on the dataset is 0.4, how many data points of type B are there in this
    dataset?
    Answer (Numeric): 60

11. Given the vector x = $\begin{bmatrix} 3 \\ 4 \end{bmatrix}$ and the line passing through the origin represented
    by the vector w = $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
    Answer the given subquestions.

12. Find the length of the projection of x
    onto the line defined by w.
    Enter your answer correct to two
    decimal places.
    Answer (Numeric): 4.8 to 5.1

13. Calculate the magnitude(norm) of
    reconstruction error after projecting
    x onto the line defined by w.
    Enter your answer correct to two
    decimal places.
   Answer (Numeric): 0.5 to 0.9

14. Based on the above data, answer the given subquestions.
 A k-means++ algorithm with k = 3 is applied on the following 2D points:
 (0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (2, 4), (3, 2)
 First cluster mean $\mu_1^0$ is chosen as (2, 1).
 Suppose the point with the highest score is chosen as the 2nd cluster mean $\mu_2^0$.

15. What is $\mu_2^0$? Use squared distance to
    calculate the scores.
    OPTIONS:
    (a) (0,1), (b) (2,3), (c) (3,2), (d) (2,4)

16. Which point has the lowest probability of being chosen as the 3rd cluster mean?
    Use squared distance to calculate the scores.
    OPTIONS:
    (a) (1,0), (b) (2,3), (c) (3,2), (d) (1,2)
```

