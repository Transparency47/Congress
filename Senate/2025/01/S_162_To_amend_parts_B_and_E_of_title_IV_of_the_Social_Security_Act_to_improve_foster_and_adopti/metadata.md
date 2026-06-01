# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/162?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/162
- Title: Recruiting Families Using Data Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 162
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2025-08-05T23:31:13Z
- Update date including text: 2025-08-05T23:31:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/162",
    "number": "162",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Families"
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
    "title": "Recruiting Families Using Data Act of 2025",
    "type": "S",
    "updateDate": "2025-08-05T23:31:13Z",
    "updateDateIncludingText": "2025-08-05T23:31:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T20:29:01Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NH"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MS"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s162is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 162\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Grassley (for himself, Ms. Hassan , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend parts B and E of title IV of the Social Security Act to improve foster and adoptive parent recruitment and retention, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Recruiting Families Using Data Act of 2025 .\n#### 2. State plan amendment\n##### (a) In general\nSection 422 of the Social Security Act ( 42 U.S.C. 622 ) is amended\u2014\n**(1)**\nin subsection (b)(7), by inserting through the development and implementation of a family partnership plan which meets the requirements of subsection (d) for identification, recruitment, screening, licensing, support, and retention of foster and adoptive families after are needed ; and\n**(2)**\nby adding at the end the following:\n(d) Family Partnership Plan Requirements For purposes of subsection (b)(7), the requirements for a family partnership plan (in this subsection referred to as the plan ) are the following: (1) The plan is developed in consultation with birth, kinship, foster and adoptive families, community-based service providers, technical assistance providers, and youth with lived experience with foster care and adoption. (2) The plan describes\u2014 (A) how the State plans to identify, notify, engage, and support relatives (and others connected to the child) as potential placement resources for children; (B) how the State plans to develop and implement child-specific recruitment plans for every child in or entering foster care who needs a foster or adoptive family; (C) how the State plans to authentically engage children and youth in recruitment efforts on their behalf; (D) how the State plans to use data to establish goals, assess needs, measure progress, reduce unnecessary placements in congregate care, increase permanency, improve placement stability, increase the rate of kinship placements, improve recruitment and retention of families for teens, sibling groups, and other special populations, and align the composition of foster and adoptive families with the needs of children in or entering foster care; and (E) how that State will stand up or support foster family advisory boards for the purpose of improving recruitment and retention of foster and adoptive families. (3) The plan provides that, not less than annually, the State shall collect and report on the State\u2019s actual foster family capacity and congregate care utilization, including the number, demographics, and characteristics of licensed foster families, including prospective adoptive families, the number of such families that haven\u2019t received a placement or are not being fully utilized and the reasons therefor, and the number, demographics, and characteristics of children placed in congregate care in-State and out-of-State. (4) The plan includes, and shall update not less than annually, a summary of the most recent feedback from foster and adoptive parents and youth regarding licensure, training, support, and reasons why parents stop fostering or why adoptive or legal guardianship placements out of foster care fail or foster and such adoptive of legal guardianship families struggle to meet children\u2019s needs. (5) The plan includes, and shall update annually, a report on the State\u2019s analysis of specific challenges or barriers to recruiting, licensing, and utilizing families who reflect the racial and ethnic background of children in foster care in the State, and the State\u2019s efforts to overcome those challenges and barriers. (6) The plan includes such other information relating to foster and adoptive parent recruitment and retention as the Secretary may require. .\n##### (b) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendment made by this subsection shall take effect on October 1, 2026.\n**(2) Delay permitted if state legislation required**\nIn the case of a State plan approved under subpart 1 of part B of title IV of the Social Security Act which the Secretary of Health and Human Services determines requires State legislation (other than legislation appropriating funds) in order for the plan to meet the additional requirements imposed by this subsection, the State plan shall not be regarded as failing to comply with the requirements of such part solely on the basis of the failure of the plan to meet such additional requirements before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that begins after the date of enactment of this subsection. For purposes of the previous sentence, in the case of a State that has a 2-year legislative session, each year of such session shall be deemed to be a separate regular session of the State legislature.\n#### 3. Inclusion of information on foster and adoptive families in annual child welfare outcomes report to Congress\nSection 479A(a) of the Social Security Act ( 42 U.S.C. 679b(a) ) is amended\u2014\n**(1)**\nin paragraph (6)(C), by striking and after the semicolon;\n**(2)**\nin paragraph (7)(B), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) include in the report submitted pursuant to paragraph (5) for fiscal year 2025 or any succeeding fiscal year\u2014 (A) State-by-State data on the number, demographics, and characteristics of foster and adoptive families in the State, and the number of potential foster and adoptive families not being utilized in the State and the reasons why; (B) a summary of the challenges of, and barriers to, being a foster or adoptive parent, including with respect to recruitment, licensure, engagement, retention, and why parents stop fostering, adoptions disrupt or dissolve, or foster or adoptive families struggle, as reported by States based on surveys of foster and adoptive parents; and (C) a summary of the challenges and barriers States reported on efforts to recruit a pool of families that reflect the racial and ethnic background of children in foster care in the State, and efforts to overcome those barriers. .",
      "versionDate": "2025-01-21",
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
        "actionDate": "2025-03-05",
        "text": "Received in the Senate and Read twice and referred to the Committee on Finance."
      },
      "number": "579",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recruiting Families Using Data Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Adoption and foster care",
            "updateDate": "2025-03-03T17:37:21Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2025-03-03T17:37:21Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-03T17:37:21Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-03-03T17:37:21Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-03-03T17:37:21Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-03T17:37:21Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-03T17:37:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Families",
        "updateDate": "2025-02-24T18:07:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s162",
          "measure-number": "162",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s162v00",
            "update-date": "2025-05-01"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Recruiting Families Using Data Act of 2025</strong></p><p>This bill requires state plans for child welfare services to provide for the development and implementation of a family partnership plan to improve foster care placement stability, increase rates of kinship placements, and align the composition of foster and adoptive families with the needs of children in or entering foster care.</p><p>The Children's Bureau of the Administration for Children and\u00a0Families also must include in its annual report information from states about the number, demographics, and characteristics of foster and adoptive families as well as a summary of the challenges related to recruiting and being foster or adoptive parents.</p>"
        },
        "title": "Recruiting Families Using Data Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s162.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Recruiting Families Using Data Act of 2025</strong></p><p>This bill requires state plans for child welfare services to provide for the development and implementation of a family partnership plan to improve foster care placement stability, increase rates of kinship placements, and align the composition of foster and adoptive families with the needs of children in or entering foster care.</p><p>The Children's Bureau of the Administration for Children and\u00a0Families also must include in its annual report information from states about the number, demographics, and characteristics of foster and adoptive families as well as a summary of the challenges related to recruiting and being foster or adoptive parents.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119s162"
    },
    "title": "Recruiting Families Using Data Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Recruiting Families Using Data Act of 2025</strong></p><p>This bill requires state plans for child welfare services to provide for the development and implementation of a family partnership plan to improve foster care placement stability, increase rates of kinship placements, and align the composition of foster and adoptive families with the needs of children in or entering foster care.</p><p>The Children's Bureau of the Administration for Children and\u00a0Families also must include in its annual report information from states about the number, demographics, and characteristics of foster and adoptive families as well as a summary of the challenges related to recruiting and being foster or adoptive parents.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119s162"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s162is.xml"
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
      "title": "Recruiting Families Using Data Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Recruiting Families Using Data Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend parts B and E of title IV of the Social Security Act to improve foster and adoptive parent recruitment and retention, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:20Z"
    }
  ]
}
```
