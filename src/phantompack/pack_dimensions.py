

class PhantomPackDimensions:
    def __init__(self,
                 pixel_size_mm = 1.0):
        
        self.pixel_size = pixel_size_mm
        # Constant pack dimensions (mm)
        self.vial_radius = 19.0/2
        self.vial_center_spacing = 31.0
        self.vial_length = 100.0
        self.vial_count = 5

    def to_px(self, value_mm:float):
        return round(value_mm / self.pixel_size)

    def radius_px(self):
        return round(self.vial_radius / self.pixel_size)
    
    def center_spacing_px(self):
        return round(self.vial_center_spacing / self.pixel_size)
    
    def length_px(self):
        return round(self.vial_length / self.pixel_size)
    
class PhantomPackTolerances:
    def __init__(self,
                 pixel_size_mm = 1.0):
        
        # all dimensions are in mm
        self.pixel_size = pixel_size_mm
        self.center_spacing = 3.0
        self.radius = 3.0
        self.length = 20.0
        self.vertical_align = 7.0

    
    def to_px(self, value_mm:float):
        return round(value_mm / self.pixel_size)
    
    def radius_px(self):
        return round(self.radius / self.pixel_size)
    
    def center_spacing_px(self):
        return round(self.center_spacing / self.pixel_size)
    
    def length_px(self):
        return round(self.length / self.pixel_size)
    
    def vertical_align_px(self):
        return round(self.vertical_align / self.pixel_size)

class PhantomPackAnalysis:
    def __init__(self,
                 pixel_size_mm = 1.0):
        self.pixel_size = pixel_size_mm
        self.center:float|None = None   # centerpoint, or None to discoover center
        self.span = 20.0                # analyze a range of images centered at the midpoint
        self.roi_radius = 13.0/2
        self.output_dir = "phantompack_results"

    def to_px(self, value_mm:float):
        return round(value_mm / self.pixel_size)
    
    def span_px(self):
        return round(self.span / self.pixel_size)
    
    def roi_radius_px(self):
        return round(self.roi_radius / self.pixel_size)


