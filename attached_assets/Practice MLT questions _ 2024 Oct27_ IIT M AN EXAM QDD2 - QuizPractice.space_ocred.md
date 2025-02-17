Exam :
Subject:
Total Marks :
QP:
Quiz 1
MLT
50.00
2024 Oct27: IIT M AN EXAM QDD2

Question 1:640653995436
Total Mark: 0.00 | Type: MCQ
THIS IS QUESTION PAPER FOR THE SUBJECT "DIPLOMA LEVEL : MACHINE
LEARNING TECHNIQUES (COMPUTER BASED EXAM)" ARE YOU SURE YOU HAVE
TO WRITE EXAM FOR THIS SUBJECT? CROSS CHECK YOUR HALL TICKET TO
CONFIRM THE SUBJECTS TO BE WRITTEN. (IF IT IS NOT THE CORRECT SUBJECT,
PLS CHECK THE SECTION AT THE TOP FOR THE SUBJECTS REGISTERED BY YOU)
OPTIONS:
YES
NO
Your score: 0

Question 2:640653995442
View Solutions (0) Total Mark: 4.00 | Type : MCQ
Let x =
$\begin{bmatrix} x1 \\ x2 \end{bmatrix}$
and y =
$\begin{bmatrix} y1 \\ y2 \end{bmatrix}$ be vectors in $R^2$. Define the functions $k_1$ and $k_2$ as:

$k_1(x, y) = x_1y_1 + x_2y_2 + (x_1 + x_2)(y_1 + y_2)$
$k_2(x, y) = x_1y_1 + x_2y_2 + (x_1^2 + y_2^2) + 3$
Which of the following statements is true?
OPTIONS:
Both $k_1$ and $k_2$ are valid kernels.
$k_1$ is a valid kernel, but $k_2$ is not a valid kernel.
$k_2$ is a valid kernel, but $k_1$ is not a valid kernel.
Neither $k_1$ nor $k_2$ is a valid kernel.
Your score: 0

Question 3: 640653995444
View Solutions (0) Total Mark: 4.00 | Type : MCQ
Consider the following kernel:

$k: R^2 * R^2 -> R$
$k(x,y) = (x^Ty)^2 + 1$
Which of the following transformation mapping $\phi$ may correspond to the kernel $k$?
OPTIONS:

Question 4:640653995443
View Solutions (0) Total Mark: 3.00 | Type : MCQ
Given n data points in a d-dimensional space with a non-linear relationship,
we apply kernel PCA to reduce the dimensionality and select the first k principal
components. Is it possible for k to be greater than d?
OPTIONS:
yes
No
Your score: 0

Question 5:640653995440
View Solutions (0) Total Mark: 4.00 | Type : MSQ
Which of the following expressions is the reconstruction error for a dataset of
n points, with respect to a line passing through the origin represented by the vector w.
Note that ||w|| = 1.
OPTIONS:
$\frac{1}{n}\sum_{i=1}^{n}||x_i - (x_i^Tw)w||^2$
$\frac{1}{n}\sum_{i=1}^{n}[x_i - (x_i^Tw)w]^T[x_i - (x_i^Tw)w]$
$\frac{1}{n}\sum_{i=1}^{n}[x_i^Tx_i - (x_i^Tw)^2]$
$\frac{1}{n}\sum_{i=1}^{n}(x_i^Tw)^2$
Your score: 0

Question 6:640653995449
View Solutions (0) Total Mark: 5.00 | Type : MSQ
Let $X_1, X_2, ..., X_n$ be n i.i.d. samples with parameter θ, which follows one
of the following PDFs:
For θ = -1, we have

$f(x | \theta) = \begin{cases} 5x^4, & \text{if } 0 < x < 1 \\ 0, & \text{otherwise} \end{cases}$

For θ = 1, we have

$f(x | \theta) = \begin{cases} 1, & \text{if } 0 < x < 1 \\ 0, & \text{otherwise} \end{cases}$

Suppose we wish to find the maximum likelihood estimate of θ, then which among the
following are true?
OPTIONS:
If $\prod_{i=1}^n 5x_i^4 < 1$, then $\hat{\theta}_{MLE} = 1$
If $\prod_{i=1}^n 5x_i^4 > 1$, then $\hat{\theta}_{MLE} = 1$
If $\prod_{i=1}^n 5x_i^4 < 1$, then $\hat{\theta}_{MLE} = -1$
If $\prod_{i=1}^n 5x_i^4 > 1$, then $\hat{\theta}_{MLE} = -1$
Your score: 0

Question 7:640653995441
View Solutions (0) Total Mark: 3.00 | Type : SA
The eigenvalues of the covariance matrix of a centered dataset in $R^5$ are
30, 10, 10, 0, 0. Standard PCA is performed on this dataset. What is the variance
captured by the top two principal components expressed as a percentage of total
variance?
Answer (Numeric):
Answer
Accepted Answer : 80
Your score: 0

Question 8:640653995448
View Solutions (0) Total Mark: 5.00 | Type : SA
Consider the following data points for k-means clustering.
(-1,0), (-1, 1), (-1,-1), (2, 0), (3, 1), (3, 1), (4, 0)
In the initialization step of k-means with k = 2, suppose $\mu_1^0 = (-1,0)$ and $\mu_2^0 = (2,0)$.
Distances of datapoints from initial cluster means is tabulated below:

$x_i$	$||x_i - \mu_1^0||^2$	$||x_i - \mu_2^0||^2$
(-1,0)	0	3
(-1,1)	1	10
(-1,-1)	1	10
(2,0)	3	0
(3,1)	17	2
(3,-1)	17	2
(4,0) 5 2

As per these cluster centers, the data points are then assigned to either cluster 1 or
cluster 2. After this assignment, what will be the value of the objective function?
Note: Objective function is given by

$F(z_1, z_2, ..., z_n) = \sum_{i=1}^{n}||x_i - \mu_{z_i}||^2$

Answer (Numeric):
Answer
Accepted Answer : 6
Your score: 0

Question 9:640653995450
View Solutions (0) Total Mark: 4.00 | Type : SA
Consider a GMM for 5 points:

$x_1 = 1, x_2 = 1.2, x_3 = 2, x_4 = 1.5, x_5 = 0.5$
At some time-step in the EM algorithm, following are the values of $\lambda_k^i$ for the k-th
mixture after the E-step:

$λ_1^1 = 0.3, λ_2^1 = 0.1, λ_3^1 = 2.5, λ_4^1 = 0.6, λ_5^1 = 0.8$

What is the estimate of $\mu_k$ after the M-step? Enter your answer correct to two decimal
places.
Answer (Numeric):
Answer
Accepted Answer : 1.50 to 1.60
Your score: 0

Question 10: 640653995451
View Solutions (0) Total Mark: 4.00 | Type : SA
Consider a dataset with 100 total data points. Each data point is classified as
either type A or type B. We model this using a Bernoulli distribution, where p is the
probability of a data point being type A. If the maximum likelihood estimate (MLE)
of p based on the dataset is 0.4, how many data points of type B are there in this
dataset?
Answer (Numeric):
Answer
Accepted Answer : 60
Your score: 0

Question 11: 640653995437
Total Mark: 0.00 | Type: COMPREHENSION
Given the vector x = $\begin{bmatrix} 3 \\ 4 \end{bmatrix}$ and the line passing through the origin represented
by the vector w = $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
Answer the given subquestions.
Your score: 0

Question 12:
640653995438
View Parent QN
View Solutions (0)
Total Mark: 3.00 | Type: SA
Find the length of the projection of x
onto the line defined by w.
Enter your answer correct to two
decimal places.

Question 13:
640653995439
Calculate the magnitude(norm) of
reconstruction error after projecting
x onto the line defined by w.
Enter your answer correct to two
decimal places.
Answer (Numeric):
Answer
Accepted Answer : 0.5 to 0.9
Your score: 0

Question 14: 640653995445
Total Mark: 0.00 | Type: COMPREHENSION
Based on the above data, answer the given subquestions.
A k-means++ algorithm with k = 3 is applied on the following 2D points:
(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (2, 4), (3, 2)
First cluster mean $\mu_1^0$ is chosen as (2, 1).
Suppose the point with the highest score is chosen as the 2nd cluster mean $\mu_2^0$.
Your score: 0

Question 15:
640653995446
View Parent QN
View Solutions (0)
Total Mark: 3.00 | Type: MCQ
What is $\mu_2^0$? Use squared distance to
calculate the scores.
OPTIONS:
(0,1)
(2,3)
(3,2)
(2,4)
Your score: 0

Question 16:
640653995447
View Parent QN
View Solutions (0)
Total Mark: 4.00 | Type: MCQ
Which point has the lowest probability of being chosen as the 3rd cluster mean?
Use squared distance to calculate the scores.
OPTIONS:
(1,0)
(2,3)
(3,2)
(1,2)
Your score: 0

