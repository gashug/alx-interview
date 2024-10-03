#!/usr/bin/python3

"""
Pascal's Triangle Generator Module

This module provides a function to generate Pascal's Triangle up to a specified number of rows
using an iterative approach.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list: A list of lists, where each inner list represents a row in Pascal's Triangle.
    """
    if n <= 0:
        # Return an empty list for non-positive input
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Iterate to build each subsequent row
    for _ in range(1, n):
        previous_row = triangle[-1]  # Get the last row from the triangle
        current_row = [1]  # Start the current row with 1

        # Generate intermediate values by summing adjacent elements from the previous row
        for i in range(1, len(previous_row)):
            current_value = previous_row[i - 1] + previous_row[i]
            current_row.append(current_value)

        current_row.append(1)  # End the current row with 1
        triangle.append(current_row)  # Add the current row to the triangle

    return triangle
