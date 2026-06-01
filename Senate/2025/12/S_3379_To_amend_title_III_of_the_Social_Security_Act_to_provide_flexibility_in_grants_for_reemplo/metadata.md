# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3379
- Title: EARLY Benefits for Workers Act
- Congress: 119
- Bill type: S
- Bill number: 3379
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T17:14:17Z
- Update date including text: 2026-04-15T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3379",
    "number": "3379",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "EARLY Benefits for Workers Act",
    "type": "S",
    "updateDate": "2026-01-07T17:14:17Z",
    "updateDateIncludingText": "2026-04-15T16:27:19Z"
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
          "date": "2025-12-04T20:43:21Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "LA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3379is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3379\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Coons (for himself, Mr. Cassidy , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title III of the Social Security Act to provide flexibility in grants for reemployment services and eligibility assessments.\n#### 1. Short title\nThis Act may be cited as the Expedited Access to Reemployment Learning Yields Benefits for Workers Act or the EARLY Benefits for Workers Act .\n#### 2. Flexibility in grants for reemployment services and eligibility assessments\n##### (a) In general\nSection 306(a) of the Social Security Act ( 42 U.S.C. 506(a) ) is amended by adding at the end the following new subsection:\n(j) Authority for early interventions (1) In general In carrying out a State program of reemployment services and eligibility assessments using grant funds awarded to the State under this section, a State may use up to the lessor of 20 percent of such grant funds or $3,000,000 to provide reemployment services and eligibility assessment services and tools to claimants for regular compensation as soon as a claimant files an initial claim for regular compensation. (2) Determination of eligibility In adjudicating an initial claim for regular compensation with respect to a claimant, a State shall not make a determination that such claimant is ineligible for such regular compensation based solely on such claimant's failure to participate in the early interventions under paragraph (1) during the period between such initial claim and such claimant's first week of such regular compensation that is based on such initial claim. (3) Subsequent determination of ineligibility In the case where a claimant is provided reemployment services and eligibility assessment services and tools by a State pursuant to the early interventions under paragraph (1) but is subsequently determined by the State to be ineligible for regular compensation, the following shall apply: (A) Such claimant shall be ineligible to continue to be provided such reemployment services and eligibility assessment services and tools unless such services and tools are funded by another source or are generally available to members of the public. (B) Such State\u2014 (i) shall not be considered to be out of compliance with the terms and conditions of the grant program by reason of the provision of such reemployment services and eligibility assessment services and tools to such claimant prior to such determination; and (ii) shall not be required to return any grant funds used in providing such reemployment services and eligibility assessment services and tools to such claimant prior to such determination. (4) Clarification Nothing in this subsection shall preclude amounts expended by a State on the early interventions under paragraph (1) from being used to meet the threshold requirement under subsection (c)(2) if the expenditures otherwise meet the requirements for interventions under such subsection. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date of enactment of this Act.",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-07T17:14:17Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3379is.xml"
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
      "title": "EARLY Benefits for Workers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EARLY Benefits for Workers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expedited Access to Reemployment Learning Yields Benefits for Workers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title III of the Social Security Act to provide flexibility in grants for reemployment services and eligibility assessments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:16Z"
    }
  ]
}
```
