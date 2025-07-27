description = [[
EduMap Pro: Fingerprints Indian .edu.in sites
- Server, CMS, frameworks, SSL cert info, etc.
]]

-- Usage:
-- nmap --script ./nse/fingerprint_edu_in.nse -p 80,443 -iL domains.txt

author = "popeyee"
categories = {"discovery", "safe"}

portrule = function(host, port)
  return port.protocol == "tcp" and port.state == "open"
end

action = function(host, port)
  local http = require "http"
  local stdnse = require "stdnse"
  local output = {}

  local resp = http.get(host, port, "/")
  if not resp then return "No HTTP response" end

  output["Domain"] = host.name or host.ip
  output["Server"] = resp.header["server"] or "Unknown"

  local body = resp.body or ""

  -- Detect CMS
  if body:match("wp%-content") then output["CMS"]="WordPress"
  elseif body:match("Moodle") then output["CMS"]="Moodle"
  elseif body:match("Drupal") then output["CMS"]="Drupal"
  elseif body:match("Joomla") then output["CMS"]="Joomla"
  else output["CMS"]="Unknown" end

  -- Detect frameworks
  if body:match("ng%-app") then output["Framework"]="AngularJS"
  elseif body:match("React") then output["Framework"]="React"
  elseif body:match("Vue") then output["Framework"]="Vue.js"
  else output["Framework"]="Unknown" end

  -- WHOIS (basic, optional)
  local whois_cmd = "whois " .. host.name .. " | grep -iE 'Registrant Organization|OrgName|Organization' | head -n 1"
  local handle = io.popen(whois_cmd)
  local whois = handle:read("*a")
  handle:close()
  output["WHOIS"] = whois:gsub("\n","") or "Not found"

  return stdnse.format_output(true, output)
end
