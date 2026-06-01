# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4174?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4174
- Title: ATF DATA Act
- Congress: 119
- Bill type: HR
- Bill number: 4174
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-12-06T07:00:29Z
- Update date including text: 2025-12-06T07:00:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4174",
    "number": "4174",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "ATF DATA Act",
    "type": "HR",
    "updateDate": "2025-12-06T07:00:29Z",
    "updateDateIncludingText": "2025-12-06T07:00:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-06-26T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4174ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4174\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Goldman of New York (for himself, Mr. Johnson of Georgia , and Ms. Norton ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the publication of data sets regarding firearm trace data.\n#### 1. Short title\nThis Act may be cited as the ATF Data and Anti-Trafficking Accountability Act or the ATF DATA Act .\n#### 2. Requiring the publication of data sets regarding firearm trace data\n##### (a) In general\nWithin 6 months after the date of the enactment of this Act and not less frequently than annually thereafter, the Attorney General, through the Bureau of Alcohol, Tobacco, Firearms and Explosives (in this section referred to as the Bureau ), shall submit to the Congress and make available to the public through electronic means a report that contains, at a minimum, the following information with respect to the then most recently completed calendar year (in this section referred to as the period ) for which data is available:\n**(1)**\nAggregated firearm trace data collected by the Bureau during the period, disaggregated by the license type of the source licensee.\n**(2)**\nA list of the 200 source licensees to whom the highest number of firearms were traced during the period, including\u2014\n**(A)**\nthe aggregate number of firearms traced to each such licensee, disaggregated by handguns, rifles, and shotguns;\n**(B)**\nthe cities from which the firearms were recovered;\n**(C)**\nthe average time-to-crime of the firearms traced to each such licensee;\n**(D)**\nthe categories (determined by the Attorney General) of crimes committed with the firearms traced to each such licensee, if such information is available;\n**(E)**\nthe number of traced firearms transferred by each licensee in any multiple sale; and\n**(F)**\nthe number of firearms traced to each licensee that the licensee reported, pursuant to section 923(g)(6) of title 18, United States Code, as lost or stolen.\n**(3)**\nAggregated data for the period on\u2014\n**(A)**\nthe distribution among source licensees of the following, disaggregated by licensee type, by total number, by percentage, and by source State\u2014\n**(i)**\n0 or more traced firearms;\n**(ii)**\n1 or more traced firearms;\n**(iii)**\n2 or more traced firearms;\n**(iv)**\n5 or more traced firearms;\n**(v)**\n10 or more traced firearms;\n**(vi)**\n25 or more traced firearms; and\n**(vii)**\n50 or more traced firearms; and\n**(B)**\nthe number of source licensees with any firearms traces, disaggregated by State.\n**(4)**\nAggregated firearm trace data for the period, disaggregated by the 50 Metropolitan Statistical Areas with the highest overall homicide rates (as determined by the Attorney General) for the period and by the 50 such areas with the highest per capita homicide rates (as so determined) for the period, as listed in the Federal Bureau of Investigation report, entitled Crime in the U.S. , covering the period or other national crime data used by the Bureau of Alcohol, Tobacco, Firearms and Explosives for the period, including\u2014\n**(A)**\nthe total number of firearms recovered;\n**(B)**\nthe number and percentage of firearms recovered from the 10 source States where the 10 greatest numbers of initial retail sales of the firearms occurred;\n**(C)**\nthe 20 source licensees who made the 20 greatest numbers of initial retail sales of the firearms recovered;\n**(D)**\nthe number of recovered firearms traced to each of the 20 licensees referred to in subparagraph (C), further disaggregated by\u2014\n**(i)**\nthe average time-to-crime for the firearms traced to the licensee; and\n**(ii)**\nthe number of firearms traced to the licensee with respect to which the time-to-crime was less than 3 years;\n**(E)**\nthe identities of the Federal, State, or local government agency that recovered the firearms;\n**(F)**\nthe types of firearms recovered; and\n**(G)**\nthe total number of recovered firearms with a time-to-crime of\u2014\n**(i)**\nless than 3 years;\n**(ii)**\nless than 2 years; and\n**(iii)**\nless than 1 year.\n**(5)**\nData, aggregated by State, related to the types of firearms traced during the period, including\u2014\n**(A)**\nthe category (as determined by the Attorney General) of crime leading to recovery, where the information is available;\n**(B)**\nthe 10 manufacturers who made the 10 greatest numbers of the firearms, the firearm models of the 10 greatest number of the firearms, the 10 most recovered finishes or colors of the firearms, and the 10 most recovered barrel lengths of the firearms; and\n**(C)**\nthe average time-to-crime for each subcategory (as determined by the Attorney General) of crime committed with the firearms.\n**(6)**\nThe number of traced firearms sold as part of a multiple sale recovered during the period, disaggregated by State and by\u2014\n**(A)**\nthe number of\u2014\n**(i)**\nhandguns; and\n**(ii)**\nrifles the source State of which requires the reporting of rifle sales that are part of a multiple sale of rifles;\n**(B)**\nthe average time-to-crime for the firearms; and\n**(C)**\nthe percentage of the firearms recovered in the State in which initially purchased.\n**(7)**\nThe following data on traced firearms determined to have been lost by or stolen from a licensee during the period, disaggregated by State:\n**(A)**\nThe number of the firearms, further disaggregated by licensee type.\n**(B)**\nThe number of the firearms, further disaggregated by average time-to-crime.\n**(C)**\nThe percentage of the firearms not reported by licensees as lost or stolen before the date of the trace request for the firearm involved.\n**(D)**\nThe percentage of the firearms recovered in the State in which the business premises from which the source licensee conducts business subject to the license is located.\n**(E)**\nThe number of licensees who have had 2 or more firearms lost or stolen in the 5 years preceding the period.\n**(F)**\nThe number of firearms lost or stolen from licensees referred to in subparagraph (E).\n**(G)**\nThe number of reports of lost or stolen firearms filed by licensees referred to in subparagraph (E).\n**(H)**\nThe number of incidents of theft or lost referred to in subparagraph (E) reported by licensees before the date of the trace request for the firearm involved.\n**(8)**\nThe total number of privately made firearms recovered during the period, disaggregated by\u2014\n**(A)**\nthe State in which the firearm was recovered;\n**(B)**\nthe type of firearm; and\n**(C)**\nthe firearm brand, if known.\n**(9)**\nA list, disaggregated by whole number and by per capita, of\u2014\n**(A)**\nthe 50 law enforcement agencies in the United States that requested the greatest number of firearm traces during the period; and\n**(B)**\nthe 10 law enforcement agencies in the United States that requested the greatest number of traces per State during the period.\n**(10)**\nThe aggregate number of traces during the period of firearms with serial numbers engraved or cast on the receiver or frame of the firearm in accordance with section 923(i) of such title that were recovered in a foreign country and submitted to the Bureau for tracing, disaggregated by\u2014\n**(A)**\nthe foreign country in which recovered;\n**(B)**\nthe number and percentage that were originally purchased in the United States;\n**(C)**\nthe average time-to-crime for the firearms;\n**(D)**\nthe number of firearms sold as part of a multiple sale; and\n**(E)**\nthe type of firearm.\n**(11)**\nAn overview and analysis of\u2014\n**(A)**\nfirearms trafficking patterns in the United States;\n**(B)**\nfirearms trafficking investigations undertaken by the Department of Justice, including at a minimum\u2014\n**(i)**\nthe number of firearms diverted from legal to illegal commerce by the targets of firearms trafficking investigations;\n**(ii)**\na description of how the trafficking investigations were initiated, including the number and percentage that were initiated through\u2014\n**(I)**\nmultiple sales records;\n**(II)**\ncrime gun trace data analysis;\n**(III)**\ninspections of licensees; or\n**(IV)**\nlicensee reporting of lost or stolen firearms;\n**(iii)**\nthe number and percentage of firearms trafficking investigations in which youth and juveniles were involved as possessors, straw purchasers, thieves, robbers, or traffickers;\n**(iv)**\na description of the crimes firearms traffickers were charged with, and convicted of, and the number and percentage of investigations and defendants that involved those crimes; and\n**(v)**\na breakdown by State of the number and percentage of firearms trafficking investigations; and\n**(C)**\nthe role of sales by unlicensed individuals or entities in firearms trafficking, including sales facilitated\u2014\n**(i)**\nat gun shows; or\n**(ii)**\nthrough online forums.\n##### (b) Definitions\nIn this section:\n**(1)**\nThe terms firearm , importer , manufacturer , licensed manufacturer , dealer , handgun , rifle , and shotgun have the meanings provided the terms, respectively, in section 921(a) of title 18, United States Code.\n**(2)**\nThe term time-to-crime means, with respect to a firearm, the length of time between the date of the initial retail sale of the firearm and the date of the trace request for the firearm.\n**(3)**\nThe term multiple sale means the sale or other disposition of 2 or more firearms at one time, or within 5 consecutive business days, that is required by law to be reported to the Attorney General.\n**(4)**\nThe term source licensee means, with respect to a firearm, the person licensed under chapter 44 of title 18, United States Code, who made the initial sale of the firearm to an unlicensed person.\n**(5)**\nThe term source State means, with respect to a firearm, the State or other territory of the United States where the initial retail sale of the firearm occurred.\n**(6)**\nThe term privately made firearm means a firearm that\u2014\n**(A)**\nis assembled or otherwise made by a person other than a licensed manufacturer; and\n**(B)**\nis not identified by means of a serial number or other mark engraved or cast on the receiver or frame by a licensed manufacturer or licensed dealer.",
      "versionDate": "2025-06-26",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2188",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ATF DATA Act",
      "type": "S"
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
        "updateDate": "2025-07-16T13:22:01Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4174ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2025-07-08T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ATF DATA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ATF Data and Anti-Trafficking Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the publication of data sets regarding firearm trace data.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T05:18:34Z"
    }
  ]
}
```
