# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1132
- Title: Families Care Act
- Congress: 119
- Bill type: S
- Bill number: 1132
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1132",
    "number": "1132",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Families Care Act",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:40:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Lujan",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1132is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1132\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Budd (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Older Americans Act of 1965 to include peer supports as a supportive service within the National Family Caregiver Support Program, to require States to consider the unique needs of caregivers whose families have been impacted by substance use disorder, including opioid use disorder, in providing services under such program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Families Care Act .\n#### 2. National Family Caregiver Support Program\nSection 373 of the Older Americans Act of 1965 ( 42 U.S.C. 3030s\u20131 ) is amended\u2014\n**(1)**\nin subsection (b)(3), by inserting peer supports, after individual counseling, ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin the subsection heading, by striking Priority and inserting priority; consideration ; and\n**(B)**\nby adding at the end the following:\n(3) Consideration In providing services under this part, the State shall consider the circumstances and unique needs of different types of caregivers, including the needs of children and their older relative caregivers whose families have been affected by substance use disorder, including opioid use disorder. ; and\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking Not later than and all that follows through the Assistant Secretary shall and inserting The Assistant Secretary shall, on a regular basis ; and\n**(B)**\nin paragraph (2), by striking make available and inserting prepare, publish, and disseminate .",
      "versionDate": "2025-03-26",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-04-09T14:03:43Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1132is.xml"
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
      "title": "Families Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Families Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Older Americans Act of 1965 to include peer supports as a supportive service within the National Family Caregiver Support Program, to require States to consider the unique needs of caregivers whose families have been impacted by substance use disorder, including opioid use disorder, in providing services under such program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:33:22Z"
    }
  ]
}
```
