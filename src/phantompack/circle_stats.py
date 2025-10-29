
# def slice_stats(img:ImagePair) -> dict:
#     # Compute the mean, median, and standard dev of a pdff/water pair.
#     # img should be a single slice of the img_pack_data, with pdff, water and rois
#     # Output: pdff_means:[], pdff_stddevs:[], pdff_medians:[] - lists of mean, stddev, median
#     # for the circles
#     stats = {}
#     # default values are -10
#     if img.has_rois() is False:
#         stats["pdff_means"] = [-10]*5 # HACK - fixed for 5 ROIs
#         stats["pdff_medians"] = [-10]*5
#         stats["pdff_stddevs"] = [0]*5
#         return stats
#     # apply rois to PDFF
#     pdff_means = []
#     pdff_medians = []
#     pdff_stddevs = []
#     for r in img.rois:
#         # make a circle mask that can be applied to pdff
#         mask = np.zeros(img.pdff.pixel_array.shape, dtype=np.uint8)
#         cv2.circle(mask, (r[CX], r[CY]), r[CR], color=1, thickness=-1) # solid circle (thickness = -1) filled with  1
#         # calculate mean and median
#         mean_pdff   = masked_mean(  img.pdff.pixel_array, mask)
#         median_pdff = masked_median(img.pdff.pixel_array, mask)
#         stddev_pdff = masked_stddev(img.pdff.pixel_array, mask)
#         pdff_means.append(mean_pdff)
#         pdff_medians.append(median_pdff)
#         pdff_stddevs.append(stddev_pdff)
#     stats["pdff_means"] = pdff_means
#     stats["pdff_medians"] = pdff_medians
#     stats["pdff_stddevs"] = pdff_stddevs
#     return stats
