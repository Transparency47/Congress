# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2132
- Title: Marianas Air Service Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 2132
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-06-25T08:06:33Z
- Update date including text: 2025-06-25T08:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Aviation.
- 2025-03-14 - IntroReferral: Sponsor introductory remarks on measure. (CR E216)
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Aviation.
- 2025-03-14 - IntroReferral: Sponsor introductory remarks on measure. (CR E216)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2132",
    "number": "2132",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000404",
        "district": "",
        "firstName": "Kimberlyn",
        "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
        "lastName": "King-Hinds",
        "party": "R",
        "state": "MP"
      }
    ],
    "title": "Marianas Air Service Improvement Act",
    "type": "HR",
    "updateDate": "2025-06-25T08:06:33Z",
    "updateDateIncludingText": "2025-06-25T08:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E216)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T22:08:46Z",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2132ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2132\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Ms. King-Hinds introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to exempt Northern Mariana Islands from certain eligibility requirements for essential air service program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Marianas Air Service Improvement Act .\n#### 2. Exception for locations in Northern Mariana Islands\nSection 41731(c) of title 49, United States Code, is amended to read as follows:\n(c) Exception for locations in Alaska, Hawaii, and Northern Mariana Islands Subparagraphs (B), (C), and (D) of subsection (a)(1) shall not apply with respect to locations in the State of Alaska, the State of Hawaii, or the Northern Mariana Islands. .",
      "versionDate": "2025-03-14",
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
        "updateDate": "2025-04-01T17:46:05Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2132ih.xml"
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
      "title": "Marianas Air Service Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Marianas Air Service Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to exempt Northern Mariana Islands from certain eligibility requirements for essential air service program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:38Z"
    }
  ]
}
```
