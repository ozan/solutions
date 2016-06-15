#include "gigasecond.h"

boost::gregorian::date gigasecond::advance(const boost::gregorian::date date) {
  boost::posix_time::ptime t(date);
  return (t + boost::posix_time::seconds(1e9)).date();
}
