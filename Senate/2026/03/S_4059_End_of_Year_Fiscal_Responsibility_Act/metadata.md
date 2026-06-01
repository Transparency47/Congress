# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4059?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4059
- Title: End-of-Year Fiscal Responsibility Act
- Congress: 119
- Bill type: S
- Bill number: 4059
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-05-01T18:43:26Z
- Update date including text: 2026-05-01T18:43:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2026-03-18 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2026-03-18 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4059",
    "number": "4059",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "End-of-Year Fiscal Responsibility Act",
    "type": "S",
    "updateDate": "2026-05-01T18:43:26Z",
    "updateDateIncludingText": "2026-05-01T18:43:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-18T18:30:06Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-11T18:33:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4059is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4059\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo provide requirements for Executive agency spending at the end of a fiscal year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End-of-Year Fiscal Responsibility Act .\n#### 2. Definitions\nIn this Act:\n**(1) Covered period**\nThe term covered period means the 2-month period immediately preceding the end of a fiscal year.\n**(2) Discretionary appropriations**\nThe term discretionary appropriations has the meaning given the term in section 250(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 900(c) ).\n**(3) Executive agency**\nThe term Executive agency has the meaning given the term in section 105 of title 5, United States Code.\n#### 3. Requirements for Executive agency spending at the end of a fiscal year\n##### (a) In general\nExcept as provided in subsection (c), the amount of discretionary appropriations obligated by an Executive agency during each month of a covered period may not exceed the average monthly amount of discretionary appropriations obligated by the Executive agency during the 10-month period immediately preceding the covered period.\n##### (b) Report\nNot later than 60 days after the end of each fiscal year, each Executive agency shall submit to Congress and post on a publicly available website an itemized list of discretionary appropriations obligated by the Executive agency during the covered period immediately preceding the date on which the report is submitted.\n##### (c) Exception\nThis section shall not apply with respect to any discretionary appropriations obligated by an Executive agency for national security-related activities or disaster relief efforts.",
      "versionDate": "2026-03-11",
      "versionType": "Introduced in Senate"
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
            "name": "Appropriations",
            "updateDate": "2026-05-01T18:43:25Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-01T18:43:21Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-05-01T18:43:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-24T01:24:30Z"
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
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4059is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "End-of-Year Fiscal Responsibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End-of-Year Fiscal Responsibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide requirements for Executive agency spending at the end of a fiscal year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T04:03:34Z"
    }
  ]
}
```
