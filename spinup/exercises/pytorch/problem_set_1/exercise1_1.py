import numpy as np
import torch

"""

Exercise 1.1: Diagonal Gaussian Likelihood

Write a function that takes in PyTorch Tensors for the means and 
log stds of a batch of diagonal Gaussian distributions, along with a 
PyTorch Tensor for (previously-generated) samples from those 
distributions, and returns a Tensor containing the log 
likelihoods of those samples.

"""


def gaussian_likelihood(x, mu, log_std):
    """
    Args:
        x: Tensor with shape [batch, dim]
        mu: Tensor with shape [batch, dim]
        log_std: Tensor with shape [batch, dim] or [dim]

    Returns:
        Tensor with shape [batch]
    """
    #######################
    #                     #
    #   YOUR CODE HERE    #

    # Note: the spinningup solution is a bit more efficient (fewer sum/square operations)
    # Also they include a small epsilon to avoid numerical instability
    # Note: inputs from exercise1_2 don't have a batch dimension
    # The spinningup solution is robust to this, so definitely use that in future
    if len(x.shape) == 1:
        dim = x.shape[0]
        dim_element = 0
    else:
        batch, dim = x.shape
        dim_element = 1
    log_prob = -0.5 * (
        dim * np.log(2 * np.pi)  # constant term
        + 2 * log_std.sum()  # sum of log stds
        + ((x - mu) ** 2 / log_std.exp() ** 2).sum(dim=dim_element)  # sum of SqErr
    )

    #                     #
    #######################
    return log_prob


if __name__ == "__main__":
    """
    Run this file to verify your solution.
    """
    from spinup.exercises.common import print_result
    from spinup.exercises.pytorch.problem_set_1_solutions import exercise1_1_soln

    batch_size = 32
    dim = 10

    x = torch.rand(batch_size, dim)
    mu = torch.rand(batch_size, dim)
    log_std = torch.rand(dim)

    your_gaussian_likelihood = gaussian_likelihood(x, mu, log_std)
    true_gaussian_likelihood = exercise1_1_soln.gaussian_likelihood(x, mu, log_std)

    your_result = your_gaussian_likelihood.detach().numpy()
    true_result = true_gaussian_likelihood.detach().numpy()

    correct = np.allclose(your_result, true_result)
    print_result(correct)
