### Script to maintain the authorization rules in DSLS license server
### Purpose is to make sure users are member from the legal authorization group

### servicedesk maintains user data, App specialists maintain the authorization groups
### script runs every hour...
####################################################################################

cls

$vary ="undefined"
################################ Functions ###########################################

# try functions, if not works we could use a class
#$script = $PSScriptRoot+"\b.ps1"
#& $script
#. $script (keep variables

function SetVariable
{
   $vary = "defined"
   return "test"
}

#Function open XML

function OpenXML
{
    $varFile=Get-Content C:\Data\Licenses\Design-Central-server\DSLS-Authorization_rules--userbased2.xml
    return $varFile
}

####################################   Main Code   ############################################
$varz = SetVariable
echo "VarZ = " $varz

# 1) Initialize
# set variables and locations...... 

##Open inputfiles
######################################################################
# 2) Open input fles
# - Userfile Americas
# - Userfile UK
# - Userfile NL
# - Pools and groups
$UserFile_US = OpenXML

# 3) Process and create output objects
# - DSLS inputfile XML
# - Changelog
# - Errorlog
# - Userinfo for chargeback


# 4) Write output to files


# 5) Import XML in DSLS server



