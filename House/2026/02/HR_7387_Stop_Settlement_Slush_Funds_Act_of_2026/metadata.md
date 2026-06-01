# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7387?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7387
- Title: Stop Settlement Slush Funds Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7387
- Origin chamber: House
- Introduced date: 2026-02-05
- Update date: 2026-04-20T23:28:56Z
- Update date including text: 2026-04-20T23:28:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-05: Introduced in House

## Actions

- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7387",
    "number": "7387",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000589",
        "district": "5",
        "firstName": "Lance",
        "fullName": "Rep. Gooden, Lance [R-TX-5]",
        "lastName": "Gooden",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop Settlement Slush Funds Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-20T23:28:56Z",
    "updateDateIncludingText": "2026-04-20T23:28:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-05",
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
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T15:01:45Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "AL"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WI"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "TN"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "AL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "SC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7387ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7387\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2026 Mr. Gooden (for himself, Ms. Tenney , Mr. Rouzer , Mr. Moore of Alabama , Mr. Tiffany , Mr. Roy , Mr. Ogles , Mr. Palmer , Mr. Fry , and Mr. McDowell ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo limit donations made pursuant to settlement agreements to which the United States is a party, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Settlement Slush Funds Act of 2026 .\n#### 2. Limitation on donations made pursuant to settlement agreements to which the united states is a party\n##### (a) Limitation on required donations\nAn official or agent of the Government may not enter into or enforce any settlement agreement on behalf of the United States directing or providing for a payment to any person or entity other than the United States, other than a payment that provides restitution for or otherwise directly remedies actual harm (including to the environment) directly and proximately caused by the party making the payment, or constitutes payment for services rendered in connection with the case.\n##### (b) Penalty\nAny official or agent of the Government who violates subsection (a) shall be subject to the same penalties that would apply in the case of a violation of section 3302 of title 31, United States Code.\n##### (c) Effective date\nSubsections (a) and (b) apply only in the case of a settlement agreement entered on or after the date of enactment of this Act.\n##### (d) Definition\nThe term settlement agreement means a settlement agreement resolving a civil action or potential civil action.\n##### (e) Reports on settlement agreements\n**(1) In general**\nNot later than at the end of the first fiscal year that begins after the date of enactment of this Act, and annually thereafter, the head of each Federal agency shall submit electronically to the Congressional Budget Office a report on each settlement agreement entered into by that agency during that fiscal year that directs or provides for a payment to a person or entity other than the United States that is providing restitution for or otherwise directly remedies actual harm (including to the environment) directly and proximately caused by the party making the payment, or that constitutes payment for services rendered in connection with the case, which shall include the parties to each settlement agreement, the source of the settlement funds, and where and how such funds were and will be distributed.\n**(2) Prohibition on additional funding**\nNo additional funds are authorized to be appropriated to carry out this subsection.\n**(3) Sunset**\nThis subsection shall cease to be effective on the date that is 7 years after the date of enactment of this Act.\n##### (f) Annual audit requirement\n**(1) In general**\nNot later than at the end of the first fiscal year that begins after the date of enactment of this Act, and annually thereafter, the Inspector General of each Federal agency shall submit, and make available on a publicly accessible website, a report on any settlement agreement entered into in violation of this section by that agency to\u2014\n**(A)**\nthe Committee on the Judiciary, the Committee on the Budget, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on the Judiciary, the Committee on the Budget, and the Committee on Appropriations of the House of Representatives.\n**(2) Prohibition on additional funding**\nNo additional funds are authorized to be appropriated to carry out this subsection.",
      "versionDate": "2026-02-05",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-20T23:28:56Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7387ih.xml"
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
      "title": "Stop Settlement Slush Funds Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Settlement Slush Funds Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit donations made pursuant to settlement agreements to which the United States is a party, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T05:18:39Z"
    }
  ]
}
```
