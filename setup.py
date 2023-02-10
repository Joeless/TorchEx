from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='torchex',
    packages=find_packages(),
    version='0.1.0',
    author='Lve Fan',
    ext_modules=[
        CUDAExtension(
            'weighted_nms_ext', 
            ['./torchex/src/weighted_nms/wnms.cpp',
             './torchex/src/weighted_nms/wnms_kernel.cu',]
        ),
        CUDAExtension(
            'dynamic_point_pool_ext', 
            ['./torchex/src/dynamic_point_pool/dynamic_point_pool.cpp',
             './torchex/src/dynamic_point_pool/dynamic_point_pool_kernel.cu',]
        ),
        CUDAExtension(
            'sparse_roi_voxelization', 
            ['./torchex/src/sparse_roi_voxelization/sparse_roiaware_pool3d.cpp',
             './torchex/src/sparse_roi_voxelization/sparse_roiaware_pool3d_kernel.cu',]
        ),
        CUDAExtension(
            'ingroup_indices', 
            ['./torchex/src/ingroup_inds/ingroup_inds.cpp',
             './torchex/src/ingroup_inds/ingroup_inds_kernel.cu',]
        ),
        CUDAExtension(
            'connected_components_labeling',
            ['./torchex/src/connected_components/ccl.cpp',
             './torchex/src/connected_components/ccl_kernel.cu',]
        ),
        CUDAExtension(
            'group_fps_ext', 
            ['./torchex/src/group_fps/group_fps.cpp',
             './torchex/src/group_fps/group_fps_kernel.cu',]
        ),
        CUDAExtension(
            'scatter_ext',
            ['./torchex/src/scatter/scatter.cpp',
             './torchex/src/scatter/scatter_kernel.cu']
        ),
        CUDAExtension(
            'codec',
            ['./torchex/src/mask_codec/codec.cpp',
             './torchex/src/mask_codec/codec_kernel.cu']
        ),
        CUDAExtension(
            'iou3d_cuda',
            ['./torchex/src/iou3d/iou3d.cpp',
             './torchex/src/iou3d/iou3d_kernel.cu']
        ),
        CUDAExtension(
            'chamfer_distance_cuda',
            ["./torchex/src/chamfer_distance/chamfer_distance.cpp",
            "./torchex/src/chamfer_distance/chamfer_distance_kernel.cu"]
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)

