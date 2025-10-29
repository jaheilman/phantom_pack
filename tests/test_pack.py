
import numpy as np
from pack_simulators import simulate_phantom_pack
from phantompack.phantom_pack import find_packs_in_images, composite_statistics
from phantompack.pack_dimensions import PhantomPackDimensions, PhantomPackTolerances, PhantomPackAnalysis


if __name__ == "__main__":
    fw_series = simulate_phantom_pack()

    # display a few images to be sure
    display_slice = len(fw_series.image_pairs) // 2
    # plot_utils.display_image(fw_series.image_pairs[display_slice].pdff_img, "PDFF, midpoint")
    # plot_utils.display_image(fw_series.image_pairs[display_slice].water_img, "Water, midpoint")

    pack_dims = PhantomPackDimensions() #oddity - I don't know the pixel size yet
    pack_tols = PhantomPackTolerances()
    pack_anyl = PhantomPackAnalysis()

    find_packs_in_images(fw_series, pack_dims, pack_tols)
    fw_series.create_rois(pack_anyl.roi_radius_px())
    fw_series.pack_midpoint = fw_series.find_pack_midpoint()
    start_slice_loc = fw_series.pack_midpoint - pack_anyl.span/2
    end_slice_loc   = fw_series.pack_midpoint + pack_anyl.span/2
    dict_results = composite_statistics(fw_series, start_slice_loc, end_slice_loc)

    x=1