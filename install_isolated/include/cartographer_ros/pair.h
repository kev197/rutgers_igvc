// Generated by gencpp from file cartographer_ros/pair.msg
// DO NOT EDIT!


#ifndef CARTOGRAPHER_ROS_MESSAGE_PAIR_H
#define CARTOGRAPHER_ROS_MESSAGE_PAIR_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace cartographer_ros
{
template <class ContainerAllocator>
struct pair_
{
  typedef pair_<ContainerAllocator> Type;

  pair_()
    : x_avg(0)
    , width(0)  {
    }
  pair_(const ContainerAllocator& _alloc)
    : x_avg(0)
    , width(0)  {
  (void)_alloc;
    }



   typedef int64_t _x_avg_type;
  _x_avg_type x_avg;

   typedef int64_t _width_type;
  _width_type width;





  typedef boost::shared_ptr< ::cartographer_ros::pair_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cartographer_ros::pair_<ContainerAllocator> const> ConstPtr;

}; // struct pair_

typedef ::cartographer_ros::pair_<std::allocator<void> > pair;

typedef boost::shared_ptr< ::cartographer_ros::pair > pairPtr;
typedef boost::shared_ptr< ::cartographer_ros::pair const> pairConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cartographer_ros::pair_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cartographer_ros::pair_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::cartographer_ros::pair_<ContainerAllocator1> & lhs, const ::cartographer_ros::pair_<ContainerAllocator2> & rhs)
{
  return lhs.x_avg == rhs.x_avg &&
    lhs.width == rhs.width;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::cartographer_ros::pair_<ContainerAllocator1> & lhs, const ::cartographer_ros::pair_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace cartographer_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros::pair_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros::pair_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros::pair_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros::pair_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros::pair_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros::pair_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cartographer_ros::pair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e422f6ba709537d0cc32d10fc4426744";
  }

  static const char* value(const ::cartographer_ros::pair_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe422f6ba709537d0ULL;
  static const uint64_t static_value2 = 0xcc32d10fc4426744ULL;
};

template<class ContainerAllocator>
struct DataType< ::cartographer_ros::pair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cartographer_ros/pair";
  }

  static const char* value(const ::cartographer_ros::pair_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cartographer_ros::pair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 x_avg\n"
"int64 width\n"
;
  }

  static const char* value(const ::cartographer_ros::pair_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cartographer_ros::pair_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x_avg);
      stream.next(m.width);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct pair_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cartographer_ros::pair_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cartographer_ros::pair_<ContainerAllocator>& v)
  {
    s << indent << "x_avg: ";
    Printer<int64_t>::stream(s, indent + "  ", v.x_avg);
    s << indent << "width: ";
    Printer<int64_t>::stream(s, indent + "  ", v.width);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CARTOGRAPHER_ROS_MESSAGE_PAIR_H
