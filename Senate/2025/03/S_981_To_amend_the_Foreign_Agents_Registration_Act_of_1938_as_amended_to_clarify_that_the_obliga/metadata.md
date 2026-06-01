# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/981
- Title: Foreign Agents Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 981
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-05T22:04:20Z
- Update date including text: 2025-12-05T22:04:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/981",
    "number": "981",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Foreign Agents Transparency Act",
    "type": "S",
    "updateDate": "2025-12-05T22:04:20Z",
    "updateDateIncludingText": "2025-12-05T22:04:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:25:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MI"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "IN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s981is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 981\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Grassley (for himself, Mr. Peters , Mr. Young , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Foreign Agents Registration Act of 1938, as amended to clarify that the obligation of individuals who formerly served as agents of foreign principals to register as foreign agents under the Act is continuing with respect to activities carried out previously on behalf of such foreign principals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Agents Transparency Act .\n#### 2. Clarifying the continuing obligation to register as an agent of a foreign principal\n##### (a) Obligation\nThe third sentence of section 2(a) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 612(a) ) is amended by striking for the period and inserting covering the period .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to any individual who serves as the agent of a foreign principal under the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611 et seq. )\u2014\n**(1)**\nduring the 5-year period ending on the date of enactment of this Act;\n**(2)**\non the date of enactment of this Act; or\n**(3)**\nafter the date of enactment of this Act.\n#### 3. Permitting order requiring compliance to apply after FARA activities have ended\n##### (a) Continual compliance\nSection 8(f) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 618(f) ) is amended\u2014\n**(1)**\nby inserting after the first sentence the following: The Attorney General may make application for an order requiring a person to comply with any appropriate provision of this Act or any regulation thereunder while the person acts as an agent of a foreign principal or at any time thereafter. ; and\n**(2)**\nby striking the period at the end and inserting the following: , including an order requiring a person to comply with section 2 with respect to any period during which the person acts as the agent of a foreign principal notwithstanding that the person does not act as the agent of a foreign principal at the time the court issues the order. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to any individual who serves as the agent of a foreign principal under the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611 et seq. )\u2014\n**(1)**\nduring the 5-year period ending on the date of enactment of this Act;\n**(2)**\non the date of enactment of this Act; or\n**(3)**\nafter the date of enactment of this Act.\n#### 4. Annual reports relating to compliance\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term covered action means an action taken by the Attorney General against a covered individual to enforce the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611 et seq. ), as amended by sections 2 and 3 of this Act; and\n**(2)**\nthe term covered individual means an individual who served as the agent of a foreign principal under the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611 et seq. ) during the 5-year period ending on the date of enactment of this Act.\n##### (b) In general\nNot later than 1 year after the date of enactment of this Act, and each year from that date thereafter, the Attorney General shall submit to the Committee on the Judiciary and the Committee on Foreign Relations of the Senate and the Committee on the Judiciary of the House of Representatives, as well as any other Member of Congress upon request of such Member, a written, machine-readable report that describes each covered action taken by the Attorney General.\n##### (c) Organization\nEach report submitted under subsection (b) shall be organized by each covered action taken and shall include, with respect to each covered action\u2014\n**(1)**\nthe name of each covered individual against whom the covered action was taken;\n**(2)**\na description of the rationale behind taking the covered action; and\n**(3)**\nthe status of the covered action.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-05-07",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3229",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Foreign Agents Transparency Act",
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
        "name": "International Affairs",
        "updateDate": "2025-05-22T14:59:22Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s981is.xml"
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
      "title": "Foreign Agents Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Foreign Agents Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Foreign Agents Registration Act of 1938, as amended to clarify that the obligation of individuals who formerly served as agents of foreign principals to register as foreign agents under the Act is continuing with respect to activities carried out previously on behalf of such foreign principals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:41Z"
    }
  ]
}
```
