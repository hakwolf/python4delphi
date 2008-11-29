////
//  This file was generated by VCL Generator
//  Copyright 1998 - Morgan Martinet
//  06/07/1999 07:59:00
//  it subclasses all classes of the unit System
////

unit Delphi_System;

interface

uses
  PythonEngine,
  PyVarArg,
  PyRecords,
  PyDelphiAssoc;

type
  TPyObject = class( TObject )
  protected
    FAssoc : Integer;
  public
    destructor Destroy; override;
  published
    property __assoc__ : Integer read FAssoc write FAssoc;
  end;

  TPyInterfacedObject = class( TInterfacedObject )
  protected
    FAssoc : Integer;
  public
    destructor Destroy; override;
  published
    property __assoc__ : Integer read FAssoc write FAssoc;
  end;


implementation

Uses Py_Misc;

/////////// class TPyObject /////////////////////

destructor TPyObject.Destroy;
begin
  ClearInterface( TDelphiAssoc(FAssoc) );
  FAssoc := 0;
  inherited;
end;

/////////// class TPyInterfacedObject /////////////////////

destructor TPyInterfacedObject.Destroy;
begin
  ClearInterface( TDelphiAssoc(FAssoc) );
  FAssoc := 0;
  inherited;
end;


end.
