void FUN_00033f88(int param_1,uint param_2,uint param_3)

{
  undefined1 uVar1;
  int iVar2;
  undefined1 uVar3;
  undefined1 uVar4;
  undefined1 uVar5;
  uint uVar6;
  
  param_2 = param_2 & 0xffff;
  if (param_2 < *(ushort *)(param_1 + 2)) {
    uVar6 = (uint)*(byte *)(param_1 + 8);
    if (uVar6 == 0) {
      uVar4 = (undefined1)(param_3 >> 0x10);
      uVar3 = (undefined1)(param_3 >> 8);
      uVar5 = (undefined1)param_3;
    }
    else {
      uVar4 = (undefined1)((param_3 >> 0x10 & 0xff) * uVar6 >> 8);
      uVar3 = (undefined1)((param_3 >> 8 & 0xff) * uVar6 >> 8);
      uVar5 = (undefined1)((param_3 & 0xff) * uVar6 >> 8);
    }
    if ((uint)*(byte *)(param_1 + 0x10) == (uint)*(byte *)(param_1 + 0x13)) {
      iVar2 = *(int *)(param_1 + 0xc) + param_2 * 3;
    }
    else {
      iVar2 = *(int *)(param_1 + 0xc) + param_2 * 4;
      if (uVar6 == 0) {
        uVar1 = (undefined1)(param_3 >> 0x18);
      }
      else {
        uVar1 = (undefined1)((param_3 >> 0x18) * uVar6 >> 8);
      }
      *(undefined1 *)(iVar2 + (uint)*(byte *)(param_1 + 0x13)) = uVar1;
    }
    *(undefined1 *)(iVar2 + (uint)*(byte *)(param_1 + 0x10)) = uVar4;
    *(undefined1 *)(iVar2 + (uint)*(byte *)(param_1 + 0x11)) = uVar3;
    *(undefined1 *)(iVar2 + (uint)*(byte *)(param_1 + 0x12)) = uVar5;
  }
  return;
}