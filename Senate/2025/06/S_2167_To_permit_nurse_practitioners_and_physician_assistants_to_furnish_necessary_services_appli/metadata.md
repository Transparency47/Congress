# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2167
- Title: Health Care for Energy Workers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2167
- Origin chamber: Senate
- Introduced date: 2025-06-25
- Update date: 2026-03-05T12:03:19Z
- Update date including text: 2026-03-05T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in Senate
- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-25: Introduced in Senate

## Actions

- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2167",
    "number": "2167",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Health Care for Energy Workers Act of 2025",
    "type": "S",
    "updateDate": "2026-03-05T12:03:19Z",
    "updateDateIncludingText": "2026-03-05T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
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
            "date": "2025-06-25T21:32:48Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-25T21:32:48Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "TN"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "WA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2167is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2167\nIN THE SENATE OF THE UNITED STATES\nJune 25 (legislative day, June 24), 2025 Mr. Hickenlooper (for himself, Mrs. Blackburn , and Mrs. Murray ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo permit nurse practitioners and physician assistants to furnish necessary services, appliances, and supplies to individuals receiving medical benefits for illnesses.\n#### 1. Short title\nThis Act may be cited as the Health Care for Energy Workers Act of 2025 .\n#### 2. Expansion of authority to furnish medical benefits\nSection 3629 of the Energy Employees Occupational Illness Compensation Program Act of 2000 ( 42 U.S.C. 7384t ) is amended\u2014\n**(1)**\nby redesignating subsections (c) through (f) as subsections (d) through (g), respectively; and\n**(2)**\nby inserting after subsection (b) the following new subsection (c):\n(c) Orders by nurse practitioners and physician assistants For purposes of subsections (a) and (b), a nurse practitioner or physician assistant, acting within the scope of their practice under State law and in accordance with such regulations and instructions as the President deems necessary, may prescribe, recommend, or order services, appliances, and supplies for an individual receiving medical benefits under this section for an illness. .",
      "versionDate": "2025-06-25",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-25",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4122",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Health Care for Energy Workers Act of 2025",
      "type": "HR"
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
        "name": "Health",
        "updateDate": "2025-07-15T10:44:00Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2167is.xml"
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
      "title": "Health Care for Energy Workers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Care for Energy Workers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permit nurse practitioners and physician assistants to furnish necessary services, appliances, and supplies to individuals receiving medical benefits for illnesses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:21Z"
    }
  ]
}
```
