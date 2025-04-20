// Auto-generated. Do not edit!

// (in-package cartographer_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class pair {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_avg = null;
      this.width = null;
    }
    else {
      if (initObj.hasOwnProperty('x_avg')) {
        this.x_avg = initObj.x_avg
      }
      else {
        this.x_avg = 0;
      }
      if (initObj.hasOwnProperty('width')) {
        this.width = initObj.width
      }
      else {
        this.width = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type pair
    // Serialize message field [x_avg]
    bufferOffset = _serializer.int64(obj.x_avg, buffer, bufferOffset);
    // Serialize message field [width]
    bufferOffset = _serializer.int64(obj.width, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type pair
    let len;
    let data = new pair(null);
    // Deserialize message field [x_avg]
    data.x_avg = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [width]
    data.width = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cartographer_ros/pair';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e422f6ba709537d0cc32d10fc4426744';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 x_avg
    int64 width
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new pair(null);
    if (msg.x_avg !== undefined) {
      resolved.x_avg = msg.x_avg;
    }
    else {
      resolved.x_avg = 0
    }

    if (msg.width !== undefined) {
      resolved.width = msg.width;
    }
    else {
      resolved.width = 0
    }

    return resolved;
    }
};

module.exports = pair;
