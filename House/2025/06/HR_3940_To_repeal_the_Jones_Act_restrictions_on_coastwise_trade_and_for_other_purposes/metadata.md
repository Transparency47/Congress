# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3940?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3940
- Title: Open America's Waters Act
- Congress: 119
- Bill type: HR
- Bill number: 3940
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-12-05T21:51:05Z
- Update date including text: 2025-12-05T21:51:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3940",
    "number": "3940",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Open America's Waters Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:51:05Z",
    "updateDateIncludingText": "2025-12-05T21:51:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
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
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T20:49:59Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3940ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3940\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. McClintock introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo repeal the Jones Act restrictions on coastwise trade, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Open America's Waters Act .\n#### 2. Repeal of certain limitations on coastwise trade\n##### (a) In general\nSection 12112(a) of title 46, United States Code, is amended to read as follows:\n(a) In general A coastwise endorsement may be issued for a vessel that qualifies under the laws of the United States to engage in the coastwise trade. .\n##### (b) Regulations\nNot later than 90 days after the date of the enactment of this Act, the Commandant of the United States Coast Guard shall issue regulations to implement the amendment made by subsection (a) that require all vessels permitted to engage in the coastwise trade to meet all appropriate safety and security requirements.\n##### (c) Conforming amendments\n**(1) Tank vessel construction standards**\nSection 3703a(c)(1)(C) of title 46, United States Code, is amended by striking and is qualified for documentation as a wrecked vessel under section 12112 of this title .\n**(2) Liquified gas tankers**\nSection 12120 of such title is amended by striking , if the vessel\u2014 and all that follows and inserting a period.\n**(3) Small passenger vessels**\nSection 12121(b) of such title is amended\u2014\n**(A)**\nby striking 12112, ; and\n**(B)**\nby striking 12132, .\n**(4) Loss of coastwise trade privileges**\nSection 12132 of such title is repealed.\n**(5) Oil spill response vessels**\nSection 12117(b) of such title is amended by striking sections 12103, 12132, and 50501 and inserting sections 12103 and 50501 .\n**(6) Optional regulatory measurement**\nSection 14305(a)(6) of such title is amended by striking sections 12118 and 12132 and inserting section 12118 .\n**(7) Court sales of undocumented vessels**\nSection 31329(b) of such title is amended\u2014\n**(A)**\nin paragraph (1), by striking ; and inserting ; and ;\n**(B)**\nin paragraph (2), by striking ; and and inserting a period; and\n**(C)**\nby striking paragraph (3).\n**(8) Clerical amendment**\nThe table of sections for chapter 121 of title 46, United States Code, is amended by striking the item relating to section 12132.",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-06-12",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2043",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Open America's Waters Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-14T18:35:06Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3940ih.xml"
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
      "title": "Open America's Waters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Open America's Waters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the Jones Act restrictions on coastwise trade, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T04:48:26Z"
    }
  ]
}
```
