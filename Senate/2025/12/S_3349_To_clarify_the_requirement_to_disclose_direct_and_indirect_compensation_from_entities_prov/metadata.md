# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3349?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3349
- Title: PBM Disclosure Act
- Congress: 119
- Bill type: S
- Bill number: 3349
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T17:18:52Z
- Update date including text: 2026-01-07T17:18:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3349",
    "number": "3349",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "PBM Disclosure Act",
    "type": "S",
    "updateDate": "2026-01-07T17:18:52Z",
    "updateDateIncludingText": "2026-01-07T17:18:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
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
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T18:33:40Z",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3349is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3349\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Marshall (for himself and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo clarify the requirement to disclose direct and indirect compensation from entities providing pharmacy benefit management services or third party administration services.\n#### 1. Short title\nThis Act may be cited as the PBM Disclosure Act .\n#### 2. Clarification of requirement to disclose direct and indirect compensation for brokers and consultants to employer-sponsored health plans\n##### (a) In general\nSection 408(b)(2)(B)(ii)(I)(bb) of the Employee Retirement Income Security Act of 1974 (29 U.S.C. 1108(b)(2)(B)(ii)(I)(bb)) is amended by adding at the end the following:\n(CC) Pharmacy benefit management services provided by pharmacy benefit managers or other service providers and related services provided by third party administrators (or other entities providing such services) for which the covered service provider, an affiliate, or a subcontractor reasonably expects to receive indirect compensation or direct compensation described in item (dd). .\n##### (b) Regulations\nNot later than 180 days after the date of enactment of this Act, the Secretary of Labor shall promulgate regulations, through notice and comment rulemaking, clarifying the requirements of section 408(b)(2)(B) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1108(b)(2)(B) ) with respect to covered service providers providing services described in subitem (CC) of subclause (I)(bb) of such section, as amended by subsection (a). Such regulations shall apply with respect to any plan year that begins on or after the date that is 6 months after such regulations are promulgated.\n##### (c) Sense of Congress\nIt is the sense of Congress that the amendment made by subsection (a) clarifies the existing requirement of covered service providers with respect to services described in section 408(b)(2)(B)(ii)(I)(bb)(BB) of the Employee Retirement Income Security Act of 1974 (29 U.S.C. 1108(b)(2)(B)(ii)(I)(bb)(BB)) that were in effect since the application date described in section 202(e) of the No Surprises Act ( Public Law 116\u2013260 ; 29 U.S.C. 1108 note), and does not impose any additional requirement under section 408(b)(2)(B) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1108(b)(2)(B) ).",
      "versionDate": "2025-12-04",
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
        "name": "Health",
        "updateDate": "2026-01-07T17:18:52Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3349is.xml"
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
      "title": "PBM Disclosure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PBM Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify the requirement to disclose direct and indirect compensation from entities providing pharmacy benefit management services or third party administration services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:16Z"
    }
  ]
}
```
