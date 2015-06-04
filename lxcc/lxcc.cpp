#include "lxcc.hpp"

#include <mutex>

namespace lxcc {

SignalHandler::SignalHandler()
{
    // TODO: install handlers
}

std::shared_ptr<SignalHandler> SignalHandler::getInstance()
{
    static std::mutex mutex;
    std::lock_guard<std::mutex> lock(mutex);

    static std::weak_ptr<SignalHandler> weak;
    if (const auto shared = weak.lock())
        return shared;

    const std::shared_ptr<SignalHandler> shared(new SignalHandler);
    weak = shared;
    return shared;
}

SignalHandler::~SignalHandler()
{
    // TODO: remove handlers
}

} // namespace lxcc
