// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: back_end.proto
#region Designer generated code

using System;
using System.Threading;
using System.Threading.Tasks;
using Grpc.Core;

namespace Interop {
  public static class BackEnd
  {
    static readonly string __ServiceName = "interop.BackEnd";

    static readonly Marshaller<global::Interop.AquireDataRequest> __Marshaller_AquireDataRequest = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.AquireDataRequest.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.StatusReply> __Marshaller_StatusReply = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.StatusReply.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.ResetDataRequest> __Marshaller_ResetDataRequest = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.ResetDataRequest.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.TrainClassifierRequest> __Marshaller_TrainClassifierRequest = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.TrainClassifierRequest.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.RecognizeCommandsRequest> __Marshaller_RecognizeCommandsRequest = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.RecognizeCommandsRequest.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.EmptyRequest> __Marshaller_EmptyRequest = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.EmptyRequest.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.UserProfileOperationRequest> __Marshaller_UserProfileOperationRequest = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.UserProfileOperationRequest.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.ProfileDataReply> __Marshaller_ProfileDataReply = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.ProfileDataReply.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.ProfileListReply> __Marshaller_ProfileListReply = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.ProfileListReply.Parser.ParseFrom);
    static readonly Marshaller<global::Interop.UpdateSensorDataRequest> __Marshaller_UpdateSensorDataRequest = Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Interop.UpdateSensorDataRequest.Parser.ParseFrom);

    static readonly Method<global::Interop.AquireDataRequest, global::Interop.StatusReply> __Method_AcquireDataForCommand = new Method<global::Interop.AquireDataRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "AcquireDataForCommand",
        __Marshaller_AquireDataRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.ResetDataRequest, global::Interop.StatusReply> __Method_ResetDataForCommand = new Method<global::Interop.ResetDataRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "ResetDataForCommand",
        __Marshaller_ResetDataRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.TrainClassifierRequest, global::Interop.StatusReply> __Method_TrainClassifier = new Method<global::Interop.TrainClassifierRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "TrainClassifier",
        __Marshaller_TrainClassifierRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.RecognizeCommandsRequest, global::Interop.StatusReply> __Method_RecognizeCommands = new Method<global::Interop.RecognizeCommandsRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "RecognizeCommands",
        __Marshaller_RecognizeCommandsRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.EmptyRequest, global::Interop.StatusReply> __Method_StopRecognizion = new Method<global::Interop.EmptyRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "StopRecognizion",
        __Marshaller_EmptyRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.UserProfileOperationRequest, global::Interop.StatusReply> __Method_CreateUserProfile = new Method<global::Interop.UserProfileOperationRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "CreateUserProfile",
        __Marshaller_UserProfileOperationRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.UserProfileOperationRequest, global::Interop.StatusReply> __Method_DeleteUserProfile = new Method<global::Interop.UserProfileOperationRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "DeleteUserProfile",
        __Marshaller_UserProfileOperationRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.UserProfileOperationRequest, global::Interop.ProfileDataReply> __Method_GetUserProfile = new Method<global::Interop.UserProfileOperationRequest, global::Interop.ProfileDataReply>(
        MethodType.Unary,
        __ServiceName,
        "GetUserProfile",
        __Marshaller_UserProfileOperationRequest,
        __Marshaller_ProfileDataReply);

    static readonly Method<global::Interop.EmptyRequest, global::Interop.ProfileListReply> __Method_GetUserProfiles = new Method<global::Interop.EmptyRequest, global::Interop.ProfileListReply>(
        MethodType.Unary,
        __ServiceName,
        "GetUserProfiles",
        __Marshaller_EmptyRequest,
        __Marshaller_ProfileListReply);

    static readonly Method<global::Interop.UpdateSensorDataRequest, global::Interop.StatusReply> __Method_UpdateSensorData = new Method<global::Interop.UpdateSensorDataRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "UpdateSensorData",
        __Marshaller_UpdateSensorDataRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.EmptyRequest, global::Interop.StatusReply> __Method_DroneTakeoff = new Method<global::Interop.EmptyRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "DroneTakeoff",
        __Marshaller_EmptyRequest,
        __Marshaller_StatusReply);

    static readonly Method<global::Interop.EmptyRequest, global::Interop.StatusReply> __Method_DroneLand = new Method<global::Interop.EmptyRequest, global::Interop.StatusReply>(
        MethodType.Unary,
        __ServiceName,
        "DroneLand",
        __Marshaller_EmptyRequest,
        __Marshaller_StatusReply);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Interop.BackEndReflection.Descriptor.Services[0]; }
    }

    /// <summary>Client for BackEnd</summary>
    public class BackEndClient : ClientBase<BackEndClient>
    {
      /// <summary>Creates a new client for BackEnd</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public BackEndClient(Channel channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for BackEnd that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public BackEndClient(CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected BackEndClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected BackEndClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::Interop.StatusReply AcquireDataForCommand(global::Interop.AquireDataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return AcquireDataForCommand(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply AcquireDataForCommand(global::Interop.AquireDataRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_AcquireDataForCommand, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> AcquireDataForCommandAsync(global::Interop.AquireDataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return AcquireDataForCommandAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> AcquireDataForCommandAsync(global::Interop.AquireDataRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_AcquireDataForCommand, null, options, request);
      }
      public virtual global::Interop.StatusReply ResetDataForCommand(global::Interop.ResetDataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return ResetDataForCommand(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply ResetDataForCommand(global::Interop.ResetDataRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_ResetDataForCommand, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> ResetDataForCommandAsync(global::Interop.ResetDataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return ResetDataForCommandAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> ResetDataForCommandAsync(global::Interop.ResetDataRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_ResetDataForCommand, null, options, request);
      }
      public virtual global::Interop.StatusReply TrainClassifier(global::Interop.TrainClassifierRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return TrainClassifier(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply TrainClassifier(global::Interop.TrainClassifierRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_TrainClassifier, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> TrainClassifierAsync(global::Interop.TrainClassifierRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return TrainClassifierAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> TrainClassifierAsync(global::Interop.TrainClassifierRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_TrainClassifier, null, options, request);
      }
      public virtual global::Interop.StatusReply RecognizeCommands(global::Interop.RecognizeCommandsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return RecognizeCommands(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply RecognizeCommands(global::Interop.RecognizeCommandsRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_RecognizeCommands, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> RecognizeCommandsAsync(global::Interop.RecognizeCommandsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return RecognizeCommandsAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> RecognizeCommandsAsync(global::Interop.RecognizeCommandsRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_RecognizeCommands, null, options, request);
      }
      public virtual global::Interop.StatusReply StopRecognizion(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return StopRecognizion(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply StopRecognizion(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_StopRecognizion, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> StopRecognizionAsync(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return StopRecognizionAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> StopRecognizionAsync(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_StopRecognizion, null, options, request);
      }
      public virtual global::Interop.StatusReply CreateUserProfile(global::Interop.UserProfileOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return CreateUserProfile(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply CreateUserProfile(global::Interop.UserProfileOperationRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_CreateUserProfile, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> CreateUserProfileAsync(global::Interop.UserProfileOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return CreateUserProfileAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> CreateUserProfileAsync(global::Interop.UserProfileOperationRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_CreateUserProfile, null, options, request);
      }
      public virtual global::Interop.StatusReply DeleteUserProfile(global::Interop.UserProfileOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return DeleteUserProfile(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply DeleteUserProfile(global::Interop.UserProfileOperationRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_DeleteUserProfile, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> DeleteUserProfileAsync(global::Interop.UserProfileOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return DeleteUserProfileAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> DeleteUserProfileAsync(global::Interop.UserProfileOperationRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_DeleteUserProfile, null, options, request);
      }
      public virtual global::Interop.ProfileDataReply GetUserProfile(global::Interop.UserProfileOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return GetUserProfile(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.ProfileDataReply GetUserProfile(global::Interop.UserProfileOperationRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetUserProfile, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.ProfileDataReply> GetUserProfileAsync(global::Interop.UserProfileOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return GetUserProfileAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.ProfileDataReply> GetUserProfileAsync(global::Interop.UserProfileOperationRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetUserProfile, null, options, request);
      }
      public virtual global::Interop.ProfileListReply GetUserProfiles(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return GetUserProfiles(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.ProfileListReply GetUserProfiles(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetUserProfiles, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.ProfileListReply> GetUserProfilesAsync(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return GetUserProfilesAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.ProfileListReply> GetUserProfilesAsync(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetUserProfiles, null, options, request);
      }
      public virtual global::Interop.StatusReply UpdateSensorData(global::Interop.UpdateSensorDataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return UpdateSensorData(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply UpdateSensorData(global::Interop.UpdateSensorDataRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_UpdateSensorData, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> UpdateSensorDataAsync(global::Interop.UpdateSensorDataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return UpdateSensorDataAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> UpdateSensorDataAsync(global::Interop.UpdateSensorDataRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_UpdateSensorData, null, options, request);
      }
      public virtual global::Interop.StatusReply DroneTakeoff(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return DroneTakeoff(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply DroneTakeoff(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_DroneTakeoff, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> DroneTakeoffAsync(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return DroneTakeoffAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> DroneTakeoffAsync(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_DroneTakeoff, null, options, request);
      }
      public virtual global::Interop.StatusReply DroneLand(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return DroneLand(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Interop.StatusReply DroneLand(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_DroneLand, null, options, request);
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> DroneLandAsync(global::Interop.EmptyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return DroneLandAsync(request, new CallOptions(headers, deadline, cancellationToken));
      }
      public virtual AsyncUnaryCall<global::Interop.StatusReply> DroneLandAsync(global::Interop.EmptyRequest request, CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_DroneLand, null, options, request);
      }
      protected override BackEndClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new BackEndClient(configuration);
      }
    }

  }
}
#endregion
