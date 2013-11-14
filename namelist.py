

class WRFConfig(object):

    def __init__(self,arw,max_dom):
        self.arw = arw
        self.max_dom = max_dom

    def physics(self):
        

    def time_control(self,start,end):

        self.run_seconds = (end-start).total_seconds()
        self.run_days = run_seconds/86400
        self.run_seconds = run_seconds-run_days*86400
        self.run_hours = run_seconds/3600
        self.run_seconds = run_seconds-run_hours*3600
        self.run_minutes = run_seconds/60
        self.run_seconds = run_seconds-run_minutes*60

        # -- only supporting one start-end pair TODO: set run to longest
        max_dom_fmt = '%d,'*self.max_dom
        self.start_year = max_dom_fmt%tuple([start.year]*self.max_dom)
        self.start_month = max_dom_fmt%tuple([start.month]*self.max_dom)
        self.start_day = max_dom_fmt%tuple([start.day]*self.max_dom)
        self.start_hour = max_dom_fmt%tuple([start.hour]*self.max_dom)
        self.start_minute = max_dom_fmt%tuple([start.minute]*self.max_dom)
        self.start_second = max_dom_fmt%tuple([start.second]*self.max_dom)
        #if self.nmm:
        #    self.tstart (max_dom)                    = 00,	; FOR NMM: starting hour of the forecast
        self.end_year = max_dom_fmt%tuple([end.year]*self.max_dom)
        self.end_month = max_dom_fmt%tuple([end.month]*self.max_dom)
        self.end_day = max_dom_fmt%tuple([end.day]*self.max_dom)
        self.end_hour = max_dom_fmt%tuple([end.hour]*self.max_dom)
        self.end_minute = max_dom_fmt%tuple([end.minute]*self.max_dom)
        self.end_second = max_dom_fmt%tuple([end.second]*self.max_dom)

        self.interval_seconds                    = 10800,	; time interval between incoming real data, which will be the interval

        input_from_file (max_dom)           = T,       ; whether nested run will have input files for domains other than 1
        fine_input_stream (max_dom)         = 0,       ; field selection from nest input for its initialization

        history_interval (max_dom)          = 60,  	; history output file interval in minutes
        frames_per_outfile (max_dom)        = 1, 	; number of output times per history output file, 

        restart                             = F,	; whether this run is a restart run
        cycling                             = F,       ; whether this run is a cycling run, if so, initializes look-up table for Thompson schemes only
        restart_interval		     = 1440,	; restart output file interval in minutes
        reset_simulation_start              = F,       ; whether to overwrite simulation_start_date with forecast start time

        io_form_history                     = 2,       ; 2 = netCDF 
        io_form_restart                     = 2,       ; 2 = netCDF 
        io_form_input                       = 2,       ; 2 = netCDF
        io_form_boundary                    = 2,       ; netCDF format; 4 PHD5 format; 5 GRIB1 format; 10 GRIB2 format; 11 pnetCDF format

        frames_per_emissfile                = 12,      ; number of times in each chemistry emission file.
        io_style_emiss                      = 1,       ; style to use for the chemistry emission files.

        debug_level                         = 0, 	; 50,100,200,300 values give increasing prints
        diag_print                          = 0, 	; print out time series of model diagnostics

        all_ic_times                        = .false., ; whether to write out wrfinput for all processing times
        adjust_output_times                 = .false., ; adjust output times to the nearest hour
        override_restart_timers             = .false., ; whether to change the alarms from what is previously set
        write_hist_at_0h_rst                = .false., ; whether to output history file at the start of restart run

        auxinput1_inname                    = "met_em.d<domain>.<date>"             ; Input to real from WPS (default since 3.0)/// "wrf_real_input_em.d<domain>.<date>"  ; Input to real from SI
        auxinput1_inname                    = "met_nm.d<domain>.<date>"             ; Input to real from WPS /// "wrf_real_input_nm.d<domain>.<date>"  ; Input to real from SI

        auxhist2_outname                    = "rainfall" ; file name for extra output; if not specified,
        auxhist2_interval (max_dom)         = 10,      ; interval in minutes
        io_form_auxhist2                    = 2,       ; output in netCDF
        frames_per_auxhist2                 = 1000,    ; number of output times in this file

        auxinput4_inname                    = "wrflowinp_d<domain>" 
        auxinput4_interval                  = 360      ; minutes generally matches time given by interval_seconds
        io_form_auxinput4                   = 2        ; IO format, required in V3.2

        nwp_diagnostics                     = 1        ; adds 7 history-interval max diagnostic fields


#For additional regional climate surface fields
#----------------------------------------------
        output_diagnostics                  = 1        ; adds 36 surface diagnostic arrays (max/min/mean/std)

        auxhist3_outname                    = 'wrfxtrm_d<domain>_<date>' ; file name for added diagnostics
        io_form_auxhist3                    = 2        ; netcdf
        auxhist3_interval                   = 1440     ; minutes between outputs (1440 gives daily max/min)
        frames_per_auxhist3                 = 1        ; output times per file

#For observation nudging
# ----------------------
        auxinput11_interval                 = 10       ; interval in minutes for observation data. It should be set as or more frequently as obs_ionf (with unit of coarse domain time step).
        auxinput11_end_h                    = 6        ; end of observation time in hours.

#Options for run-time IO:
# http://www.mmm.ucar.edu/wrf/OnLineTutorial/Class/cases/reg.htm
        iofields_filename (max_dom)         = "my_iofields_list.txt", (example: +:h:21:rainc, rainnc, rthcuten)
        ignore_iofields_warning             = .true.,  ; what to do when encountering an error in the user-specified files///.false., : abort when encountering an error in iofields_filename file

#Additional settings when running WRFVAR:
write_input                         = t,       ; write input-formatted data as output
inputout_interval                   = 180,     ; interval in minutes when writing input-formatted data 
input_outname                       = 'wrfinput_d<domain>_<date>' ; you may change the output file name
inputout_begin_y                    = 0
inputout_begin_mo                   = 0
inputout_begin_d                    = 0
inputout_begin_h                    = 3
inputout_begin_m                    = 0
inputout_begin_s                    = 0
inputout_end_y                      = 0
inputout_end_mo                     = 0
inputout_end_d                      = 0
inputout_end_h                      = 12
inputout_end_m                      = 0
inputout_end_s                      = 0        ; the above shows that the input-formatted data are output starting from hour 3 to hour 12 in 180 min interval.

# =======
# domains
# =======

    def domains(self):

        # Example, if you want to use 60.3 sec as your time step, set time_step = 60, time_step_fract_num = 3, and time_step_fract_den = 10
        time_step                           = 60,	; time step for integration in integer seconds///recommend 6*dx (in km) for typical real-data cases
        time_step_fract_num                 = 0,	; numerator for fractional time step 
        time_step_fract_den                 = 1,	; denominator for fractional time step 

        time_step_dfi                       = 60,	; time step for DFI, may be different from regular time_step

        max_dom                             = 1,	; number of domains - set it to > 1 if it is a nested run
        s_we (max_dom)                      = 1,	; start index in x (west-east) direction (leave as is)
        e_we (max_dom)                      = 91,	; end index in x (west-east) direction (staggered dimension)
        s_sn (max_dom)                      = 1,	; start index in y (south-north) direction (leave as is)
        e_sn (max_dom)                      = 82,	; end index in y (south-north) direction (staggered dimension)
        s_vert (max_dom)                    = 1,	; start index in z (vertical) direction (leave as is)
        e_vert (max_dom)                    = 30,	; end index in z (vertical) direction (staggered dimension)
                                                  Note: this refers to full levels including surface and top
                                                  vertical dimensions need to be the same for all nests
                                                  Note: most variables are unstaggered (= staggered dim - 1)
        dx (max_dom)                        = 10000,	; grid length in x direction; ARW: unit in meters, NMM: unit in degrees (e.g. 0.667)
        dy (max_dom)                        = 10000,	; grid length in y direction; ARW: unit in meters, NMM: unit in degrees (e.g. 0.0658) 

        ztop (max_dom)                      = 19000.	; used in mass model for idealized cases

        grid_id (max_dom)                   = 1,	; domain identifier
        parent_id (max_dom)                 = 0,       ; id of the parent domain
        i_parent_start (max_dom)            = 0,       ; starting LLC I-indices from the parent domain
        j_parent_start (max_dom)            = 0,       ; starting LLC J-indices from the parent domain
        parent_grid_ratio (max_dom)         = 1,       ; parent-to-nest domain grid size ratio: for real-data cases
                                                  the ratio has to be odd; for idealized cases,
                                                  the ratio can be even if feedback is set to 0. (NMM: must be 3)
        parent_time_step_ratio (max_dom)    = 1,       ; parent-to-nest time step ratio; it can be different
                                                 from the parent_grid_ratio (NMM: must be 3)
        feedback                            = 1,       ; feedback from nest to its parent domain; 0 = no feedback
        smooth_option                       = 0        ; smoothing option for parent domain, used only with feedback
                                                  option on. 0: no smoothing; 1: 1-2-1 smoothing; 2: smoothing-desmoothing

#Namelist variables specifically for the WPS input for real:

num_metgrid_soil_levels             = 4        ; number of vertical soil levels or layers input
                                                ; from WPS metgrid program
num_metgrid_levels                  = 27       ; number of vertical levels of 3d meteorological fields coming 
                                                ; from WPS metgrid program
interp_type                         = 2        ; vertical interpolation
                                                ; 1 = linear in pressure
                                                ; 2 = linear in log(pressure)
extrap_type                         = 2        ; vertical extrapolation of non-temperature fields
                                                ; 1 = extrapolate using the two lowest levels
                                                ; 2 = use lowest level as constant below ground
t_extrap_type                       = 2        ; vertical extrapolation for potential temperature
                                                ; 1 = isothermal
                                                ; 2 = -6.5 K/km lapse rate for temperature
                                                ; 3 = constant theta
use_levels_below_ground             = .true.   ; in vertical interpolation, use levels below input surface level
                                                ; T = use input isobaric levels below input surface
                                                ; F = extrapolate when WRF location is below input surface value
use_surface                         = .true.   ; use the input surface level data in the vertical interp and extrap
                                                ; T = use the input surface data
                                                ; F = do not use the input surface data
lagrange_order                      = 1        ; vertical interpolation order
                                                ; 1 = linear
                                                ; 2 = quadratic
zap_close_levels                    = 500      ; ignore isobaric level above surface if delta p (Pa) < zap_close_levels
lowest_lev_from_sfc                 = .false.  ; place the surface value into the lowest eta location
                                                ; T = use surface value as lowest eta (u,v,t,q)
                                                ; F = use traditional interpolation
force_sfc_in_vinterp                = 1        ; use the surface level as the lower boundary when interpolating
                                                ; through this many eta levels
                                                ; 0 = perform traditional trapping interpolation
                                                ; n = first n eta levels directly use surface level
sfcp_to_sfcp                        = .false.  ; Optional method to compute model's surface pressure when incoming
                                                ; data only has surface pressure and terrain, but not SLP
smooth_cg_topo	                     = .false.  ; Smooth the outer rows and columns of domain 1's topography w.r.t.
                                                ; the input data
use_tavg_for_tsk                    = .false.  ; whether to use diurnally averaged surface temp as skin temp. The 
                                                  diurnall averaged surface temp can be computed using WPS utility
                                                  avg_tsfc.exe. May use this option when SKINTEMP is not present.
aggregate_lu                        = .false.  ; whetger to aggregate the grass, shrubs, trees in dominant landuse;
                                                 default is false.
rh2qv_wrt_liquid                    = .true.,  ; whether to compute RH with respect to water (true) or ice (false)
rh2qv_method                        = 1,       ; which methed to use to computer mixing ratio from RH:
                                                  default is option 1, the old MM5 method; option 2 uses a WMO 
                                                  recommended method (WMO-No. 49, corrigendum, August 2000) - 
                                                  there is a difference between the two methods though small
interp_theta                        = .true.   ; If set to .false., it will vertically interpolate temperature 
                                                  instead of potential temperature, which may reduce bias when 
                                                  compared with input data
hypsometric_opt                     = 1,       ; = 1: default method
                                                  = 2: it uses an alternative way (less biased 
                                                  when compared agaist input data) to compute height in program 
                                                  real and pressure in model (ARW only). 
p_top_requested                     = 5000     ; p_top (Pa) to use in the model
ptsgm                               = 42000.   ; FOR NMM:  defines the pressure interface dividing
                                                ;           the terrain following portion of the hybrid vertical
                                                ;           coordinate (p > ptsgm) and the purely
                                                ;           isobaric portion of the vertical coordinate (p < ptsgm)
vert_refine_fact                    = 1        ; vertical refinement factor for ndown

#Users may explicitly define full eta levels.  Given are two distributions for 28 and 35 levels.  The number of levels must agree with the number of eta surfaces allocated (e_vert).
#Users may alternatively request only the number of levels (with e_vert), and the real program will compute values.  The computation assumes a known first several layers, then generates equi-height spaced levels up to the top of the model.
eta_levels                          = 1.000, 0.990, 0.978, 0.964, 0.946,
                                      0.922, 0.894, 0.860, 0.817, 0.766,
                                      0.707, 0.644, 0.576, 0.507, 0.444,
                                      0.380, 0.324, 0.273, 0.228, 0.188,
                                      0.152, 0.121, 0.093, 0.069, 0.048,
                                      0.029, 0.014, 0.000,
eta_levels                          = 1.000, 0.993, 0.983, 0.970, 0.954,
                                      0.934, 0.909, 0.880, 0.845, 0.807,
                                      0.765, 0.719, 0.672, 0.622, 0.571,
                                      0.520, 0.468, 0.420, 0.376, 0.335,
                                      0.298, 0.263, 0.231, 0.202, 0.175,
                                      0.150, 0.127, 0.106, 0.088, 0.070,
                                      0.055, 0.040, 0.026, 0.013, 0.000

Variables specifically for the 3d ocean initialization with a single profile. Set
the ocean physics option to #2.  Specify a number of levels.  For each of those levels,
provide a depth (m) below the surface.  At each depth provide a temperature (K) and
a salinity (ppt).  The default is not to use the 3d ocean.  Even when the 3d ocean is
activated, the user must specify a reasonable ocean.  Currently, this is the only way
available to run the 3d ocean option.

 &physics
 sf_ocean_physics                    = 0 (default), 1 (mixed layer model), 2 (3d ocean)

 &domains
 ocean_levels                        = 30,
 ocean_z                             =        5,        15,        25,        35,        45,        55,
                                             65,        75,        85,        95,       105,       115,
                                            125,       135,       145,       155,       165,       175,
                                            185,       195,       210,       230,       250,       270,
                                            290,       310,       330,       350,       370,       390
 ocean_t                             = 302.3493,  302.3493,  302.3493,  302.1055,  301.9763,  301.6818,
                                       301.2220,  300.7531,  300.1200,  299.4778,  298.7443,  297.9194,
                                       297.0883,  296.1443,  295.1941,  294.1979,  293.1558,  292.1136,
                                       291.0714,  290.0293,  288.7377,  287.1967,  285.6557,  284.8503,
                                       284.0450,  283.4316,  283.0102,  282.5888,  282.1674,  281.7461
 ocean_s                             =  34.0127,   34.0127,   34.0127,   34.3217,   34.2624,   34.2632,
                                        34.3240,   34.3824,   34.3980,   34.4113,   34.4220,   34.4303,
                                        34.6173,   34.6409,   34.6535,   34.6550,   34.6565,   34.6527,
                                        34.6490,   34.6446,   34.6396,   34.6347,   34.6297,   34.6247,
                                        34.6490,   34.6446,   34.6396,   34.6347,   34.6297,   34.6247

#Namelist variables for controling the specified moving nest: 
                   Note that this moving nest option needs to be activated at the compile time by adding -DMOVE_NESTS
                   to the ARCHFLAGS. The maximum number of moves, max_moves, is set to 50 
                   but can be modified in source code file frame/module_driver_constants.F.
 num_moves                           = 4        ; total number of moves
 move_id(max_moves)                  = 2,2,2,2, ; a list of nest domain id's, one per move
 move_interval(max_moves)            = 60,120,150,180,   ; time in minutes since the start of this domain
 move_cd_x(max_moves)                = 1,1,0,-1,; the number of parent domain grid cells to move in i direction
 move_cd_y(max_moves)                = 1,0,-1,1,; the number of parent domain grid cells to move in j direction
                                                  positive is to move in increasing i and j direction, and 
                                                  negative is to move in decreasing i and j direction.
                                                  0 means no move. The limitation now is to move only 1 grid cell
                                                  at each move.

Namelist variables for controling the automatic moving nest: 
                   Note that this moving nest option needs to be activated at the compile time by adding -DMOVE_NESTS
                   and -DVORTEX_CENTER to the ARCHFLAGS. This option uses an mid-level vortex following algorthm to
                   determine the nest move. This option is experimental.
 vortex_interval(max_dom)            = 15       ; how often the new vortex position is computed
 max_vortex_speed(max_dom)           = 40       ; used to compute the search radius for the new vortex position
 corral_dist(max_dom)                = 8        ; how many coarse grid cells the moving nest is allowed to get
                                                  near the mother domain boundary
 track_level                         = 50000    ; pressure value in Pa where the vortex is tracked
 time_to_move(max_dom)               = 0.       ; time (in minutes) to start the moving nests     

 tile_sz_x                           = 0,       ; number of points in tile x direction
 tile_sz_y                           = 0,       ; number of points in tile y direction
                                                  can be determined automatically
 numtiles                            = 1,       ; number of tiles per patch (alternative to above two items)
 nproc_x                             = -1,      ; number of processors in x for decomposition
 nproc_y                             = -1,      ; number of processors in y for decomposition
                                                  -1: code will do automatic decomposition
                                                  >1: for both: will be used for decomposition

Namelist variables for controlling the adaptive time step option: These options are only valid for the ARW core.  
 use_adaptive_time_step              = .false.  ; T/F use adaptive time stepping, ARW only
 step_to_output_time                 = .true.   ; if adaptive time stepping, T/F modify the
                                                  time steps so that the exact history time is reached
 target_cfl(max_dom)                 = 1.2,1.2  ; vertical and horizontal CFL <= to this value implies
                                                  no reason to reduce the time step, and to increase it
 target_hcfl(max_dom)                = .84,.84  ; horizontal CFL <= to this value implies
 max_step_increase_pct(max_dom)      = 5,51     ; percentage of previous time step to increase, if the
                                                  max(vert cfl, horiz cfl) <= target_cfl, then the time
                                                  will increase by max_step_increase_pct. Use something 
                                                  large for nests (51% suggested)
 starting_time_step(max_dom)         = -1,-1    ; flag = -1 implies use 6 * dx (defined in start_em), 
                                                  starting_time_step = 100 means the starting time step
                                                  for the coarse grid is 100 s
 max_time_step(max_dom)              = -1,-1    ; flag = -1 implies max time step is 3 * starting_time_step,
                                                  max_time_step = 100 means that the time step will not
                                                  exceed 100 s
 min_time_step(max_dom)              = -1,-1    ; flag = -1 implies max time step is 0.5 * starting_time_step,
                                                  min_time_step = 100 means that the time step will not
                                                  be less than 100 s
 adaptation_domain                   = 1        ; default, all fine grid domains adaptive dt driven by coarse-grid
                                                ; 2 = Fine grid domain #2 determines the fundamental adaptive dt.

# ===
# DFI
# ===
    def dfi_control(self):
dfi_opt                             = 0        ; which DFI option to use (3 is recommended)
                                                ;   0 = no digital filter initialization
                                                ;   1 = digital filter launch (DFL)
                                                ;   2 = diabatic DFI (DDFI)
                                                ;   3 = twice DFI (TDFI)
dfi_nfilter                         = 7        ; digital filter type to use (7 is recommended)
                                                ;   0 = uniform
                                                ;   1 = Lanczos
                                                ;   2 = Hamming
                                                ;   3 = Blackman
                                                ;   4 = Kaiser
                                                ;   5 = Potter
                                                ;   6 = Dolph window
                                                ;   7 = Dolph
                                                ;   8 = recursive high-order
dfi_write_filtered_input            = .true.   ; whether to write wrfinput file with filtered 
                                                ;   model state before beginning forecast
dfi_write_dfi_history               = .false.  ; whether to write wrfout files during filtering integration
dfi_cutoff_seconds                  = 3600     ; cutoff period, in seconds, for the filter
dfi_time_dim                        = 1000     ; maximum number of time steps for filtering period
                                                ;   this value can be larger than necessary
dfi_bckstop_year                    = 2004     ; four-digit year of stop time for backward DFI integration
dfi_bckstop_month                   = 03       ; two-digit month of stop time for backward DFI integration
dfi_bckstop_day                     = 14       ; two-digit day of stop time for backward DFI integration
dfi_bckstop_hour                    = 12       ; two-digit hour of stop time for backward DFI integration
dfi_bckstop_minute                  = 00       ; two-digit minute of stop time for backward DFI integration
dfi_bckstop_second                  = 00       ; two-digit second of stop time for backward DFI integration
dfi_fwdstop_year                    = 2004     ; four-digit year of stop time for forward DFI integration
dfi_fwdstop_month                   = 03       ; two-digit month of stop time for forward DFI integration
dfi_fwdstop_day                     = 13       ; two-digit month of stop time for forward DFI integration
dfi_fwdstop_hour                    = 12       ; two-digit month of stop time for forward DFI integration
dfi_fwdstop_minute                  = 00       ; two-digit month of stop time for forward DFI integration
dfi_fwdstop_second                  = 00       ; two-digit month of stop time for forward DFI integration
dfi_radar                           = 0        ; DFI radar da switch
