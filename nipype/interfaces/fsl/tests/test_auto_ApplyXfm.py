# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.preprocess import ApplyXfm

def test_ApplyXfm_inputs():
    input_map = dict(angle_rep=dict(argstr='-anglerep %s',
    ),
    apply_isoxfm=dict(argstr='-applyisoxfm %f',
    xor=['apply_xfm'],
    ),
    apply_xfm=dict(argstr='-applyxfm',
    requires=['in_matrix_file'],
    usedefault=True,
    ),
    args=dict(argstr='%s',
    ),
    bbrslope=dict(argstr='-bbrslope %f',
    min_ver='5.0.0',
    ),
    bbrtype=dict(argstr='-bbrtype %s',
    min_ver='5.0.0',
    ),
    bgvalue=dict(argstr='-setbackground %f',
    ),
    bins=dict(argstr='-bins %d',
    ),
    coarse_search=dict(argstr='-coarsesearch %d',
    units='degrees',
    ),
    cost=dict(argstr='-cost %s',
    ),
    cost_func=dict(argstr='-searchcost %s',
    ),
    datatype=dict(argstr='-datatype %s',
    ),
    display_init=dict(argstr='-displayinit',
    ),
    dof=dict(argstr='-dof %d',
    ),
    echospacing=dict(argstr='-echospacing %f',
    min_ver='5.0.0',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fieldmap=dict(argstr='-fieldmap %s',
    min_ver='5.0.0',
    ),
    fieldmapmask=dict(argstr='-fieldmapmask %s',
    min_ver='5.0.0',
    ),
    fine_search=dict(argstr='-finesearch %d',
    units='degrees',
    ),
    force_scaling=dict(argstr='-forcescaling',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-in %s',
    mandatory=True,
    position=0,
    ),
    in_matrix_file=dict(argstr='-init %s',
    ),
    in_weight=dict(argstr='-inweight %s',
    ),
    interp=dict(argstr='-interp %s',
    ),
    min_sampling=dict(argstr='-minsampling %f',
    units='mm',
    ),
    no_clamp=dict(argstr='-noclamp',
    ),
    no_resample=dict(argstr='-noresample',
    ),
    no_resample_blur=dict(argstr='-noresampblur',
    ),
    no_search=dict(argstr='-nosearch',
    ),
    out_file=dict(argstr='-out %s',
    hash_files=False,
    name_source=['in_file'],
    name_template='%s_flirt',
    position=2,
    ),
    out_log=dict(keep_extension=True,
    name_source=['in_file'],
    name_template='%s_flirt.log',
    requires=['save_log'],
    ),
    out_matrix_file=dict(argstr='-omat %s',
    hash_files=False,
    keep_extension=True,
    name_source=['in_file'],
    name_template='%s_flirt.mat',
    position=3,
    ),
    output_type=dict(),
    padding_size=dict(argstr='-paddingsize %d',
    units='voxels',
    ),
    pedir=dict(argstr='-pedir %d',
    min_ver='5.0.0',
    ),
    ref_weight=dict(argstr='-refweight %s',
    ),
    reference=dict(argstr='-ref %s',
    mandatory=True,
    position=1,
    ),
    rigid2D=dict(argstr='-2D',
    ),
    save_log=dict(),
    schedule=dict(argstr='-schedule %s',
    ),
    searchr_x=dict(argstr='-searchrx %s',
    units='degrees',
    ),
    searchr_y=dict(argstr='-searchry %s',
    units='degrees',
    ),
    searchr_z=dict(argstr='-searchrz %s',
    units='degrees',
    ),
    sinc_width=dict(argstr='-sincwidth %d',
    units='voxels',
    ),
    sinc_window=dict(argstr='-sincwindow %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    uses_qform=dict(argstr='-usesqform',
    ),
    verbose=dict(argstr='-verbose %d',
    ),
    wm_seg=dict(argstr='-wmseg %s',
    min_ver='5.0.0',
    ),
    wmcoords=dict(argstr='-wmcoords %s',
    min_ver='5.0.0',
    ),
    wmnorms=dict(argstr='-wmnorms %s',
    min_ver='5.0.0',
    ),
    )
    inputs = ApplyXfm.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ApplyXfm_outputs():
    output_map = dict(out_file=dict(),
    out_log=dict(),
    out_matrix_file=dict(),
    )
    outputs = ApplyXfm.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
