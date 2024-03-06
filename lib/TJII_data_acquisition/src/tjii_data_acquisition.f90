module TJII_data_acquisition

   implicit none
   integer :: status

contains
   subroutine f_lastshot(ndes, ierr)

      integer, external :: lastshot

      integer, intent(out) :: ndes, ierr

      status = lastshot(ndes, ierr)

   end subroutine f_lastshot


   subroutine f_fecha(ndes, tmp, ierr)

      integer, external :: fecha

      integer, intent(in)                :: ndes
      integer, intent(out), dimension(5) :: tmp
      integer, intent(out)               :: ierr
      integer                            :: ano, mes, dia, hora, minuto

      status = fecha(ndes, dia, mes, ano, hora, minuto, ierr)
      tmp = [ano, mes, dia, hora, minuto]

   end subroutine f_fecha


   subroutine f_dimenp(ndes, senal, nper, npunt, ierr)

      integer, external :: dimenp

      character*32, intent(in) :: senal
      integer, intent(in)      :: ndes
      integer, intent(out)     :: ierr, nper, npunt

      status = dimenp(ndes, senal, nper, npunt, ierr)

   end subroutine f_dimenp


   subroutine f_dimens(ndes, senal, ndat, nvent, ierr)

      integer, external :: dimens

      character*32, intent(in) :: senal
      integer, intent(in)      :: ndes
      integer, intent(out)     :: ierr, ndat, nvent

      status = dimens(ndes, senal, ndat, nvent, ierr)

   end subroutine f_dimens


   subroutine f_ertxt(ncode)

      integer, external :: ertxt

      integer, intent(in) :: ncode

      status = ertxt(ncode)

   end subroutine f_ertxt


   subroutine f_getq(ndes, senal, idx, ierr)
      integer, external :: getq

      character*32, intent(in) :: senal
      integer, intent(in)      :: ndes
      integer, intent(out)     :: ierr, idx

      status = getq(ndes, senal, idx, ierr)


   end subroutine f_getq


   subroutine f_lectur(ndes, senal, ndat, nvent, x, y, ierr)

      integer, external :: lectur

      character*32, intent(in)   :: senal
      integer,      intent(in)   :: ndes, ndat, nvent
      real,         intent(out)  :: x(ndat), y(ndat)
      integer,      intent(out)  :: ierr

      integer              :: code, nbits, ndimv, ndimx, ndimy, mv(nvent)
      real                 :: factor, offsets, vpp, ymax, ymin, per(nvent), tini(nvent)
      character*32         :: unidad

      ndimx = ndat
      ndimy = ndat
      ndimv = nvent

      status = lectur(ndes, senal, ndimx, ndimy, ndimv, x, y, &
         ndat, nvent, mv, per, tini, nbits, offsets, ymax,   &
         ymin, factor, vpp, code, unidad, ierr)

   end subroutine f_lectur


   subroutine f_leep(ndes, senal, nnper, nnpunt, t, r, y, ierr)

      integer, external :: leep

      integer, intent(in)      :: ndes, nnpunt, nnper
      character*32, intent(in) :: senal
      integer, intent(out)     :: ierr
      real, intent(out)        :: r(nnpunt,nnper), y(nnpunt,nnper), t(nnper)

      character*32 :: unidx, unidy

      integer magnx, magny, nperf, npunt(nnper)

      real factx, facty

      status = leep(ndes, senal, nnpunt, nnper, r, y, nperf, npunt, t, &
         factx, unidx, magnx, facty, unidy, magny, ierr)

   end subroutine f_leep


   subroutine f_nums(ndes, nsen, ierr)

      integer, external :: nums

      integer, intent(in)  :: ndes
      integer, intent(out) :: nsen, ierr

      status = nums(ndes, nsen, ierr)

   end subroutine f_nums


   subroutine f_listas(ndes, nums, lista, ierr)

      integer, external :: listas

      integer, intent(in)       :: ndes, nums
      integer, intent(out)      :: ierr
      character*24, intent(out) :: lista(nums)

      integer :: nsr

      status = listas(ndes, nums, nsr, lista, ierr)

   end subroutine f_listas


   subroutine f_numshots(ano, mes, dia, nshots, ierr)

      integer, external :: numshots

      integer, intent(in)  :: ano, mes, dia
      integer, intent(out) :: ierr, nshots

      status = numshots(ano, mes, dia, nshots, ierr)

   end subroutine f_numshots


   subroutine f_paramn(ndes, senal, np, ierr)

      integer, external :: paramn

      integer, intent(in)  :: ndes
      integer, intent(out) :: np, ierr

      character*32, intent(in) :: senal

      status = paramn(ndes, senal, np, ierr)

   end subroutine f_paramn


   subroutine f_params(ndes, senal, ndimp, prmtos, values, ierr)

      integer, external :: params

      integer, intent(in)       :: ndes, ndimp
      integer, intent(out)      :: ierr
      character*32, intent(in)  :: senal
      character*16, intent(out) :: prmtos(ndimp)
!~ 	character, intent(out) :: prmtos(112)
      real, intent(out)         :: values(ndimp)

      integer ndimvl, np
      ndimvl = ndimp

      status = params(ndes, senal, ndimp, ndimvl, prmtos, values, np, ierr)
      print *, prmtos

   end subroutine f_params


   subroutine f_sigtype(senal, tipo, ierr)

      integer, external :: sigtype

      character*32, intent(in) :: senal
      integer, intent(out)     :: tipo, ierr

      status = sigtype(senal, tipo, ierr)

   end subroutine f_sigtype


   subroutine f_shotlist(ano, mes, dia, ndim, shots, ierr)

      integer, external :: shotlist

      integer, intent(in)  :: ano, mes, dia, ndim
      integer, intent(out) :: shots(ndim), ierr
      integer nshots

      status = shotlist(ano, mes, dia, ndim, nshots, shots, ierr)

   end subroutine f_shotlist


   subroutine f_lectc(ndes, senal, ndat, nvent, x, y, ierr)

      integer, external :: lectc

      character*32, intent(in)   :: senal
      integer,      intent(in)   :: ndes, ndat, nvent
      real,         intent(out)  :: x(ndat)
      integer,      intent(out)  :: ierr, y(ndat)

      integer              :: code, nbits, ndimv, ndimx, ndimy, mv(nvent), ymax, ymin, offsets
      real                 :: factor, vpp, per(nvent), tini(nvent)
      character*32         :: unidad

   end subroutine f_lectc

end module TJII_data_acquisition
