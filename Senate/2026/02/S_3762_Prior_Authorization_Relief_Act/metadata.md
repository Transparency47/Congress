# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3762?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3762
- Title: Prior Authorization Relief Act
- Congress: 119
- Bill type: S
- Bill number: 3762
- Origin chamber: Senate
- Introduced date: 2026-02-03
- Update date: 2026-04-14T11:03:26Z
- Update date including text: 2026-04-14T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in Senate
- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-03: Introduced in Senate

## Actions

- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3762",
    "number": "3762",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Prior Authorization Relief Act",
    "type": "S",
    "updateDate": "2026-04-14T11:03:26Z",
    "updateDateIncludingText": "2026-04-14T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T16:15:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3762is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3762\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2026 Mr. Whitehouse introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend part C of title XVIII of the Social Security Act to provide for prior authorization reforms under the Medicare Advantage program.\n#### 1. Short title\nThis Act may be cited as the Prior Authorization Relief Act .\n#### 2. Medicare Advantage program prior authorization reforms\n##### (a) Medicare Advantage\nSection 1859 of the Social Security Act ( 42 U.S.C. 1395w\u201328 ) is amended by adding at the end the following new subsection:\n(j) Prior authorization requirements (1) Audit Not later than January 1, 2027, the Secretary shall conduct an audit of prior authorization requirements for items and services furnished, and covered part D drugs prescribed, to enrollees under this part in order to identify the items and services and covered part D drugs that the Secretary determines meet each of the following criteria: (A) Reimbursement for such item or service or covered part D drug under this part is in the top 10 percent of reimbursements for all items and services and covered part D drugs under this part. (B) There is sufficient clinical evidence to establish a standard medical policy for the prior authorization process for such item or service or covered part D drug. (C) Prior authorization for such item or service or covered part D drug requires an excessive number of steps to complete the required protocols. (2) Standardized requirements Not later than May 1, 2028, taking into account the results of the audit conducted under paragraph (1), the Secretary shall promulgate a final rule to standardize the prior authorization requirements (including supplemental forms) for items and services and covered part D drugs identified under paragraph (1) across all Medicare Advantage plans, including MA\u2013PD plans. (3) Exemption from requirements (A) In general Subject to subparagraph (B), the prior authorization requirements under paragraph (2) for the items and services and covered part D drugs identified under paragraph (1) shall not apply when such items and services are furnished by, or such covered part D drugs are prescribed by, a provider of services or supplier that is participating in a two-sided risk model tested or implemented under section 1115A or this title, including an accountable care organization under section 1899, where the model is at risk for both potential losses and gains. (B) Limitation The Secretary shall establish a process under which an MA organization offering a Medicare Advantage plan (including an MA\u2013PD plan) may request that the exemption under subparagraph (A) not apply with respect to items and services and covered part D drugs furnished to enrollees under the plan and that the prior authorization requirements that would otherwise apply under the plan for such items and services and covered part D drugs continue to apply. .",
      "versionDate": "2026-02-03",
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
        "updateDate": "2026-02-25T17:16:04Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3762is.xml"
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
      "title": "Prior Authorization Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prior Authorization Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend part C of title XVIII of the Social Security Act to provide for prior authorization reforms under the Medicare Advantage program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:03:25Z"
    }
  ]
}
```
