# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6642?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6642
- Title: ROUTE Act
- Congress: 119
- Bill type: HR
- Bill number: 6642
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-30T08:06:49Z
- Update date including text: 2026-04-30T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6642",
    "number": "6642",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "ROUTE Act",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:49Z",
    "updateDateIncludingText": "2026-04-30T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:09:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:37:44Z",
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
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "KS"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "AL"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "GA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6642ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6642\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to authorize limited operation of commercial motor vehicles for eligible drivers under age 21 in interstate commerce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responsible Opportunity for Under-21 Trucking Engagement Act or the ROUTE Act .\n#### 2. Limited interstate operation of commercial motor vehicles for drivers under 21\n##### (a) In general\nChapter 313 of title 49, United States Code, is amended by adding at the end the following:\n31318. Limited interstate operation for drivers under 21 (a) Definition of eligible driver In this section, the term \u2018eligible driver\u2019 means an individual who\u2014 (1) holds a commercial driver\u2019s license limited to intrastate operation of a commercial motor vehicle; and (2) is\u2014 (A) not less than 18 years old; and (B) less than 21 years old. (b) Limited interstate operation of commercial motor vehicles Notwithstanding any other provision of law, an eligible driver may operate a commercial motor vehicle in interstate commerce (as defined in section 31132) within a 150 air-mile radius of the normal work reporting location of the eligible driver, subject to the conditions that\u2014 (1) not more than 14 consecutive hours after departing from that normal work reporting location, the eligible driver returns to that normal work reporting location and is released from work; (2) the eligible driver has at least 10 consecutive hours off duty separating each on-duty period described in paragraph (1); and (3) the normal work reporting location of the eligible driver remains in the State in which the eligible driver holds a commercial driver\u2019s license described in subsection (a)(1). .\n##### (b) Clerical amendment\nThe analysis for chapter 313 of title 49, United States Code, is amended by adding at the end the following:\n31318. Limited interstate operation for drivers under 21. .",
      "versionDate": "2025-12-11",
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
        "updateDate": "2026-01-08T14:37:04Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6642ih.xml"
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
      "title": "ROUTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ROUTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T06:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Responsible Opportunity for Under-21 Trucking Engagement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T06:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to authorize limited operation of commercial motor vehicles for eligible drivers under age 21 in interstate commerce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T06:48:22Z"
    }
  ]
}
```
