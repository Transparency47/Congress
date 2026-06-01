# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5957?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5957
- Title: Connecting Veterans to Care Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5957
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2026-01-07T09:05:46Z
- Update date including text: 2026-01-07T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-08 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-08 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5957",
    "number": "5957",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Connecting Veterans to Care Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:46Z",
    "updateDateIncludingText": "2026-01-07T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-08",
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
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-08T18:12:33Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5957ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5957\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Kean introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to provide eligibility for urbanized area formula grants for public transportation that services Department of Veterans Affairs medical facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Connecting Veterans to Care Act of 2025 .\n#### 2. Assistance for operating costs for public transportation that services department of veterans affairs medical facilities\nSection 5307 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1)(D) by striking public transportation in an urbanized area and all that follows through the period at the end and inserting the following:\npublic transportation\u2014 (i) in an urbanized area with a population of fewer than 200,000 individuals, as determined by the Bureau of the Census; or (ii) that services a Department of Veterans Affairs medical facility. ;\n**(2)**\nby redesignating subsection (h) as subsection (i); and\n**(3)**\nby inserting after subsection (g) the following:\n(h) Certification of use of certain funds (1) Certification The recipient of financial assistance described in subsection (a)(1)(D)(ii) shall, not later than the 30 days after the date on which the recipient first receives grant funds under this section, and each year thereafter, submit to the Secretary a certification that the operating costs will be used to provide public transportation that services a Department of Veterans Affairs medical facility. (2) Penalty If the Secretary finds that a recipient failed to provide transportation as certified to under paragraph (1) during a fiscal year, the Secretary shall suspend assistance provided under this section for such operating costs. .",
      "versionDate": "2025-11-07",
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
        "updateDate": "2025-11-19T12:49:36Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5957ih.xml"
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
      "title": "Connecting Veterans to Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T10:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Connecting Veterans to Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T10:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to provide eligibility for urbanized area formula grants for public transportation that services Department of Veterans Affairs medical facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T10:03:13Z"
    }
  ]
}
```
