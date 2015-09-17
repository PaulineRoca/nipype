# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.cmtk.convert import MergeCNetworks

def test_MergeCNetworks_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_files=dict(mandatory=True,
    ),
    out_file=dict(usedefault=True,
    ),
    )
    inputs = MergeCNetworks.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_MergeCNetworks_outputs():
    output_map = dict(connectome_file=dict(),
    )
    outputs = MergeCNetworks.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
