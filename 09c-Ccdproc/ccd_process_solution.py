# The single line below does the bias subtraction,
# dark subtraction and flat correction for a single image.

stars_calibrated = ccdp.ccd_process(raw_stars,
                                    master_bias=bias,
                                    dark_frame=dark,
                                    exposure_key='exposure', exposure_unit=u.second,
                                    dark_scale=True,
                                    master_flat=flat)

plt.figure(figsize=(10,10))
im, _ = visualization.imshow_norm(stars_calibrated.data, 
                          interval=visualization.PercentileInterval(99), 
                          stretch=visualization.LinearStretch())
plt.colorbar(im);
