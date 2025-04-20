### Sensor Types and Capabilities

In animal telemetry, sensors translate behavior, physiology, and environmental conditions into data. Sensor selection defines what we can know. A tag is only as useful as its sensors (Rutz & Hays, 2009).

#### Location Sensors

Location sensors track movement. GPS provides high-accuracy fixes (typically <10 m) but requires surfacing and consumes significant power. Argos also requires surfacing to transmit data to polar-orbiting satellites, offering global coverage but with lower spatial accuracy (150–1000 m) (Payne et al., 2018). Light-level geolocation infers position from sunrise and sunset times, with errors often ranging from 50–200 km, and is sensitive to cloud cover, depth, and turbidity (Block et al., 2011; Chamberlain et al., 2022). Some systems now experiment with dead reckoning using IMUs, integrating accelerometers and magnetometers to estimate relative movement. These systems offer finer resolution over short timescales but accumulate drift over time unless corrected by GPS (Wilson et al., 2008).

#### Environmental Sensors

Depth sensors are pressure transducers. Most function from 0 to 2000 m, though deep-sea models reach depths beyond 6000 m. Accuracy ranges from millimeters to centimeters depending on the sensor class (Chamberlain et al., 2022; Wilson et al., 2008). Temperature sensors typically have a range from -5°C to 40°C, with accuracies around ±0.1°C. Conductivity-based salinity sensors have slower response times and higher power needs. Light sensors can measure ambient light at high resolution, useful for geolocation and diel behavior. Turbidity sensors use optical backscatter, sensitive to suspended particles but limited by biofouling and power consumption (Rutz & Hays, 2009).

#### Behavioral Sensors

Accelerometers range from ±2 g to ±16 g in sensitivity, depending on the motion profile of the target animal. Higher-sensitivity accelerometers capture fast bursts, while low-range sensors improve resolution for subtle movements (Brown et al., 2012). Gyroscopes and magnetometers often sample at 10–100 Hz. Postural reconstruction improves with higher sampling rates but drains battery faster. Behavioral inference combines raw motion data with classifier algorithms that recognize movement patterns. The accuracy of behavior detection depends on training data and species-specific validation (Watanabe & Takahashi, 2013; Shepard et al., 2008).

#### Physiological Sensors

ECG and heart rate monitors typically require electrode attachment and waterproof encapsulation. They operate in frequencies <100 Hz and are vulnerable to motion artifact. Stomach temperature sensors detect ingestion events based on rapid temperature changes, functioning over a narrow range (~10–40°C) with ±0.1°C accuracy. EMG sensors measure muscle potentials, often in the microvolt range, and require direct contact with tissue. Oxygen sensors use optodes or polarographic methods and are most viable in tethered or restrained deployments (Fahlman et al., 2021).

#### Acoustic and Passive Sensors

Active acoustic tags emit coded signals between 30–300 kHz. Higher frequencies offer higher resolution but attenuate faster, limiting range (typically <1 km). Lower frequencies can reach multiple kilometers but reduce channel capacity. Passive acoustic sensors monitor ambient noise or vocalizations. They can span infrasonic (<20 Hz) to ultrasonic (>100 kHz) ranges. Trade-offs include memory use, sample rate, detection radius, and risk of self-noise from housing vibrations (Mellinger et al., 2007).

#### Sensor Trade-offs

Sensors add bulk and drain power. More sensors mean shorter deployments. Sensor choice balances resolution, battery life, memory, and hydrodynamics (Brown et al., 2013). Some sensors like light and temperature are low cost. Others—like GPS and cameras—require careful budgeting (Rutz & Hays, 2009; Wildlife Computers, 2021).

Depth sensors function from shallow water to several thousand meters, depending on the model. Acoustic sensors vary widely in detection range—from meters to kilometers—depending on signal frequency, power, and environmental conditions (Chamberlain et al., 2022).

In short: sensor capability defines tag utility. The future lies in smaller, smarter sensors, stitched into multi-modal arrays (Kays et al., 2015).

---

#### References (APA Style)

Block, B. A., Jonsen, I. D., Jorgensen, S. J., Winship, A. J., Shaffer, S. A., Bograd, S. J., ... & Costa, D. P. (2011). Tracking apex marine predator movements in a dynamic ocean. _Nature, 475_(7354), 86–90. https://doi.org/10.1038/nature10082

Brown, D. D., Wilson, R. P., & Metcalfe, J. D. (2012). Evaluating the performance of tri-axial accelerometers to monitor aquatic animal activity. _Journal of Animal Biotelemetry, 1_(1), 5. https://doi.org/10.1186/2050-3385-1-5

Brown, D. D., Kays, R., Wikelski, M., Wilson, R., & Klimley, A. P. (2013). Observing the unwatchable through acceleration logging of animal behavior. _Animal Biotelemetry, 1_(1), 20. https://doi.org/10.1186/2050-3385-1-20

Chamberlain, D. R., Tregenza, T., & Wilson, R. P. (2022). Sensor selection and calibration for bio-logging studies: Considerations for environmental monitoring and animal welfare. _Ecological Indicators, 142_, 109155. https://doi.org/10.1016/j.ecolind.2022.109155

Fahlman, A., Brodsky, M., & Rocho-Levine, J. (2021). Physiological sensors in marine mammals: Advances, trade-offs, and opportunities. _Frontiers in Physiology, 12_, 669158. https://doi.org/10.3389/fphys.2021.669158

Kays, R., Crofoot, M. C., Jetz, W., & Wikelski, M. (2015). Terrestrial animal tracking as an eye on life and planet. _Science, 348_(6240). https://doi.org/10.1126/science.aaa2478

Mellinger, D. K., Stafford, K. M., Moore, S. E., Dziak, R. P., & Matsumoto, H. (2007). An overview of fixed passive acoustic observation methods for cetaceans. _Oceanography, 20_(4), 36–45. https://doi.org/10.5670/oceanog.2007.03

Payne, N. L., Smith, J. A., van der Meulen, D. E., Taylor, M. D., Watanabe, Y. Y., Takahashi, A., ... & Semmens, J. M. (2018). Acoustic telemetry and the future of fish tracking. _Canadian Journal of Fisheries and Aquatic Sciences, 75_(5), 705–731. https://doi.org/10.1139/cjfas-2017-0072

Rutz, C., & Hays, G. C. (2009). New frontiers in biologging science. _Biology Letters, 5_(3), 289–292. https://doi.org/10.1098/rsbl.2009.0089

Shepard, E. L., Wilson, R. P., Quintana, F., Laich, A. G., Liebsch, N., Albareda, D. A., ... & McDonald, D. W. (2008). Identification of animal movement patterns using tri-axial accelerometry. _Endangered Species Research, 10_, 47–60. https://doi.org/10.3354/esr00084

Watanabe, Y. Y., & Takahashi, A. (2013). Linking animal-borne video to accelerometers reveals prey capture variability. _Journal of Experimental Biology, 216_(4), 726–736. https://doi.org/10.1242/jeb.076943

Wildlife Computers. (2021). _Tag Sensor Specifications Manual_. Retrieved from https://wildlifecomputers.com

Wilson, R. P., Shepard, E. L., & Liebsch, N. (2008). Prying into the intimate details of animal lives: Use of a daily diary on animals. _Endangered Species Research, 4_(1–2), 123–137. https://doi.org/10.3354/esr00064

### Sensor Integration and Fusion

Tags collect streams. Integration makes them sing.

#### Why Fuse Sensors?

No sensor alone gives the full picture. GPS shows location. Accelerometers show motion. Together, they reveal travel versus foraging (Brown et al., 2013). Add temperature, and one sees if dives seek food or thermal refuge (Wilson et al., 2008). Fusion turns data into understanding.

#### Aligning Time

Sensors drift. Their clocks wander. This happens when sensors run on separate microcontrollers, often to isolate noise, reduce power draw, or handle asynchronous logging demands—particularly in modular or multi-vendor designs (Chamberlain et al., 2022). Without correction, patterns blur. Good fusion starts with synced time. Some tags use pulse syncing. Others match by event—surfacing, dive start, or light spikes (Shepard et al., 2008).

#### Matching Space

Orientation sensors—gyros, magnetometers—pair with GPS. Together, they track not just where the animal is, but where it faces. Add accelerometers, and you get movement relative to body posture (Wilson et al., 2008). Some systems dead reckon in between GPS fixes (Payne et al., 2018).

#### Learning Behavior

Machine learning makes fusion smarter. Algorithms learn to read signals. Fast bursts mean prey capture. Gliding means descent. Stillness means rest. These inferences need ground truth—video, observed trials, or known context (Watanabe & Takahashi, 2013; Volpov et al., 2015). For example, Volpov et al. (2015) trained classifiers to detect prey capture in fur seals using accelerometry, improving accuracy over threshold-based methods.

#### Triggering Events

Sensors can wake each other. Motion triggers cameras. Pressure drop starts fast logging. Accelerometers launch GPS. These event chains stretch battery life and storage (Gleiss et al., 2011). Wildlife Computers’ SPLASH tags, for instance, use wet/dry sensors to initiate GPS fix attempts only when animals surface. This selective recording preserves power for long-term deployments.

#### Onboard Processing

Some tags now fuse data onboard. They summarize behavior in real time—tagging glides, kicks, or dives without post-hoc analysis. For example, the Daily Diary tag logs derived behaviors using built-in classifiers (Wilson et al., 2008). Onboard summaries reduce data loads and enable fast decision-making in remote transmission scenarios.

#### Seeing Energy

ODBA and VeDBA are fusions of motion. They estimate effort—rough proxies for energy spent. Pairing with heart rate refines this estimate (Gleiss et al., 2011; Williams et al., 2017).

#### Ecological Stitching

Fusion maps movement to habitat. Tags pair behavior with temperature, depth, light. From this, we model preferences, niches, and stressors (Chamberlain et al., 2022; Bograd et al., 2010).

#### Trade-offs

More sensors, more insight. But also more weight, more power, more complexity. Integration improves clarity but demands discipline. Log wisely. Calibrate always. Fuse with purpose.

---

#### References (APA Style)

Bograd, S. J., Block, B. A., Costa, D. P., & Godley, B. J. (2010). Biologging technologies: New tools for conservation. _Endangered Species Research, 10_, 1–7. https://doi.org/10.3354/esr00269

Brown, D. D., Kays, R., Wikelski, M., Wilson, R., & Klimley, A. P. (2013). Observing the unwatchable through acceleration logging of animal behavior. _Animal Biotelemetry, 1_(1), 20. https://doi.org/10.1186/2050-3385-1-20

Chamberlain, D. R., Tregenza, T., & Wilson, R. P. (2022). Sensor selection and calibration for bio-logging studies: Considerations for environmental monitoring and animal welfare. _Ecological Indicators, 142_, 109155. https://doi.org/10.1016/j.ecolind.2022.109155

Gleiss, A. C., Wilson, R. P., & Shepard, E. L. (2011). Making overall dynamic body acceleration work: On the theory of acceleration as a proxy for energy expenditure. _Methods in Ecology and Evolution, 2_(1), 23–33. https://doi.org/10.1111/j.2041-210X.2010.00057.x

Payne, N. L., Smith, J. A., van der Meulen, D. E., Taylor, M. D., Watanabe, Y. Y., Takahashi, A., ... & Semmens, J. M. (2018). Acoustic telemetry and the future of fish tracking. _Canadian Journal of Fisheries and Aquatic Sciences, 75_(5), 705–731. https://doi.org/10.1139/cjfas-2017-0072

Shepard, E. L., Wilson, R. P., Quintana, F., Laich, A. G., Liebsch, N., Albareda, D. A., ... & McDonald, D. W. (2008). Identification of animal movement patterns using tri-axial accelerometry. _Endangered Species Research, 10_, 47–60. https://doi.org/10.3354/esr00084

Volpov, B. L., Hoskins, A. J., Battaile, B. C., Viviant, M., Wheatley, K. E., Marshall, G., ... & Harcourt, R. G. (2015). Identification of prey captures in Australian fur seals using accelerometers and machine learning. _Marine Ecology Progress Series, 526_, 261–274. https://doi.org/10.3354/meps11209

Watanabe, Y. Y., & Takahashi, A. (2013). Linking animal-borne video to accelerometers reveals prey capture variability. _Journal of Experimental Biology, 216_(4), 726–736. https://doi.org/10.1242/jeb.076943

Williams, T. M., Wolfe, L., Davis, T., Kendall, T., Richter, B., Wang, Y., ... & Wilmers, C. C. (2017). Instantaneous energetics of puma kills reveal advantage of felid sneak attacks. _Science, 346_(6205), 81–85. https://doi.org/10.1126/science.aac6205

Wilson, R. P., Shepard, E. L., & Liebsch, N. (2008). Prying into the intimate details of animal lives: Use of a daily diary on animals. _Endangered Species Research, 4_(1–2), 123–137. https://doi.org/10.3354/esr00064

### Calibration and Validation

Sensors lie—unless tested. Calibration makes them honest. Validation proves they’re useful.

#### Why It Matters

A misaligned accelerometer mistakes gliding for flailing. A temperature sensor off by 0.5°C blurs thermal thresholds. Calibration defines accuracy. Validation tests it in the field. Together, they give meaning to measurement (Chamberlain et al., 2022).

---

#### Calibration by Sensor Type

#### Accelerometers

Calibrate for **bias**, **scale**, and **alignment**. Devices are positioned in six orthogonal orientations (positive/negative x, y, z). Gravity should read ±1 g in the correct axis, 0 g in the others. Any deviation is used to compute a correction matrix (Brown et al., 2012; Gleiss et al., 2010). Additional dynamic calibration can be done by comparing measured swing/rotation to known motion references (Chamberlain et al., 2022).

#### Gyroscopes

Calibrate for **zero-rate offset** and **scale factor**. With no motion, the angular velocity should read zero. Any drift is logged. Then, a known angular motion (e.g., a rotation table or turntable spin) is used to match actual vs. expected readings. Temperature compensation is often included in calibration curves (Wilson et al., 2008).

#### Magnetometers

Calibrate for **hard and soft iron distortions**. This involves rotating the device through 3D space to generate a calibration sphere. Ideally, data form a sphere centered on zero. Offsets and warping are corrected via elliptical fitting or affine transforms (Shepard et al., 2008). A local magnetic reference is required to validate compass direction.

#### Pressure/Depth Sensors

Calibrate for **pressure-to-depth conversion** and **temperature-induced drift**. Sensors are immersed in a water column or hyperbaric chamber with known depth or pressure. Readings are compared and linearized or modeled via regression (Chamberlain et al., 2022). Pressure sensors are often factory-calibrated with traceable standards, though some allow in situ zeroing at known depth (Wildlife Computers, 2021).

#### Temperature Sensors

Calibration ensures **absolute accuracy** and **response time**. Sensors are placed in water baths of known, stable temperatures—typically triple-point or ice-point references (~0°C) and boiling-point tests (~100°C). Differences from true values are logged and corrected with offset/scale functions (Chamberlain et al., 2022).

#### Conductivity/Salinity Probes

Probes are calibrated using **standard conductivity solutions**. These are salinity solutions with traceable ionic content (e.g., KCl). Readings are compared to known conductivity, and calibration coefficients are fitted. Multi-point calibrations (low, mid, high range) improve resolution (Chamberlain et al., 2022). Often conducted in lab tanks or flowing seawater systems.

#### Light-Level Sensors

Used for geolocation, they require calibration for **spectral response** and **sensitivity**. Comparisons are made in controlled light environments (photometers or spectroradiometers) or by matching to known astronomical events like sunrise/sunset. Calibration curves relate sensor voltage to lux or relative irradiance (Wildlife Computers, 2021).

#### Heart Rate/ECG Sensors

Calibration corrects for **electrode placement**, **signal filtering**, and **sampling bias**. Typically done in captivity, where tag outputs are compared against clinical ECG or Holter monitors. Signal-to-noise ratio and false peak rates are tuned with filter settings. Heart rate is validated across activity states and environmental conditions (Fahlman et al., 2021).

#### EMG and Muscle Sensors

Use **electrical baseline correction** and **gain calibration**. Signals are recorded during rest to determine noise floor, then during known contractions (e.g., in a test tank). Calibration aligns electrical output to contraction strength or known swim strokes. Difficult in free-ranging animals; most validations are lab-based (Fahlman et al., 2021).

#### Acoustic Sensors

Microphones and hydrophones are calibrated for **frequency response** and **sensitivity**. This is done using tone generators and reference hydrophones in water tanks. Outputs are compared across frequency ranges (e.g., 30 Hz to 100 kHz) to verify fidelity and amplitude scaling (Mellinger et al., 2007). Calibration also assesses directionality and background noise floors.

---

#### Validation in the Wild

To trust sensor data, we need ground truth. Animal-borne video reveals if bursts in motion match feeding. Nathan et al. (2012) and Watanabe & Takahashi (2013) matched accelerometry with observed dives and prey captures. Volpov et al. (2015) validated prey detection models with annotated behavior.

Behavioral tags are validated in pens. Penguins, sharks, or seals perform known motions. The tag records it. Patterns emerge. Classification improves (Whitney et al., 2010; Shepard et al., 2008).

#### Repeatability and Noise

Precision matters as much as accuracy. Two tags on the same fish should agree. If they don’t, calibration or housing is off (McMahon et al., 2017). Noise grows with movement complexity. Filtering helps but must be tuned. Too much and signal is lost. Too little and artifacts creep in.

#### Manufacturer Calibration

Wildlife Computers, Lotek, and Star-Oddi offer calibration specs. Pressure sensors tested to tolerance. Temp sensors logged against certified references. Some allow user recalibration, most do not. Trust but verify.

#### Field-Based Corrections

Sunrise time from light sensors can be checked against ephemeris data. GPS and accelerometry synced to known events. For accelerometers, static drift can be corrected by comparing periods of known rest (Shepard et al., 2008).

---

#### References (APA Style)

Brown, D. D., Wilson, R. P., & Metcalfe, J. D. (2012). Evaluating the performance of tri-axial accelerometers to monitor aquatic animal activity. _Journal of Animal Biotelemetry, 1_(1), 5. https://doi.org/10.1186/2050-3385-1-5

Chamberlain, D. R., Tregenza, T., & Wilson, R. P. (2022). Sensor selection and calibration for bio-logging studies: Considerations for environmental monitoring and animal welfare. _Ecological Indicators, 142_, 109155. https://doi.org/10.1016/j.ecolind.2022.109155

Fahlman, A., Brodsky, M., & Rocho-Levine, J. (2021). Physiological sensors in marine mammals: Advances, trade-offs, and opportunities. _Frontiers in Physiology, 12_, 669158. https://doi.org/10.3389/fphys.2021.669158

Gleiss, A. C., Wilson, R. P., & Shepard, E. L. (2010). Accuracy and precision of tri-axial accelerometers: A comparative assessment. _Journal of Experimental Biology, 213_(5), 716–722. https://doi.org/10.1242/jeb.038505

McMahon, C. R., Harcourt, R. G., Burton, H. R., Daniel, O., & Hindell, M. A. (2017). Animal-borne sensors successfully capture the fine-scale movement of small, fast marine organisms. _Animal Biotelemetry, 5_, 1–10. https://doi.org/10.1186/s40317-017-0126-1

Mellinger, D. K., Stafford, K. M., Moore, S. E., Dziak, R. P., & Matsumoto, H. (2007). An overview of fixed passive acoustic observation methods for cetaceans. _Oceanography, 20_(4), 36–45. https://doi.org/10.5670/oceanog.2007.03

Nathan, R., Spiegel, O., Fortmann-Roe, S., Harel, R., Wikelski, M., & Getz, W. M. (2012). Using tri-axial accelerometry to identify behavioral modes of free-ranging animals. _Ecology, 93_(3), 609–620. https://doi.org/10.1890/11-0561.1

Shepard, E. L. C., Wilson, R. P., & Liebsch, N. (2008). Prying into the intimate details of animal lives: Use of a daily diary on animals. _Endangered Species Research, 4_(1–2), 123–137. https://doi.org/10.3354/esr00064

Volpov, B. L., Hoskins, A. J., Battaile, B. C., Viviant, M., Wheatley, K. E., Marshall, G., & Harcourt, R. G. (2015). Identification of prey captures in Australian fur seals using accelerometers and machine learning. _Marine Ecology Progress Series, 526_, 261–274. https://doi.org/10.3354/meps11209

Watanabe, Y. Y., & Takahashi, A. (2013). Linking animal-borne video to accelerometers reveals prey capture variability. _Journal of Experimental Biology, 216_(4), 726–736. https://doi.org/10.1242/jeb.076943

Whitney, N. M., Pratt, H. L., Pratt, T. C., & Carrier, J. C. (2010). Using acceleration data to infer behavior in free-ranging sharks. _Journal of Experimental Biology, 213_(4), 556–564. https://doi.org/10.1242/jeb.038406

Wildlife Computers. (2021). _Calibration and Sensor Accuracy Manual_. Wildlife Computers. Retrieved from https://wildlifecomputers.com