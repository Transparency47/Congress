# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3759?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3759
- Title: SAF Act
- Congress: 119
- Bill type: S
- Bill number: 3759
- Origin chamber: Senate
- Introduced date: 2026-02-02
- Update date: 2026-02-10T21:42:19Z
- Update date including text: 2026-02-10T21:42:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in Senate
- 2026-02-02 - IntroReferral: Introduced in Senate
- 2026-02-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-02: Introduced in Senate

## Actions

- 2026-02-02 - IntroReferral: Introduced in Senate
- 2026-02-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3759",
    "number": "3759",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "SAF Act",
    "type": "S",
    "updateDate": "2026-02-10T21:42:19Z",
    "updateDateIncludingText": "2026-02-10T21:42:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T23:26:45Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NV"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "IA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3759is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3759\nIN THE SENATE OF THE UNITED STATES\nFebruary 2, 2026 Mr. Moran (for himself, Ms. Cortez Masto , Ms. Ernst , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to reinstate the special rate calculation of the clean fuel production credit with respect to sustainable aviation fuel, and to extend the credit through 2033.\n#### 1. Short title\nThis Act may be cited as the Securing America's Fuels Act or the SAF Act .\n#### 2. Extension of clean fuel production credit; reinstatement of special rate calculation for sustainable aviation fuel\n##### (a) Reinstatement of special rate\n**(1) In general**\nParagraph (3) of section 45Z(a) of the Internal Revenue Code of 1986, as amended by section 70521(g)(2) of Public Law 119\u201321 , is amended to read as follows:\n(3) Special rate for sustainable aviation fuel (A) In general In the case of a transportation fuel which is sustainable aviation fuel, paragraph (2) shall be applied\u2014 (i) in the case of fuel produced at a qualified facility described in paragraph (2)(A), by substituting 35 cents for 20 cents , and (ii) in the case of fuel produced at a qualified facility described in paragraph (2)(B), by substituting $1.75 for $1.00 . (B) Sustainable aviation fuel For purposes of this section, the term sustainable aviation fuel means liquid fuel, the portion of which is not kerosene, which is sold for use in an aircraft and which\u2014 (i) meets the requirements of\u2014 (I) ASTM International Standard D7566, or (II) the Fischer Tropsch provisions of ASTM International Standard D1655, Annex A1, and (ii) is not derived from palm fatty acid distillates or petroleum. .\n**(2) Conforming amendment**\nSection 45Z(c)(1) of such Code, as amended by section 70521(g)(2) of Public Law 119\u201321 , is amended by striking and the $1.00 amount in subsection (a)(2)(B) and inserting , the $1.00 amount in subsection (a)(2)(B), the 35 cent amount in subsection (a)(3)(A)(i), and the $1.75 amount in subsection (a)(3)(A)(ii) .\n##### (b) Extension of credit\nSection 45Z(g) of such Code, as amended by section 70521(d) of Public Law 119\u201321 , is amended by striking December 31, 2029 and inserting December 31, 2033 .\n##### (c) Effective date\nThe amendments made by this section shall apply to fuel produced after December 31, 2025.",
      "versionDate": "2026-02-02",
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
        "actionDate": "2025-12-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6518",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAF Act",
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
        "name": "Taxation",
        "updateDate": "2026-02-10T21:42:19Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3759is.xml"
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
      "title": "SAF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing America's Fuels Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to reinstate the special rate calculation of the clean fuel production credit with respect to sustainable aviation fuel, and to extend the credit through 2033.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:28Z"
    }
  ]
}
```
