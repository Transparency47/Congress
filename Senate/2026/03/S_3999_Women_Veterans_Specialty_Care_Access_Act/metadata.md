# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3999?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3999
- Title: Women Veterans Specialty Care Access Act
- Congress: 119
- Bill type: S
- Bill number: 3999
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3999",
    "number": "3999",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Women Veterans Specialty Care Access Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
            "date": "2026-04-29T21:37:36Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-05T16:39:48Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3999is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3999\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mrs. Blackburn (for herself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to ensure that women veterans may schedule appointments for women\u2019s specialty care under the laws administered by the Secretary without requiring a referral, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Women Veterans Specialty Care Access Act .\n#### 2. Direct scheduling of women\u2019s specialty care for women veterans\n##### (a) In general\nThe Secretary of Veterans Affairs shall ensure that any covered veteran may directly schedule an appointment for women\u2019s specialty care, including through the Veterans Community Care Program under section 1703 of title 38, United States Code, without requiring a referral from a primary care provider of the Department of Veterans Affairs.\n##### (b) Availability\nThe Secretary shall ensure that direct scheduling under subsection (a) is available\u2014\n**(1)**\nthrough each medical center or clinic of the Department that offers women\u2019s specialty care; and\n**(2)**\nvia telephone, online scheduling tools, and any other modality used by the Department for scheduling of specialty care.\n##### (c) Prohibition on additional administrative barriers\nThe Secretary may not require any additional approval, referral, or screening step as a condition of a covered veteran accessing women\u2019s specialty care.\n##### (d) Rule of construction\nNothing in this section shall be construed to alter or waive eligibility or access standards for the receipt of care or services under section 1703 of title 38, United States Code.\n##### (e) Definitions\nIn this section:\n**(1) Covered veteran**\nThe term covered veteran means a woman veteran enrolled in the system of annual patient enrollment of the Department of Veterans Affairs established and operated under section 1705(a) of title 38, United States Code, who is eligible for the receipt of women\u2019s specialty care under the laws administered by the Secretary.\n**(2) Women\u2019s specialty care**\nThe term women\u2019s specialty care means gynecology care, obstetrics care, maternity care, and postpartum care.",
      "versionDate": "2026-03-05",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-24T01:06:19Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3999is.xml"
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
      "title": "Women Veterans Specialty Care Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Women Veterans Specialty Care Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Veterans Affairs to ensure that women veterans may schedule appointments for women's specialty care under the laws administered by the Secretary without requiring a referral, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:03:25Z"
    }
  ]
}
```
