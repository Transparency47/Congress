# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/984
- Title: To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide timely equitable relief to an individual who suffers a loss based on an administrative error by the Secretary, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 984
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-12-20T09:06:45Z
- Update date including text: 2025-12-20T09:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-07 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-07 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/984",
    "number": "984",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide timely equitable relief to an individual who suffers a loss based on an administrative error by the Secretary, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-12-20T09:06:45Z",
    "updateDateIncludingText": "2025-12-20T09:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-07",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-11T16:40:16Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-07T22:44:48Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr984ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 984\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Van Orden introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide timely equitable relief to an individual who suffers a loss based on an administrative error by the Secretary, and for other purposes.\n#### 1. Improvements to equitable relief in the case of an administrative error by the Secretary of Veterans Affairs\n##### (a) Affirmative duty To provide timely equitable relief\nSection 503 of title 38, United States Code, is amended by striking may both places it appears and inserting shall, not later than 120 days after such determination, .\n##### (b) Cancellation of debt collection\nSection 5314 of such title is amended, in subsection (a), by adding at the end the following new paragraph:\n(3) The Secretary shall promptly cancel any agreement, entered into by the Secretary with a debt collector (as defined in section 803 of the Fair Debt Collection Practices Act ( 15 U.S.C. 1692a )) to collect an amount of indebtedness described in paragraph (1), if the Secretary determines that the determination of such indebtedness was in error. .",
      "versionDate": "2025-02-05",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-04-11T18:26:12Z"
          },
          {
            "name": "Debt collection",
            "updateDate": "2025-04-11T18:26:19Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-04-11T18:26:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-19T16:01:21Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr984ih.xml"
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
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide timely equitable relief to an individual who suffers a loss based on an administrative error by the Secretary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:47Z"
    },
    {
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide timely equitable relief to an individual who suffers a loss based on an administrative error by the Secretary, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T09:06:25Z"
    }
  ]
}
```
