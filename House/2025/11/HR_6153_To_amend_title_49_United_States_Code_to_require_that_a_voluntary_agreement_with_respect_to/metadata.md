# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6153
- Title: Communities Before Air Tourism Act
- Congress: 119
- Bill type: HR
- Bill number: 6153
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-01-07T09:05:43Z
- Update date including text: 2026-01-07T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-20 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-20 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6153",
    "number": "6153",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Communities Before Air Tourism Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:43Z",
    "updateDateIncludingText": "2026-01-07T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-20T18:24:02Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NJ"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "HI"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6153ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6153\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Menendez (for himself, Mr. Goldman of New York , Mr. Nadler , Ms. Pou , Mr. Case , and Mr. Pallone ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to require that a voluntary agreement with respect to commercial air tour operations over a national park considers the well-being of communities overflown by aircraft involved in such operations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Communities Before Air Tourism Act .\n#### 2. Park protection\nSection 40128(b)(7) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B) by striking or the air traffic control system and inserting , the air traffic control system, or the well-being of communities overflown by aircraft involved in such commercial air tour operations ; and\n**(2)**\nin subparagraph (C) by inserting any community whose lands are, or may be, and before any Indian tribe .",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-12-04T15:52:49Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6153ih.xml"
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
      "title": "Communities Before Air Tourism Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T10:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Communities Before Air Tourism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T10:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require that a voluntary agreement with respect to commercial air tour operations over a national park considers the well-being of communities overflown by aircraft involved in such operations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T10:18:34Z"
    }
  ]
}
```
