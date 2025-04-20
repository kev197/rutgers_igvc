; Auto-generated. Do not edit!


(cl:in-package cartographer_ros-msg)


;//! \htmlinclude pair.msg.html

(cl:defclass <pair> (roslisp-msg-protocol:ros-message)
  ((x_avg
    :reader x_avg
    :initarg :x_avg
    :type cl:integer
    :initform 0)
   (width
    :reader width
    :initarg :width
    :type cl:integer
    :initform 0))
)

(cl:defclass pair (<pair>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pair>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pair)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cartographer_ros-msg:<pair> is deprecated: use cartographer_ros-msg:pair instead.")))

(cl:ensure-generic-function 'x_avg-val :lambda-list '(m))
(cl:defmethod x_avg-val ((m <pair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cartographer_ros-msg:x_avg-val is deprecated.  Use cartographer_ros-msg:x_avg instead.")
  (x_avg m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <pair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cartographer_ros-msg:width-val is deprecated.  Use cartographer_ros-msg:width instead.")
  (width m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pair>) ostream)
  "Serializes a message object of type '<pair>"
  (cl:let* ((signed (cl:slot-value msg 'x_avg)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pair>) istream)
  "Deserializes a message object of type '<pair>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x_avg) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'width) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pair>)))
  "Returns string type for a message object of type '<pair>"
  "cartographer_ros/pair")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pair)))
  "Returns string type for a message object of type 'pair"
  "cartographer_ros/pair")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pair>)))
  "Returns md5sum for a message object of type '<pair>"
  "e422f6ba709537d0cc32d10fc4426744")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pair)))
  "Returns md5sum for a message object of type 'pair"
  "e422f6ba709537d0cc32d10fc4426744")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pair>)))
  "Returns full string definition for message of type '<pair>"
  (cl:format cl:nil "int64 x_avg~%int64 width~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pair)))
  "Returns full string definition for message of type 'pair"
  (cl:format cl:nil "int64 x_avg~%int64 width~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pair>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pair>))
  "Converts a ROS message object to a list"
  (cl:list 'pair
    (cl:cons ':x_avg (x_avg msg))
    (cl:cons ':width (width msg))
))
