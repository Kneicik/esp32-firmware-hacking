void FUN_00011a14(undefined1 *param_1)

{
  uint uVar1;
  undefined4 uVar2;
  
  if (*(int *)(param_1 + 0xc) != 0) {
    do {
      while( true ) {
        uVar1 = FUN_0001267c();
        if (*(uint *)(param_1 + 0x14) <= uVar1) break;
        *(uint *)(param_1 + 0x14) = uVar1;
      }
    } while (uVar1 - *(uint *)(param_1 + 0x14) < 300);
    FUN_00011af0(*(undefined2 *)(param_1 + 6),*(undefined4 *)(param_1 + 0xc),
                 *(undefined2 *)(param_1 + 4),*param_1);
    uVar2 = FUN_0001267c();
    *(undefined4 *)(param_1 + 0x14) = uVar2;
  }
  return;
}