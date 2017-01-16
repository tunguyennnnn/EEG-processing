@rem Generate the C# code for .proto files

setlocal

@rem enter this directory
cd /d %~dp0

set TOOLS_PATH=..\packages\Grpc.Tools.1.0.1\tools\windows_x86

%TOOLS_PATH%\protoc.exe -I=protos --csharp_out out protos/shared.proto --grpc_out=no_client:out --plugin=protoc-gen-grpc=%TOOLS_PATH%\grpc_csharp_plugin.exe

%TOOLS_PATH%\protoc.exe -I=protos --csharp_out out protos/front_end.proto --grpc_out=no_client:out --plugin=protoc-gen-grpc=%TOOLS_PATH%\grpc_csharp_plugin.exe
%TOOLS_PATH%\protoc.exe -I=protos --csharp_out out protos/back_end.proto --grpc_out=no_server:out --plugin=protoc-gen-grpc=%TOOLS_PATH%\grpc_csharp_plugin.exe

python generate_protos.py

endlocal