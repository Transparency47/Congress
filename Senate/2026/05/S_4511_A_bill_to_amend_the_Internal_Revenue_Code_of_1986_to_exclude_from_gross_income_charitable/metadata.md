# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4511
- Title: A bill to amend the Internal Revenue Code of 1986 to exclude from gross income charitable distributions from certain employer-sponsored retirement plans, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4511
- Origin chamber: Senate
- Introduced date: 2026-05-13
- Update date: 2026-05-28T20:36:55Z
- Update date including text: 2026-05-28T20:36:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in Senate
- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-13: Introduced in Senate

## Actions

- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4511",
    "number": "4511",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income charitable distributions from certain employer-sponsored retirement plans, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-28T20:36:55Z",
    "updateDateIncludingText": "2026-05-28T20:36:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
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
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T17:41:20Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "DE"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "KS"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4511is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4511\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2026 Mr. Cramer (for himself, Mr. Coons , Mr. Marshall , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income charitable distributions from certain employer-sponsored retirement plans, and for other purposes.\n#### 1. Exclusion from gross income of charitable distributions from certain employer-sponsored retirement plans\n##### (a) In general\nSection 402 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(m) Distributions for charitable purposes (1) In general Gross income for any taxable year shall not include so much of the aggregate amount of qualified charitable distributions made with respect to a taxpayer during such taxable year which does not exceed the applicable amount. (2) Qualified charitable distribution For purposes of this subsection, the term qualified charitable distribution means any distribution from a qualified employer plan\u2014 (A) which is made directly by the plan to an organization described in section 170(b)(1)(A) (other than any organization described in section 509(a)(3) or any fund or account described in section 4966(d)(2)), and (B) which is made on or after the date that the individual on whose behalf the distribution is made has attained age 70 1/2 . A distribution shall be treated as a qualified charitable distribution only to the extent that the distribution would be includible in gross income without regard to paragraph (1). (3) Special rules (A) In general Rules similar to the rules of subparagraphs (C), (E), and (F) of section 408(d)(8) shall apply for purposes of this subsection. (B) Application of section 72 Rules similar to the rules of section 408(d)(8)(D) shall apply for purposes of this subsection, by taking into account all amounts to which the taxpayer has a nonforfeitable right in all qualified employer plans maintained by the employer in lieu of all amounts in all individual retirement plans of the individual. (4) Definitions For purposes of this subsection\u2014 (A) Applicable amount The term applicable amount means the excess of\u2014 (i) the dollar amount in effect under section 408(d)(8) for the taxable year, over (ii) the total amount of distributions not includible in the gross income of the taxpayer for the taxable year by reason of section 408(d)(8). (B) Qualified employer plan The term qualified employer plan means\u2014 (i) an eligible retirement plan described in clause (iii) or (vi) of subsection (c)(8)(B), or (ii) a plan established for its employees by the United States, by a State or political subdivision thereof, or by an agency or instrumentality of any of the foregoing. .\n##### (b) SEPs and SIMPLEs\nSection 408(d)(8)(B) of such Code is amended by striking (other than a plan described in subsection (k) or (p)) .\n##### (c) 403(b) plans\nSection 403 of such Code is amended by adding at the end the following new subsection:\n(d) Distributions for charitable purposes The rules of section 402(m) shall apply to distributions under an annuity contract described in subsection (b). .\n##### (d) 457(b) plans\nSection 457(e) of such Code is amended by adding at the end the following new paragraph:\n(19) Distributions for charitable purposes The rules of section 402(m) shall apply to distributions under an eligible deferred compensation plan established and maintained by an eligible employer described in subsection (e)(1)(A). .\n##### (e) Effective date\nThe amendments made by this section shall apply to distributions made in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2026-05-13",
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
        "name": "Taxation",
        "updateDate": "2026-05-28T20:36:55Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4511is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income charitable distributions from certain employer-sponsored retirement plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:35Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income charitable distributions from certain employer-sponsored retirement plans, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T10:56:24Z"
    }
  ]
}
```
