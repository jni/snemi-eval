#!/usr/bin/env fiji
"""Compute the Rand Error between two segmentations.
"""
import argparse


def evaluate(gt, auto):
    """Run the main Fiji-based functionality.
    """
    from jython_imports import IJ, RandError
    impgt = IJ.openImage(gt)
    impauto = IJ.openImage(auto)
    fscore = RandError.adaptedRandIndexFScore3D(impgt, impauto)
    print(1.0 - fscore)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Compute Rand Error between two segmentations.")
    parser.add_argument('gt', help='The image containing the ground truth'
                                   'segmentation.')
    parser.add_argument('auto', help='The image containing the candidate'
                                     'segmentation.')

    args = parser.parse_args()
    evaluate(args.gt, args.auto)
