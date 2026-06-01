# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/497?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/497
- Title: FENCE Act
- Congress: 119
- Bill type: S
- Bill number: 497
- Origin chamber: Senate
- Introduced date: 2025-02-10
- Update date: 2025-05-05T18:46:41Z
- Update date including text: 2025-05-05T18:46:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-10: Introduced in Senate
- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-10: Introduced in Senate

## Actions

- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/497",
    "number": "497",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "FENCE Act",
    "type": "S",
    "updateDate": "2025-05-05T18:46:41Z",
    "updateDateIncludingText": "2025-05-05T18:46:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T22:06:55Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s497is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 497\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Mr. Hagerty introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify eligibility for 501(c)(3) status.\n#### 1. Short title\nThis Act may be cited as the Fixing Exemptions for Networks Choosing to Enable Illegal Migration Act or the FENCE Act .\n#### 2. Organizations harboring aliens unlawfully present in the United States\n##### (a) In general\nParagraph (3) of section 501(c) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking animals, no part and inserting \u201canimals\u2014\n(A) no part ,\n**(2)**\nby striking individual, no substantial part and inserting \u201cindividual,\n(B) no substantial part ,\n**(3)**\nby striking subsection (h)), and which and inserting \u201csubsection (h)),\n(C) which ,\n**(4)**\nby striking the period at the end and inserting , and , and\n**(5)**\nby adding at the end the following:\n(D) which does not engage in a pattern or practice of providing financial assistance, benefits, services, or other material support to individuals which such corporation, community chest, fund, or foundation knows or reasonably should know to be unlawfully present in the United States. Subparagraph (D) shall not be construed to require proof of citizenship or verification of an individual\u2019s immigration status to be presented, or to require a religious organization to act in violation of its religious beliefs. .\n##### (b) Effective date\nThe amendments made by this section shall take effect upon the date of the enactment of this Act.",
      "versionDate": "2025-02-10",
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
        "updateDate": "2025-05-05T18:46:41Z"
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
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s497is.xml"
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
      "title": "FENCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FENCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fixing Exemptions for Networks Choosing to Enable Illegal Migration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify eligibility for 501(c)(3) status.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:50Z"
    }
  ]
}
```
