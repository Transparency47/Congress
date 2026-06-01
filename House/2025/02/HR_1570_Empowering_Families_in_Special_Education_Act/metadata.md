# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1570?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1570
- Title: Empowering Families in Special Education Act
- Congress: 119
- Bill type: HR
- Bill number: 1570
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:01:12Z
- Update date including text: 2025-12-05T22:01:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1570",
    "number": "1570",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Empowering Families in Special Education Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:01:12Z",
    "updateDateIncludingText": "2025-12-05T22:01:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-25T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1570ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1570\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mrs. Houchin (for herself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Individuals with Disabilities Education Act to require notification with respect to individualized education program teams, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empowering Families in Special Education Act .\n#### 2. Notification requirement for IEP teams\nSection 614(d)(1)(B) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1414(d)(1)(B) ) is amended\u2014\n**(1)**\nin clause (iv), by redesignating subclauses (I) through (III) as items (aa) through (cc), respectively (and by conforming the margins accordingly);\n**(2)**\nby redesignating clauses (i) through (vii) as subclauses (I) through (VII), respectively (and by conforming the margins accordingly);\n**(3)**\nin the matter preceding subclause (I), as so redesignated, by striking The term and inserting the following:\n(i) In general The term ; and\n**(4)**\nby adding at the end the following:\n(ii) Notification required Within a reasonable timeframe prior to the first convening of the individualized education program team for a child with a disability for a school year, the local educational agency that serves such child shall notify the parent of such child that such parent may, under clause (i)(VI), include other individuals who have knowledge or special expertise regarding the child, including related services personnel as appropriate, as part of the individualized education program team. .",
      "versionDate": "2025-02-25",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-26",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "745",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Empowering Families in Special Education Act",
      "type": "S"
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
        "updateDate": "2025-03-21T16:24:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "House",
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
          "measure-id": "id119hr1570",
          "measure-number": "1570",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2025-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1570v00",
            "update-date": "2025-04-21"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Empowering Families in Special Education Act</strong></p><p>This bill establishes a notification requirement related to an individualized education program (IEP). (Generally, IEPs are individualized plans to ensure that a child with a disability receives a free appropriate public education.)</p><p>Under current law, states and local educational agencies (LEAs) must convene a team to develop an IEP. The composition of the team that develops the IEP is outlined in current law and allows for other individuals who have knowledge or special expertise regarding the child (including related services personnel, as appropriate) to participate in this team. This bill requires the LEA that serves the child to notify the child's parents of their right to include these other individuals with knowledge or special expertise on the child's IEP team.</p>"
        },
        "title": "Empowering Families in Special Education Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1570.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Empowering Families in Special Education Act</strong></p><p>This bill establishes a notification requirement related to an individualized education program (IEP). (Generally, IEPs are individualized plans to ensure that a child with a disability receives a free appropriate public education.)</p><p>Under current law, states and local educational agencies (LEAs) must convene a team to develop an IEP. The composition of the team that develops the IEP is outlined in current law and allows for other individuals who have knowledge or special expertise regarding the child (including related services personnel, as appropriate) to participate in this team. This bill requires the LEA that serves the child to notify the child's parents of their right to include these other individuals with knowledge or special expertise on the child's IEP team.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119hr1570"
    },
    "title": "Empowering Families in Special Education Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Empowering Families in Special Education Act</strong></p><p>This bill establishes a notification requirement related to an individualized education program (IEP). (Generally, IEPs are individualized plans to ensure that a child with a disability receives a free appropriate public education.)</p><p>Under current law, states and local educational agencies (LEAs) must convene a team to develop an IEP. The composition of the team that develops the IEP is outlined in current law and allows for other individuals who have knowledge or special expertise regarding the child (including related services personnel, as appropriate) to participate in this team. This bill requires the LEA that serves the child to notify the child's parents of their right to include these other individuals with knowledge or special expertise on the child's IEP team.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119hr1570"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1570ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empowering Families in Special Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Individuals with Disabilities Education Act to require notification with respect to individualized education program teams, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:00Z"
    }
  ]
}
```
