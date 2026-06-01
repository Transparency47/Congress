# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2328?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2328
- Title: Soo Locks Security and Economic Reporting Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2328
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-06-27T08:06:39Z
- Update date including text: 2025-06-27T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-25 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-25 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2328",
    "number": "2328",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "J000307",
        "district": "10",
        "firstName": "John",
        "fullName": "Rep. James, John [R-MI-10]",
        "lastName": "James",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Soo Locks Security and Economic Reporting Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-27T08:06:39Z",
    "updateDateIncludingText": "2025-06-27T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-25T20:44:59Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2328ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2328\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. James introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo study the security of the Soo Locks and effects on the supply chain resulting from a malfunction or failure of the Soo Locks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Soo Locks Security and Economic Reporting Act of 2025 .\n#### 2. Report on security and economic effects on supply chain of Soo Locks, Michigan\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation, in coordination with the Commandant of the Coast Guard and the Secretary of Defense, shall submit to the appropriate committees of Congress a report that\u2014\n**(1)**\nhighlights any security deficiencies that exist with respect to the Soo Locks in Sault Ste. Marie, Michigan;\n**(2)**\nhighlights the supply chain, logistical, and economic effects that would result in the event of a malfunction or failure of the Soo Locks and how such effects would impact the region surrounding the Soo Locks and the United States;\n**(3)**\nhighlights any potential domestic or international threats to the integrity of the Soo Locks;\n**(4)**\ndetails the current security structure of the Coast Guard and any other relevant Federal, State, or local agency to protect the Soo Locks; and\n**(5)**\nprovides any recommendations, and cost estimates for such recommendations, for\u2014\n**(A)**\nstrengthening the security of the Soo Locks; and\n**(B)**\nreducing the impacts to the supply chain of the United States that would result in the event of a malfunction or failure of the Soo Locks.\n##### (b) Appropriate committees of Congress defined\nIn this Act, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Transportation and Infrastructure of the House of Representatives;\n**(2)**\nthe Committee on Commerce, Transportation, and Science of the Senate; and\n**(3)**\nthe Committee on Environment and Public Works of the Senate.",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-05-20T17:02:47Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2328ih.xml"
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
      "title": "Soo Locks Security and Economic Reporting Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T06:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Soo Locks Security and Economic Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T06:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To study the security of the Soo Locks and effects on the supply chain resulting from a malfunction or failure of the Soo Locks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T06:48:37Z"
    }
  ]
}
```
