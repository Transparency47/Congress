# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2188
- Title: ATF DATA Act
- Congress: 119
- Bill type: S
- Bill number: 2188
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2025-12-06T06:59:57Z
- Update date including text: 2025-12-06T06:59:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2188",
    "number": "2188",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "ATF DATA Act",
    "type": "S",
    "updateDate": "2025-12-06T06:59:57Z",
    "updateDateIncludingText": "2025-12-06T06:59:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-06-26T20:25:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NJ"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2188is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2188\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Mr. Schiff (for himself, Mr. Booker , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the publication of data sets regarding firearm trace data.\n#### 1. Short title\nThis Act may be cited as the ATF Data and Anti-Trafficking Accountability Act or the ATF DATA Act .\n#### 2. Requiring the publication of data sets regarding firearm trace data\n##### (a) Definitions\nIn this section:\n**(1) Bureau**\nThe term Bureau means the Bureau of Alcohol, Tobacco, Firearms and Explosives.\n**(2) Firearm, importer, manufacturer, licensed manufacturer, dealer, handgun, rifle, shotgun**\nThe terms firearm , importer , manufacturer , licensed manufacturer , dealer , handgun , rifle , and shotgun have the meanings provided the terms, respectively, in section 921(a) of title 18, United States Code.\n**(3) Multiple sale**\nThe term multiple sale means the sale or other disposition of 2 or more firearms at one time, or within 5 consecutive business days, that is required by law to be reported to the Attorney General.\n**(4) Covered period**\nThe term covered period means the most recently completed calendar year.\n**(5) Privately made firearm**\nThe term privately made firearm means a firearm that\u2014\n**(A)**\nis assembled or otherwise made by a person other than a licensed manufacturer; and\n**(B)**\nis not identified by means of a serial number or other mark engraved or cast on the receiver or frame by a licensed manufacturer or licensed dealer.\n**(6) Source licensee**\nThe term source licensee means, with respect to a firearm, the person licensed under chapter 44 of title 18, United States Code, who made the initial sale of the firearm to an unlicensed person.\n**(7) Source State**\nThe term source State means, with respect to a firearm, the State or other territory of the United States where the initial retail sale of the firearm occurred.\n**(8) Time-to-crime**\nThe term time-to-crime means, with respect to a firearm, the length of time between the date of the initial retail sale of the firearm and the date of the trace request for the firearm.\n##### (b) Report\nNot later than 180 days after the date of enactment of this Act and not less frequently than annually thereafter, the Attorney General, through the Bureau shall submit to Congress and make available to the public through electronic means a report that contains, at a minimum, the following information with respect to the covered period for which data is available:\n**(1)**\nAggregated firearm trace data collected by the Bureau during the covered period, disaggregated by the license type of the source licensee.\n**(2)**\nA list of the 200 source licensees to whom the highest number of firearms were traced during the covered period, including\u2014\n**(A)**\nthe aggregate number of firearms traced to each such licensee, disaggregated by handguns, rifles, and shotguns;\n**(B)**\nthe cities from which the firearms were recovered;\n**(C)**\nthe average time-to-crime of the firearms traced to each such licensee;\n**(D)**\nthe categories, determined by the Attorney General, of crimes committed with the firearms traced to each such licensee, if such information is available;\n**(E)**\nthe number of traced firearms transferred by each licensee in any multiple sale; and\n**(F)**\nthe number of firearms traced to each licensee that the licensee reported, pursuant to section 923(g)(6) of title 18, United States Code, as lost or stolen.\n**(3)**\nAggregated data for the covered period on\u2014\n**(A)**\nthe distribution among source licensees of the following, disaggregated by licensee type, by total number, by percentage, and by source State\u2014\n**(i)**\n0 or more traced firearms;\n**(ii)**\n1 or more traced firearms;\n**(iii)**\n2 or more traced firearms;\n**(iv)**\n5 or more traced firearms;\n**(v)**\n10 or more traced firearms;\n**(vi)**\n25 or more traced firearms; and\n**(vii)**\n50 or more traced firearms; and\n**(B)**\nthe number of source licensees with any firearms traces, disaggregated by State.\n**(4)**\nAggregated firearm trace data for the covered period, disaggregated by the 50 Metropolitan Statistical Areas, as defined by the Office of Management and Budget, with the highest overall homicide rates, as determined by the Attorney General, for the covered period and by the 50 such areas with the highest per capita homicide rates, as so determined, for the covered period, as listed in the Federal Bureau of Investigation report, entitled Crime in the U.S. , covering the covered period or other national crime data used by the Bureau for the covered period, including\u2014\n**(A)**\nthe total number of firearms recovered;\n**(B)**\nthe number and percentage of firearms recovered from the 10 source States where the 10 greatest numbers of initial retail sales of the firearms occurred;\n**(C)**\nthe 20 source licensees who made the 20 greatest numbers of initial retail sales of the firearms recovered;\n**(D)**\nthe number of recovered firearms traced to each of the 20 licensees referred to in subparagraph (C), further disaggregated by\u2014\n**(i)**\nthe average time-to-crime for the firearms traced to the licensee; and\n**(ii)**\nthe number of firearms traced to the licensee with respect to which the time-to-crime was less than 3 years;\n**(E)**\nthe identities of the Federal, State, or local government agency that recovered the firearms;\n**(F)**\nthe types of firearms recovered; and\n**(G)**\nthe total number of recovered firearms with a time-to-crime of\u2014\n**(i)**\nless than 3 years;\n**(ii)**\nless than 2 years; and\n**(iii)**\nless than 1 year.\n**(5)**\nData, aggregated by State, related to the types of firearms traced during the covered period, including\u2014\n**(A)**\nthe category, as determined by the Attorney General, of crime leading to recovery, where the information is available;\n**(B)**\nthe 10 manufacturers who made the 10 greatest numbers of the firearms, the firearm models of the 10 greatest numbers of the firearms, the 10 most recovered finishes or colors of the firearms, and the 10 most recovered barrel lengths of the firearms; and\n**(C)**\nthe average time-to-crime for each subcategory, as determined by the Attorney General, of crime committed with the firearms.\n**(6)**\nThe number of traced firearms sold as part of a multiple sale recovered during the covered period, disaggregated by State and by\u2014\n**(A)**\nthe number of\u2014\n**(i)**\nhandguns; and\n**(ii)**\nrifles the source State of which requires the reporting of rifle sales that are part of a multiple sale of rifles;\n**(B)**\nthe average time-to-crime for the firearms; and\n**(C)**\nthe percentage of the firearms recovered in the State in which initially purchased.\n**(7)**\nThe following data on traced firearms determined to have been lost by or stolen from a licensee during the covered period, disaggregated by State:\n**(A)**\nThe number of the firearms, further disaggregated by licensee type.\n**(B)**\nThe number of the firearms, further disaggregated by average time-to-crime.\n**(C)**\nThe percentage of the firearms not reported by licensees as lost or stolen before the date of the trace request for the firearm involved.\n**(D)**\nThe percentage of the firearms recovered in the State in which the business premises from which the source licensee conducts business subject to the license is located.\n**(E)**\nThe number of licensees who have had 2 or more firearms lost or stolen in the 5 years preceding the covered period.\n**(F)**\nThe number of firearms lost or stolen from licensees referred to in subparagraph (E).\n**(G)**\nThe number of reports of lost or stolen firearms filed by licensees referred to in subparagraph (E).\n**(H)**\nThe number of incidents of theft or loss referred to in subparagraph (E) reported by licensees before the date of the trace request for the firearm involved.\n**(8)**\nThe total number of privately made firearms recovered during the covered period, disaggregated by\u2014\n**(A)**\nthe State in which the firearm was recovered;\n**(B)**\nthe type of firearm; and\n**(C)**\nthe firearm brand, if known.\n**(9)**\nA list, disaggregated by whole number and by per capita, of\u2014\n**(A)**\nthe 50 law enforcement agencies in the United States that requested the greatest number of firearm traces during the covered period; and\n**(B)**\nthe 10 law enforcement agencies in the United States that requested the greatest number of traces per State during the covered period.\n**(10)**\nThe aggregate number of traces during the covered period of firearms with serial numbers engraved or cast on the receiver or frame of the firearm in accordance with section 923(i) of title 18, United States Code, that were recovered in a foreign country and submitted to the Bureau for tracing, disaggregated by\u2014\n**(A)**\nthe foreign country in which they were recovered;\n**(B)**\nthe number and percentage that were originally purchased in the United States;\n**(C)**\nthe average time-to-crime for the firearms;\n**(D)**\nthe number of firearms sold as part of a multiple sale; and\n**(E)**\nthe type of firearm.\n**(11)**\nAn overview and analysis of\u2014\n**(A)**\nfirearms trafficking patterns in the United States;\n**(B)**\nfirearms trafficking investigations undertaken by the Department of Justice, including at a minimum\u2014\n**(i)**\nthe number of firearms diverted from legal to illegal commerce by the targets of firearms trafficking investigations;\n**(ii)**\na description of how the trafficking investigations were initiated, including the number and percentage that were initiated through\u2014\n**(I)**\nmultiple sales records;\n**(II)**\ncrime gun trace data analysis;\n**(III)**\ninspections of licensees; or\n**(IV)**\nlicensee reporting of lost or stolen firearms;\n**(iii)**\nthe number and percentage of firearms trafficking investigations in which youth and juveniles were involved as possessors, straw purchasers, thieves, robbers, or traffickers;\n**(iv)**\na description of the crimes firearms traffickers were charged with, and convicted of, and the number of investigations that involved those crimes and defendants that were charged in those crimes; and\n**(v)**\na breakdown by State of the number and percentage of firearms trafficking investigations; and\n**(C)**\nthe role of sales by unlicensed individuals or entities in firearms trafficking, including sales facilitated\u2014\n**(i)**\nat gun shows; or\n**(ii)**\nthrough online forums.",
      "versionDate": "2025-06-26",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4174",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ATF DATA Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-16T13:22:22Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2188is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "ATF DATA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ATF DATA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ATF Data and Anti-Trafficking Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the publication of data sets regarding firearm trace data.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:22Z"
    }
  ]
}
```
