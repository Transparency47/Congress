# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2216?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2216
- Title: To amend title 49, United States Code, to except from certain requirements relating to eligibility for essential air service Guam and the Northern Mariana Islands, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2216
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-06-12T08:06:44Z
- Update date including text: 2025-06-12T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-18 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-18 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2216",
    "number": "2216",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "To amend title 49, United States Code, to except from certain requirements relating to eligibility for essential air service Guam and the Northern Mariana Islands, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:44Z",
    "updateDateIncludingText": "2025-06-12T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-18T20:47:13Z",
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
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MP"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2216ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2216\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Moylan (for himself and Ms. King-Hinds ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to except from certain requirements relating to eligibility for essential air service Guam and the Northern Mariana Islands, and for other purposes.\n#### 1. Exception for certain locations\nSection 41731(c) of title 49, United States Code, is amended\u2014\n**(1)**\nin the subsection heading by striking Alaska and Hawaii and inserting Alaska, Guam, Hawaii, and the Northern Mariana Islands ; and\n**(2)**\nby striking State of Alaska or the State of Hawaii and inserting State of Alaska, the State of Hawaii, the territory of Guam, or the territory of the Northern Mariana Islands .",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-04-03T12:02:31Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2216ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to except from certain requirements relating to eligibility for essential air service Guam and the Northern Mariana Islands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T04:33:35Z"
    },
    {
      "title": "To amend title 49, United States Code, to except from certain requirements relating to eligibility for essential air service Guam and the Northern Mariana Islands, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T08:05:26Z"
    }
  ]
}
```
