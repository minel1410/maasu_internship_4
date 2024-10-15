ENTRY(reset_handler)

/* Highest address of the user mode stack */
_estack = 0x20020000;    /* end of RAM */
/* Generate a link error if heap and stack don't fit into RAM */
_Min_Heap_Size = 0x800;      /* required amount of heap  */
_Min_Stack_Size = 0x1000; /* required amount of stack */

MEMORY
{
	FLASH (rx): ORIGIN = 0x08000000, LENGTH = 512K
	SRAM (rwx): ORIGIN = 0x20000000, LENGTH = 128K
}

SECTIONS
{
  .isr_vector (READONLY):
  {
    KEEP(*(.isr_vector))
  } >FLASH

  .text (READONLY):
  {
    . = ALIGN(4);
		
    *(.text*)
    *(.rodata*)
    KEEP(*(.init))
    KEEP(*(.fini))
    *(.eh_frame)
    *(.ARM.exidx)
		
    . = ALIGN(4);
    _etext = .;
    __end__ = .;
  } >FLASH

  _sidata = LOADADDR(.data);

  .data :
  {
    . = ALIGN(4);
    _sdata = .;
		
    *(.data*)
    KEEP(*(.init_array))
    KEEP(*(.fini_array))

    . = ALIGN(4);
    _edata = .;
  } >SRAM AT> FLASH

  /* Uninitialized data section */
  .bss :
  {
    . = ALIGN(4);
    _sbss = .;
    __bss_start__ = _sbss;

    *(.bss*)
    *(COMMON)
    . = ALIGN(4);
    _ebss = .;
    __bss_end__ = _ebss;
  } >SRAM

  __exidx_start = .;

  .ARM.exidx   : { *(.ARM.exidx* .gnu.linkonce.armexidx.*) } >SRAM

  __exidx_end = .;


  /* User_heap_stack section, used to check that there is enough RAM left */
  ._user_heap_stack :
  {
    . = ALIGN(8);
    PROVIDE ( end = . );
    PROVIDE ( _end = . );
    . = . + _Min_Heap_Size;
    . = . + _Min_Stack_Size;
    . = ALIGN(8);
  } >SRAM

  .comment :
  {
      *(.comment)
  } >FLASH

  .debug_line :
  {
      *(.debug_line)
  } >FLASH

  .debug_line_str :
  {
      *(.debug_line_str)
  } >FLASH

  .debug_info :
  {
      *(.debug_info)
  } >FLASH

  .debug_abbrev :
  {
      *(.debug_abbrev)
  } >FLASH

  .debug_arranges :
  {
      *(.debug_arranges)
  } >FLASH

  .debug_str :
  {
      *(.debug_str)
  } >FLASH

  .debug_loclists :
  {
      *(.debug_loclists)
  } >FLASH

  .debug_rnglists :
  {
      *(.debug_rnglists)
  } >FLASH

  .debug_frame :
  {
      *(.debug_frame)
  } >FLASH

  .ARM.attributes :
  {
      *(.ARM.attributes)
      KEEP(*(.ARM.attributes))
  } >FLASH
}