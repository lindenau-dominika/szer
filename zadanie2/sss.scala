import java.util.TimeZone

def australiaZones(): Array[String] =
  TimeZone.getAvailableIDs
    .filter(_.startsWith("Australia/"))
    .map(_.substring("Australia/".length))
    .sorted