### Multivariate Linear Regression | Gradient Descent | Normal Equation

    A Linear regression predicts a real-valued output based on an input value.The target variable in a problem that we want to predict should be continuous, to use linear regression for prediction.Linear regression with multiple variables is also known as "multivariate linear regression".

    ![Multivariate Linear Regression: Hypothesis]()

    In the above equation, we can measure the accuracy of our hypothesis function by using a cost function. This takes an average difference (actually a fancier version of an average) of all the results of the hypothesis with inputs from x's and the actual output y's.

    ![Cost Function J]()

    So we have our hypothesis function and we have a way of measuring how well it fits into the data. Now we need to estimate the parameters in the hypothesis function. That's where gradient descent comes in.

    Gradient Descent Algorithm is used to find the minimum value of cost function J, such that the values of θ is minimize on each iteration of gradient descent, hence decreasing the difference between predicted and actual values of the target variable.

    ![Gradient Descent]()

    The point of all this is that if we start with a guess for our hypothesis and then repeatedly apply these gradient descent equations, our hypothesis will become more and more accurate.
