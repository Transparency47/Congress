# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1830?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1830
- Title: Right to Treat Act
- Congress: 119
- Bill type: S
- Bill number: 1830
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2026-04-06T20:30:38Z
- Update date including text: 2026-04-06T20:30:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1830",
    "number": "1830",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Right to Treat Act",
    "type": "S",
    "updateDate": "2026-04-06T20:30:38Z",
    "updateDateIncludingText": "2026-04-06T20:30:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
        "item": [
          {
            "date": "2026-03-19T14:00:30Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T15:54:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1830is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1830\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Johnson introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo clarify that agencies of the Department of Health and Human Services do not have the authority to regulate the practice of medicine.\n#### 1. Short title\nThis Act may be cited as the Right to Treat Act .\n#### 2. Scope of authorities\n##### (a) In general\nSubject to subsection (b) and notwithstanding any other provision of law\u2014\n**(1)**\nno Federal agency, including the Food and Drug Administration, the National Institutes of Health, and the Centers for Disease Control and Prevention, shall have the authority to regulate the practice of medicine; and\n**(2)**\nno Federal law, rule, regulation, or policy shall prohibit or restrict the prescription or disbursement for an unapproved use of any drug that is approved by the Food and Drug Administration, or that is available pursuant to section 561B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20130a ).\n##### (b) Rule of construction\nNothing in this Act shall be construed to affect any Federal law, rule, regulation, or policy that restricts abortion, assisted suicide, euthanasia, mercy killing, coercive family planning, female genital mutilation, or gender transition medical interventions.",
      "versionDate": "2025-05-21",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-06T20:30:37Z"
          },
          {
            "name": "Centers for Disease Control and Prevention (CDC)",
            "updateDate": "2026-04-06T20:30:27Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2026-04-06T20:30:17Z"
          },
          {
            "name": "Food and Drug Administration (FDA)",
            "updateDate": "2026-04-06T20:30:21Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-04-06T20:30:34Z"
          },
          {
            "name": "National Institutes of Health (NIH)",
            "updateDate": "2026-04-06T20:30:24Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2026-04-06T20:30:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-03T12:26:36Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1830is.xml"
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
      "title": "Right to Treat Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Right to Treat Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify that agencies of the Department of Health and Human Services do not have the authority to regulate the practice of medicine.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:22Z"
    }
  ]
}
```
