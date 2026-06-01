# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/745
- Title: Empowering Families in Special Education Act
- Congress: 119
- Bill type: S
- Bill number: 745
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-12-18T12:03:18Z
- Update date including text: 2025-12-18T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/745",
    "number": "745",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Empowering Families in Special Education Act",
    "type": "S",
    "updateDate": "2025-12-18T12:03:18Z",
    "updateDateIncludingText": "2025-12-18T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
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
      "actionCode": "10000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T17:36:29Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NH"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s745is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 745\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Schmitt (for himself, Mrs. Shaheen , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Individuals with Disabilities Education Act to require notification with respect to individualized education program teams, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empowering Families in Special Education Act .\n#### 2. Notification requirement for IEP teams\nSection 614(d)(1)(B) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1414(d)(1)(B) ) is amended\u2014\n**(1)**\nin clause (iv), by redesignating subclauses (I) through (III) as items (aa) through (cc), respectively (and by conforming the margins accordingly);\n**(2)**\nby redesignating clauses (i) through (vii) as subclauses (I) through (VII), respectively (and by conforming the margins accordingly);\n**(3)**\nin the matter preceding subclause (I), as so redesignated, by striking The term and inserting the following:\n(i) In general The term ; and\n**(4)**\nby adding at the end the following:\n(ii) Notification required Within a reasonable timeframe prior to the first convening of the individualized education program team for a child with a disability for a school year, the local educational agency that serves such child shall notify the parent of such child that such parent may, under clause (i)(VI), include other individuals who have knowledge or special expertise regarding the child, including related services personnel as appropriate, as part of the individualized education program team. .",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-02-25",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1570",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Empowering Families in Special Education Act",
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
        "name": "Education",
        "updateDate": "2025-03-23T11:21:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s745",
          "measure-number": "745",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s745v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Empowering Families in Special Education Act</strong></p><p>This bill establishes a notification requirement related to an individualized education program (IEP). (Generally, IEPs are individualized plans to ensure that a child with a disability receives a free appropriate public education.)</p><p>Under current law, states and local educational agencies (LEAs) must convene a team to develop an IEP. The composition of the team that develops the IEP is outlined in current law and allows for other individuals who have knowledge or special expertise regarding the child (including related services personnel, as appropriate) to participate in this team. This bill requires the LEA that serves the child to notify the child's parents of their right to include these other individuals with knowledge or special expertise on the child's IEP team.</p>"
        },
        "title": "Empowering Families in Special Education Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s745.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Empowering Families in Special Education Act</strong></p><p>This bill establishes a notification requirement related to an individualized education program (IEP). (Generally, IEPs are individualized plans to ensure that a child with a disability receives a free appropriate public education.)</p><p>Under current law, states and local educational agencies (LEAs) must convene a team to develop an IEP. The composition of the team that develops the IEP is outlined in current law and allows for other individuals who have knowledge or special expertise regarding the child (including related services personnel, as appropriate) to participate in this team. This bill requires the LEA that serves the child to notify the child's parents of their right to include these other individuals with knowledge or special expertise on the child's IEP team.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s745"
    },
    "title": "Empowering Families in Special Education Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Empowering Families in Special Education Act</strong></p><p>This bill establishes a notification requirement related to an individualized education program (IEP). (Generally, IEPs are individualized plans to ensure that a child with a disability receives a free appropriate public education.)</p><p>Under current law, states and local educational agencies (LEAs) must convene a team to develop an IEP. The composition of the team that develops the IEP is outlined in current law and allows for other individuals who have knowledge or special expertise regarding the child (including related services personnel, as appropriate) to participate in this team. This bill requires the LEA that serves the child to notify the child's parents of their right to include these other individuals with knowledge or special expertise on the child's IEP team.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s745"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s745is.xml"
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
      "title": "Empowering Families in Special Education Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Empowering Families in Special Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Individuals with Disabilities Education Act to require notification with respect to individualized education program teams, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:33Z"
    }
  ]
}
```
