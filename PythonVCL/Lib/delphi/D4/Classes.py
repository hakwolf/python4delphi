###
#  This file was generated by VCL Generator
#  Copyright 1998 - Morgan Martinet
#  06/07/1999 07:58:58
#  it declares the symbols of the Delphi unit Classes.pas
###

from System import *
import _Classes

# TAlignment = ( taLeftJustify, taRightJustify, taCenter );
taLeftJustify = 0
taRightJustify = 1
taCenter = 2

# TBiDiMode = ( bdLeftToRight, bdRightToLeft, bdRightToLeftNoAlign, bdRightToLeftReadingOnly );
bdLeftToRight = 0
bdRightToLeft = 1
bdRightToLeftNoAlign = 2
bdRightToLeftReadingOnly = 3

# TShiftState = set of ( ssShift, ssAlt, ssCtrl, ssLeft, ssRight, ssMiddle, ssDouble );
ssShift = 0
ssAlt = 1
ssCtrl = 2
ssLeft = 3
ssRight = 4
ssMiddle = 5
ssDouble = 6

# TDuplicates = ( dupIgnore, dupAccept, dupError );
dupIgnore = 0
dupAccept = 1
dupError = 2

# TStreamOwnership = ( soReference, soOwned );
soReference = 0
soOwned = 1

# TValueType = ( vaNull, vaList, vaInt8, vaInt16, vaInt32, vaExtended, vaString, vaIdent, vaFalse, vaTrue, vaBinary, vaSet, vaLString, vaNil, vaCollection, vaSingle, vaCurrency, vaDate, vaWString );
vaNull = 0
vaList = 1
vaInt8 = 2
vaInt16 = 3
vaInt32 = 4
vaExtended = 5
vaString = 6
vaIdent = 7
vaFalse = 8
vaTrue = 9
vaBinary = 10
vaSet = 11
vaLString = 12
vaNil = 13
vaCollection = 14
vaSingle = 15
vaCurrency = 16
vaDate = 17
vaWString = 18

# TFilerFlag = ( ffInherited, ffChildPos );
ffInherited = 0
ffChildPos = 1

# TThreadPriority = ( tpIdle, tpLowest, tpLower, tpNormal, tpHigher, tpHighest, tpTimeCritical );
tpIdle = 0
tpLowest = 1
tpLower = 2
tpNormal = 3
tpHigher = 4
tpHighest = 5
tpTimeCritical = 6

# TOperation = ( opInsert, opRemove );
opInsert = 0
opRemove = 1

# TComponentState = set of ( csLoading, csReading, csWriting, csDestroying, csDesigning, csAncestor, csUpdating, csFixups );
csLoading = 0
csReading = 1
csWriting = 2
csDestroying = 3
csDesigning = 4
csAncestor = 5
csUpdating = 6
csFixups = 7

# TComponentStyle = set of ( csInheritable, csCheckPropAvail );
csInheritable = 0
csCheckPropAvail = 1

# TActiveXRegType = ( axrComponentOnly, axrIncludeDescendants );
axrComponentOnly = 0
axrIncludeDescendants = 1

####################################################
class TList( TObject ):
    def Create( Self ):
        return _Classes.CreateList( Self )

    def __getattr__( Self, Key ):
        return _Classes.List_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.List_SetAttr( Self, Key, Value )

####################################################
class TThreadList(TObject):
    def Create( Self ):
        return _Classes.CreateThreadList( Self )

    def __getattr__( Self, Key ):
        return _Classes.ThreadList_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.ThreadList_SetAttr( Self, Key, Value )

####################################################
class TBits(TObject):
    def Create( Self ):
        return _Classes.CreateBits( Self )

    def __getattr__( Self, Key ):
        return _Classes.Bits_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Bits_SetAttr( Self, Key, Value )

####################################################
class TPersistent( TObject ):
    def Create( Self ):
        return _Classes.CreatePersistent( Self )

    def __getattr__( Self, Key ):
        return _Classes.Persistent_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Persistent_SetAttr( Self, Key, Value )

####################################################
class TCollectionItem( TPersistent ):
    def Create( Self, Collection ):
        return _Classes.CreateCollectionItem( Self, Collection )

    def __getattr__( Self, Key ):
        return _Classes.CollectionItem_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.CollectionItem_SetAttr( Self, Key, Value )

####################################################
class TCollection( TPersistent ):
    def Create( Self, ItemClass ):
        return _Classes.CreateCollection( Self, ItemClass )

    def __getattr__( Self, Key ):
        return _Classes.Collection_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Collection_SetAttr( Self, Key, Value )

####################################################
class TOwnedCollection( TCollection ):
    def Create( Self, AOwner, ItemClass ):
        return _Classes.CreateOwnedCollection( Self, AOwner, ItemClass )

    def __getattr__( Self, Key ):
        return _Classes.OwnedCollection_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.OwnedCollection_SetAttr( Self, Key, Value )

####################################################
class TStrings( TPersistent ):
    def Create( Self ):
        return _Classes.CreateStrings( Self )

    def __getattr__( Self, Key ):
        return _Classes.Strings_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Strings_SetAttr( Self, Key, Value )

####################################################
class TStringList( TStrings ):
    def Create( Self ):
        return _Classes.CreateStringList( Self )

    def __getattr__( Self, Key ):
        return _Classes.StringList_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.StringList_SetAttr( Self, Key, Value )

####################################################
class TStream( TObject ):
    def Create( Self ):
        return _Classes.CreateStream( Self )

    def __getattr__( Self, Key ):
        return _Classes.Stream_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Stream_SetAttr( Self, Key, Value )

####################################################
class THandleStream( TStream ):
    def Create( Self, AHandle ):
        return _Classes.CreateHandleStream( Self, AHandle )

    def __getattr__( Self, Key ):
        return _Classes.HandleStream_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.HandleStream_SetAttr( Self, Key, Value )

####################################################
class TFileStream( THandleStream ):
    def Create( Self, FileName, Mode ):
        return _Classes.CreateFileStream( Self, FileName, Mode )

    def __getattr__( Self, Key ):
        return _Classes.FileStream_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.FileStream_SetAttr( Self, Key, Value )

####################################################
class TCustomMemoryStream( TStream ):
    def Create( Self ):
        return _Classes.CreateCustomMemoryStream( Self )

    def __getattr__( Self, Key ):
        return _Classes.CustomMemoryStream_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.CustomMemoryStream_SetAttr( Self, Key, Value )

####################################################
class TMemoryStream( TCustomMemoryStream ):
    def Create( Self ):
        return _Classes.CreateMemoryStream( Self )

    def __getattr__( Self, Key ):
        return _Classes.MemoryStream_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.MemoryStream_SetAttr( Self, Key, Value )

####################################################
class TStringStream( TStream ):
    def Create( Self, AString ):
        return _Classes.CreateStringStream( Self, AString )

    def __getattr__( Self, Key ):
        return _Classes.StringStream_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.StringStream_SetAttr( Self, Key, Value )

####################################################
class TResourceStream( TCustomMemoryStream ):
    def Create( Self, Instance, ResName, ResType ):
        return _Classes.CreateResourceStream( Self, Instance, ResName, ResType )

    def CreateFromID( Self, Instance, ResID, ResType ):
        return _Classes.CreateFromIDResourceStream( Self, Instance, ResID, ResType )

    def __getattr__( Self, Key ):
        return _Classes.ResourceStream_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.ResourceStream_SetAttr( Self, Key, Value )

####################################################
class TStreamAdapter( TInterfacedObject ):
    def Create( Self, Stream, Ownership = soReference ):
        return _Classes.CreateStreamAdapter( Self, Stream, Ownership )

    def __getattr__( Self, Key ):
        return _Classes.StreamAdapter_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.StreamAdapter_SetAttr( Self, Key, Value )

####################################################
class TFiler( TObject ):
    def Create( Self, Stream, BufSize ):
        return _Classes.CreateFiler( Self, Stream, BufSize )

    def __getattr__( Self, Key ):
        return _Classes.Filer_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Filer_SetAttr( Self, Key, Value )

####################################################
class TReader( TFiler ):
    def Create( Self, Stream, BufSize ):
        return _Classes.CreateReader( Self, Stream, BufSize )

    def __getattr__( Self, Key ):
        return _Classes.Reader_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Reader_SetAttr( Self, Key, Value )

####################################################
class TWriter( TFiler ):
    def Create( Self, Stream, BufSize ):
        return _Classes.CreateWriter( Self, Stream, BufSize )

    def __getattr__( Self, Key ):
        return _Classes.Writer_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Writer_SetAttr( Self, Key, Value )

####################################################
class TParser( TObject ):
    def Create( Self, Stream ):
        return _Classes.CreateParser( Self, Stream )

    def __getattr__( Self, Key ):
        return _Classes.Parser_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Parser_SetAttr( Self, Key, Value )

####################################################
class TThread(TObject):
    def Create( Self, CreateSuspended ):
        return _Classes.CreateThread( Self, CreateSuspended )

    def __getattr__( Self, Key ):
        return _Classes.Thread_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Thread_SetAttr( Self, Key, Value )

####################################################
class TComponent( TPersistent ):
    def Create( Self, AOwner ):
        return _Classes.CreateComponent( Self, AOwner )

    def __getattr__( Self, Key ):
        return _Classes.Component_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.Component_SetAttr( Self, Key, Value )

####################################################
class TBasicActionLink( TObject ):
    def Create( Self, AClient ):
        return _Classes.CreateBasicActionLink( Self, AClient )

    def __getattr__( Self, Key ):
        return _Classes.BasicActionLink_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.BasicActionLink_SetAttr( Self, Key, Value )

####################################################
class TBasicAction( TComponent ):
    def Create( Self, AOwner ):
        return _Classes.CreateBasicAction( Self, AOwner )

    def __getattr__( Self, Key ):
        return _Classes.BasicAction_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Classes.BasicAction_SetAttr( Self, Key, Value )

