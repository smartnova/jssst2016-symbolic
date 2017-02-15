/// Creates a matrix for a symetric perspective-view frustum based on the default handedness.
/// 
/// @param fovy Specifies the field of view angle in the y direction. Expressed in radians.
/// @param aspect Specifies the aspect ratio that determines the field of view in the x direction. The aspect ratio is the ratio of x (width) to y (height).
/// @param near Specifies the distance from the viewer to the near clipping plane (always positive).
/// @param far Specifies the distance from the viewer to the far clipping plane (always positive).
/// @tparam T Value type used to build the matrix. Currently supported: half (not recommanded), float or double.
/// @see gtc_matrix_transform
template <typename T>
GLM_FUNC_DECL tmat4x4<T, defaultp> perspective(
        T fovy,
        T aspect,
        T near,
        T far);
