# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1376?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1376
- Title: Healthy Poultry Assistance and Indemnification Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1376
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-05-16T08:07:30Z
- Update date including text: 2026-05-16T08:07:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1376",
    "number": "1376",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Healthy Poultry Assistance and Indemnification Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:30Z",
    "updateDateIncludingText": "2026-05-16T08:07:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-20",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:30:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-20T20:38:56Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "MO"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "NY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "MN"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "GA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "MN"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "PA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "IA"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "AR"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "KS"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "DE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1376ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1376\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Costa (for himself, Mr. Alford , Mr. Riley of New York , Mr. Stauber , Mr. Johnson of Georgia , Mr. Finstad , Ms. Houlahan , Mr. Feenstra , and Mr. Womack ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Animal Health Protection Act to provide compensation for poultry growers and layers in control areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Poultry Assistance and Indemnification Act of 2025 .\n#### 2. Compensation for poultry growers and layers in control areas\nSection 10407 of the Animal Health Protection Act ( 7 U.S.C. 8306 ) is amended\u2014\n**(1)**\nin subsection (d), in the subsection heading, by inserting for destroyed animals after Compensation ; and\n**(2)**\nby adding at the end the following:\n(e) Compensation for poultry growers and layers in control areas (1) Definitions In this subsection: (A) Control area The term control area means a Control Area determined by the Administrator of the Animal and Plant Health Inspection Service. (B) Poultry The term poultry means domesticated fowl that are bred for the primary purpose of producing eggs or meat, including, when so bred, chickens, turkeys, ostriches, emus, rheas, cassowaries, waterfowl, and game birds, but not including doves and pigeons. (2) Compensation (A) In general Except as provided in paragraph (3), the Secretary shall compensate the owner of a poultry growing or laying facility for flocks of birds that the owner of such facility was prohibited from growing or laying due to the location of the facility within a control area. (B) Amount (i) In general Compensation paid under subparagraph (A) shall be in an amount that is equal to the product obtained by multiplying\u2014 (I) the average income from the 5 most recent flocks of birds that the poultry growing or laying facility grew or laid; and (II) the number of flocks of birds that the owner of the poultry growing or laying facility was prohibited from growing or laying during the period of time in which the control area was in effect. (ii) Limitation Compensation paid any owner of a poultry growing or laying facility under this subsection shall not exceed the difference between\u2014 (I) the amount described in clause (i); and (II) any compensation received by the owner from a State or other source for the 1 or more flocks of birds that the owner was prohibited from growing or laying. (iii) Reviewability The determination by the Secretary of the amount to be paid under this subsection shall be final and not subject to judicial review or review by any officer or employee of the Federal Government other than the Secretary or the designee of the Secretary. (C) Timing Compensation shall be paid under subparagraph (A) not later than 60 days after the date on which the owner of a poultry growing or laying facility submits a request to the Secretary for compensation. (3) Exceptions (A) In general The exceptions described in subsection (d)(3) shall apply to this subsection. (B) Compensation for destroyed animals No payment shall be made by the Secretary under this subsection to an owner of a poultry growing or laying facility who has received compensation under subsection (d) for a facility in the same control area during the same period of time. .",
      "versionDate": "2025-02-14",
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
        "actionDate": "2025-02-13",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "574",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Healthy Poultry Assistance and Indemnification Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-20T19:53:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1376",
          "measure-number": "1376",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1376v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Healthy Poultry Assistance and Indemnification Act\u00a0of 2025</strong></p><p>This bill expands the Animal and Plant Health Inspection Service (APHIS) producer indemnity and compensation program to include compensation for all poultry growers and layers located in an APHIS-determined control area, which may include non-infected poultry.\u00a0</p><p>Currently, APHIS provides indemnity and compensation to producers to remove animals classified as affected, suspect, or exposed to diseases of concern, including highly pathogenic avian influenza (HPAI). An APHIS-determined\u00a0<em>control area</em> consists of both an infected zone and a buffer zone. \u00a0Under the bill, APHIS must compensate all owners of poultry growing or laying facilities for flocks of birds that the facility owner was prohibited from growing or laying due to the location of the facility\u00a0within a control area. This may include facilities that are located in the buffer zones and have non-infected poultry.</p><p>Further, the bill establishes a new compensation payment formula that requires payments to be based on the owner\u2019s average income from the five most recent flocks.\u00a0Under the bill,\u00a0APHIS's compensation determination is final and not subject to judicial or administrative review (other than by the Secretary of Agriculture or a designee).</p>"
        },
        "title": "Healthy Poultry Assistance and Indemnification Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1376.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy Poultry Assistance and Indemnification Act\u00a0of 2025</strong></p><p>This bill expands the Animal and Plant Health Inspection Service (APHIS) producer indemnity and compensation program to include compensation for all poultry growers and layers located in an APHIS-determined control area, which may include non-infected poultry.\u00a0</p><p>Currently, APHIS provides indemnity and compensation to producers to remove animals classified as affected, suspect, or exposed to diseases of concern, including highly pathogenic avian influenza (HPAI). An APHIS-determined\u00a0<em>control area</em> consists of both an infected zone and a buffer zone. \u00a0Under the bill, APHIS must compensate all owners of poultry growing or laying facilities for flocks of birds that the facility owner was prohibited from growing or laying due to the location of the facility\u00a0within a control area. This may include facilities that are located in the buffer zones and have non-infected poultry.</p><p>Further, the bill establishes a new compensation payment formula that requires payments to be based on the owner\u2019s average income from the five most recent flocks.\u00a0Under the bill,\u00a0APHIS's compensation determination is final and not subject to judicial or administrative review (other than by the Secretary of Agriculture or a designee).</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1376"
    },
    "title": "Healthy Poultry Assistance and Indemnification Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy Poultry Assistance and Indemnification Act\u00a0of 2025</strong></p><p>This bill expands the Animal and Plant Health Inspection Service (APHIS) producer indemnity and compensation program to include compensation for all poultry growers and layers located in an APHIS-determined control area, which may include non-infected poultry.\u00a0</p><p>Currently, APHIS provides indemnity and compensation to producers to remove animals classified as affected, suspect, or exposed to diseases of concern, including highly pathogenic avian influenza (HPAI). An APHIS-determined\u00a0<em>control area</em> consists of both an infected zone and a buffer zone. \u00a0Under the bill, APHIS must compensate all owners of poultry growing or laying facilities for flocks of birds that the facility owner was prohibited from growing or laying due to the location of the facility\u00a0within a control area. This may include facilities that are located in the buffer zones and have non-infected poultry.</p><p>Further, the bill establishes a new compensation payment formula that requires payments to be based on the owner\u2019s average income from the five most recent flocks.\u00a0Under the bill,\u00a0APHIS's compensation determination is final and not subject to judicial or administrative review (other than by the Secretary of Agriculture or a designee).</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1376"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1376ih.xml"
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
      "title": "Healthy Poultry Assistance and Indemnification Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthy Poultry Assistance and Indemnification Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Animal Health Protection Act to provide compensation for poultry growers and layers in control areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T15:18:27Z"
    }
  ]
}
```
