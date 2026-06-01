# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4500
- Title: HELP Act
- Congress: 119
- Bill type: HR
- Bill number: 4500
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-03-19T08:07:18Z
- Update date including text: 2026-03-19T08:07:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-18 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-18 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4500",
    "number": "4500",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "HELP Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:18Z",
    "updateDateIncludingText": "2026-03-19T08:07:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-18",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-18T17:05:20Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "KS"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "CO"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "TN"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "NE"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WY"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "KY"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4500ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4500\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Hurd of Colorado (for himself, Mr. Mann , Mr. Evans of Colorado , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo exempt certain livestock hauling vehicles from regulations relating to hours of service and electronic logging devices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hauling Exemptions for Livestock Protection Act or the HELP Act .\n#### 2. Exception from electronic logging devices and hours of service regulations\n##### (a) In general\nA covered livestock hauling vehicle, including the individual operating such vehicle, shall be exempt from\u2014\n**(1)**\nany requirement relating to hours of service established under\u2014\n**(A)**\nsubchapter III of chapter 311 of title 49, United States Code; or\n**(B)**\nchapter 315 of title 49, United States Code; and\n**(2)**\nany requirement relating to electronic logging devices established under section 31137 of title 49, United States Code.\n##### (b) Unladen vehicles\nAn unladen covered livestock hauling vehicle picking up or returning from delivering livestock shall be covered under the exemption under subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Commercial motor vehicle**\nThe term commercial motor vehicle has the meaning given such term in section 31132 of title 49, United States Code.\n**(2) Covered livestock hauling vehicle**\nThe term covered livestock hauling vehicle means a commercial motor vehicle transporting livestock, insects, or aquatic animals.\n**(3) Livestock**\nThe term livestock means livestock (as such term is defined in section 602 of the Emergency Livestock Feed Assistance Act of 1988 ( 7 U.S.C. 1471 )), insects, all other living animals cultivated, grown, or raised for commercial purposes, and live aquatic animals that have been caught, taken, or harvested.",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in House"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-10T16:57:59Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4500ih.xml"
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
      "title": "HELP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HELP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hauling Exemptions for Livestock Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt certain livestock hauling vehicles from regulations relating to hours of service and electronic logging devices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:59Z"
    }
  ]
}
```
