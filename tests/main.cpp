#define CATCH_CONFIG_RUNNER

#include <catch2/catch.hpp>
#include <faabric/util/logging.h>

struct LogListener : Catch::TestEventListenerBase
{
    using TestEventListenerBase::TestEventListenerBase;

    void testCaseStarting(Catch::TestCaseInfo const& testInfo) override
    {
        auto logger = faabric::util::getLogger();
        logger->debug("---------------------------------------------");
        logger->debug("TEST: {}", testInfo.name);
        logger->debug("---------------------------------------------");
    }
};

int main(int argc, char* argv[])
{
    int result = Catch::Session().run(argc, argv);

    fflush(stdout);

    return result;
}
