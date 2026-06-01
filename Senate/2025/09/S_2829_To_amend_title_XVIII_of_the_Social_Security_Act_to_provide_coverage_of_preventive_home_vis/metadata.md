# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2829?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2829
- Title: Preventive Home Visit Act
- Congress: 119
- Bill type: S
- Bill number: 2829
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2025-11-18T19:47:59Z
- Update date including text: 2025-11-18T19:47:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2829",
    "number": "2829",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Preventive Home Visit Act",
    "type": "S",
    "updateDate": "2025-11-18T19:47:59Z",
    "updateDateIncludingText": "2025-11-18T19:47:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T16:32:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2829is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2829\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. King introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide coverage of preventive home visits under Medicare, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventive Home Visit Act .\n#### 2. Medicare coverage of preventive home visits\n##### (a) In general\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)\u2014\n**(A)**\nin subparagraph (JJ), by adding and after the semicolon; and\n**(B)**\nby adding at the end the following new subparagraph:\n(KK) a preventive home visit (as defined in subsection (nnn)); ; and\n**(2)**\nby adding at the end the following new subsection:\n(nnn) Preventive home visit The term preventive home visit means a visit to the home of an individual by a qualified professional or team of professionals (as defined by the Secretary), not more frequently than once every 2 years, during which the qualified professional provides an assessment of the home environment of the individual, identifies health risks, and provides referrals, as appropriate, for interventions or home modifications to improve physical function, balance, strength and mobility, reduce other falls risk factors, or enhance nutrition with respect to the individual. The preventive home visit can be conducted in-person, remotely, or a combination thereof. .\n##### (b) Payment\n**(1) In general**\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(A)**\nby striking and (HH) and inserting (HH) ; and\n**(B)**\nby inserting before the semicolon at the end the following: and (II) with respect to a preventive home visit (as defined in section 1861(nnn)), the amount paid shall be equal to 100 percent of the lesser of the actual charge for the service or the amount determined under section 1834(aa) .\n**(2) Payment determination**\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(aa) Preventive home visits The Secretary shall establish a bundled payment amount for a preventive home visit (as defined in section 1861(nnn)), including any referrals made in connection with the visit. .\n##### (c) Frequency limitation\nSection 1862(a)(1) of the Social Security Act ( 42 U.S.C. 1395y(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (O), by striking and at the end;\n**(2)**\nin subparagraph (P), by inserting and after the semicolon; and\n**(3)**\nby adding at the end the following new subparagraph:\n(Q) in the case of a preventive home visit (as defined in section 1861(nnn)), which is provided more frequently than is covered under such section. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to services furnished on or after January 1, 2027.",
      "versionDate": "2025-09-17",
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
        "updateDate": "2025-11-18T19:47:59Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2829is.xml"
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
      "title": "Preventive Home Visit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventive Home Visit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide coverage of preventive home visits under Medicare, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:18Z"
    }
  ]
}
```
