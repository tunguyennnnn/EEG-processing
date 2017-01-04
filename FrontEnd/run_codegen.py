"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc.tools import protoc

protoc.main(
    (
	'',
	'-I=Interop/protos',
	'--python_out=Interop',
	'--grpc_python_out=Interop',
	'Interop/protos/simulation.proto',
    )
)
