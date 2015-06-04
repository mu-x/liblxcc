#ifndef LXCC_HPP
#define LXCC_HPP

#include <string>
#include <memory>

namespace lxcc {

/** Installs and deinstalls signal handlers */
class SignalHandler
{
    SignalHandler(); // singletone

public:
    /** Instantiates or just returns another @class std::shared_ptr.
     *  NOTE: keep the pointer as long as you what to collect crashes */
    std::shared_ptr<SignalHandler> getInstance();
    ~SignalHandler();

private:
    std::string mMask;
};

} // namespace lxcc

#endif // LXCC_HPP
