# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3101
- Title: SAFE KIDS Act
- Congress: 119
- Bill type: S
- Bill number: 3101
- Origin chamber: Senate
- Introduced date: 2025-11-04
- Update date: 2026-02-02T14:48:14Z
- Update date including text: 2026-02-02T14:48:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in Senate
- 2025-11-04 - IntroReferral: Introduced in Senate
- 2025-11-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-04: Introduced in Senate

## Actions

- 2025-11-04 - IntroReferral: Introduced in Senate
- 2025-11-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3101",
    "number": "3101",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "SAFE KIDS Act",
    "type": "S",
    "updateDate": "2026-02-02T14:48:14Z",
    "updateDateIncludingText": "2026-02-02T14:48:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-04",
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
            "date": "2025-11-04T22:44:18Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-04T22:44:18Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3101is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3101\nIN THE SENATE OF THE UNITED STATES\nNovember 4, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prevent citizens of foreign adversarial nations from entering into or enforcing surrogacy contracts in the United States.\n#### 1. Short title\nThis Act may be cited as the Stopping Adversarial Foreign Exploitation of Kids In Domestic Surrogacy Act or the SAFE KIDS Act .\n#### 2. Findings and purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nCitizens of foreign entities of concern are exploiting commercial surrogacy laws in the United States.\n**(2)**\nMany developed countries ban international commercial surrogacy altogether. The United States, however, presently allows even citizens of foreign entities of concern to solicit and pay financially-distressed Americans to give birth to their children in the United States and then send these infants abroad.\n**(3)**\nThis presents an acute national security threat, and recent events in Arcadia, California reveal that surrogacy is even being used to facilitate human trafficking.\n##### (b) Purposes\nThis Act\u2014\n**(1)**\nacknowledges that foreign persons (including nationals of foreign entities of concern) are abusing surrogacy agreements to exploit women in the United States and to obtain United States citizenship for their children;\n**(2)**\ninvalidates surrogate parentage contracts between prospective parents from foreign entities of concern and a surrogate mother in the United States; and\n**(3)**\nimposes criminal penalties on surrogacy brokers who commercially facilitate such invalid agreements.\n#### 3. Definitions\nIn this Act:\n**(1) Foreign entity of concern**\nThe term foreign entity of concern means any foreign nation listed under section 4872(f)(2) of title 10, United States Code.\n**(2) Prospective parent**\nThe term prospective parent means an individual who, directly or indirectly, enters into a surrogacy agreement to become the legal or custodial parent of a child birthed by a surrogate parent.\n**(3) Surrogacy agreement**\n**(A) In general**\nThe term surrogacy agreement means a contract, agreement, or arrangement, without regard to whether it is oral or written or is direct or brokered, between 1 or more prospective parents and a surrogate parent, under which the surrogate parent agrees to become pregnant and give birth to a child, and, subject to subparagraph (B), to relinquish all parental rights and responsibilities to the prospective parent or parents.\n**(B) Presumption**\nWith respect to a contract, agreement, or arrangement, without regard to whether it is oral or written or is direct or brokered, under which a surrogate parent agrees to become pregnant and give birth to a child that does not expressly address parental or custodial rights, there shall be a presumption that the surrogate parent has agreed to relinquish her parental or custodial rights, and that the contract, agreement, or arrangement is a surrogacy agreement, if the contract, agreement, or arrangement is with a prospective parent who is a citizen or permanent resident of a foreign entity of concern.\n**(4) Surrogacy broker**\nThe term surrogacy broker means any individual or entity that induces, arranges, procures, facilitates, or otherwise assists in the formation or execution of a surrogacy agreement.\n**(5) Surrogate parent**\nThe term surrogate parent means a person who agrees to become pregnant and give birth to a child, and to relinquish all parental rights and responsibilities to another person under the terms of a surrogacy agreement.\n#### 4. Certain international surrogate parentage contracts void and unenforceable\n##### (a) In general\nSubject to subsection (b), a surrogacy agreement shall be void and unenforceable if the agreement is between a surrogate parent who is in the United States at the time of birth or who is a citizen or lawful permanent resident of the United States and\u2014\n**(1)**\na prospective parent who is a citizen or permanent resident of a foreign entity of concern; or\n**(2)**\na surrogacy broker who arranges a surrogacy agreement with a prospective parent who is a citizen or permanent resident of a foreign entity of concern.\n##### (b) Exception\nSubsection (a) shall not invalidate a surrogacy agreement between a surrogate parent and 2 prospective parents, if\u2014\n**(1)**\nthe 2 prospective parents are legally married; and\n**(2)**\nat least 1 prospective parent is a citizen or lawful permanent resident of the United States.\n#### 5. Commercial facilitation of foreign surrogacy prohibited; penalty\nA surrogacy broker who knowingly or recklessly induces, arranges, procures, facilitates, or otherwise assists in the formation or execution of a surrogacy agreement that is void and unenforceable under section 4 shall be fined under title 18, United States Code, imprisoned for not more than 1 year, or both.\n#### 6. Custody of child when international surrogate parentage contracts are void and unenforceable\nLegal custody of a child born pursuant to a surrogacy agreement that is void and unenforceable under section 4 shall be decided based on a determination of the best interests of the child under the law of the State where the surrogate parent resides, with no effect given to the surrogacy agreement or any other purported agreement, contract, or understanding concerning the custody of the child.",
      "versionDate": "2025-11-04",
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
        "actionDate": "2026-01-21",
        "text": "Sponsor introductory remarks on measure. (CR H1161-1162)"
      },
      "number": "7040",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAFE KIDS Act",
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
        "name": "Immigration",
        "updateDate": "2025-11-19T15:20:14Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3101is.xml"
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
      "title": "SAFE KIDS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE KIDS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T07:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stopping Adversarial Foreign Exploitation of Kids In Domestic Surrogacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T07:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prevent citizens of foreign adversarial nations from entering into or enforcing surrogacy contracts in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T07:03:27Z"
    }
  ]
}
```
