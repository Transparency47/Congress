# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6279?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6279
- Title: Urban Canal Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 6279
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-04-10T12:12:27Z
- Update date including text: 2026-04-10T12:12:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6279",
    "number": "6279",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001148",
        "district": "2",
        "firstName": "Michael",
        "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
        "lastName": "Simpson",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Urban Canal Modernization Act",
    "type": "HR",
    "updateDate": "2026-04-10T12:12:27Z",
    "updateDateIncludingText": "2026-04-10T12:12:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "ID"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "WA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6279ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6279\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Simpson (for himself, Mr. Fulcher , Mr. Newhouse , and Mr. Gray ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Omnibus Public Land Management Act of 2009 to authorize certain extraordinary operation and maintenance work for urban canals of concern.\n#### 1. Short title\nThis Act may be cited as the Urban Canal Modernization Act .\n#### 2. Extraordinary operation and maintenance work performed by the Secretary of the Interior\n##### (a) Definitions\nSection 9601 of the Omnibus Public Land Management Act of 2009 ( 43 U.S.C. 510 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), (3), (4), (5), (6), and (7) as paragraphs (2), (3), (4), (5), (6), (7), and (1), respectively;\n**(2)**\nby arranging the redesignated paragraphs in numerical order;\n**(3)**\nin paragraph (3) (as so redesignated), by striking et seq.) and inserting et seq.)) ;\n**(4)**\nin paragraph (4) (as so redesignated), by striking mean and inserting means ; and\n**(5)**\nby adding at the end the following:\n(8) Urban canal of concern The term urban canal of concern means a transferred works or segment of a transferred works\u2014 (A) that is\u2014 (i) a canal reach, the failure of which would result in\u2014 (I) an estimated at-risk population of more than 100 individuals; or (II) an estimated property damage of more than $5,000,000; or (ii) a canal reach determined by the responsible Bureau of Reclamation regional or area office to be classified as an urban canal reach; and (B) with respect to which the Secretary determines, pursuant to the guidelines and criteria developed under section 9602(a), that if a failure were to occur, the failure would result in loss of life and property in the vicinity of the failed transferred works or segment of transferred works. .\n##### (b) Extraordinary maintenance and operation work on urban canal of concerns\nSection 9603 of the Omnibus Public Land Management Act of 2009 ( 43 U.S.C. 510b ) is amended by adding at the end the following:\n(e) Extraordinary operation and maintenance work on urban canals of concern (1) In general The Secretary or the transferred works operating entity shall carry out any extraordinary operation and maintenance work on an urban canal of concern that the transferred works operating entity, with the concurrence of the Secretary, determines to be necessary. (2) Funding In the case of extraordinary operation and maintenance work on an urban canal of concern authorized under paragraph (1), or if the Secretary determines that a project facility inspected and maintained pursuant to the guidelines and criteria set forth in section 9602(a) requires extraordinary operation and maintenance work pursuant to paragraph (1), the Secretary shall provide Federal funds on a nonreimbursable basis sufficient to cover 35 percent of the portion of total cost of the extraordinary operation and maintenance work allocable to the transferred works operating entity that is needed to carry out the extraordinary operation and maintenance work on the urban canal of concern, with the remaining share of any additional Federal funds advanced by the Secretary for the extraordinary operation and maintenance work to be repaid under subsection (b). (f) Reimbursable funds Any reimbursable funds provided under this section shall be considered to be a non-Federal source of funds for purposes of any cost-sharing requirement for a Federal grant. .",
      "versionDate": "2025-11-21",
      "versionType": "Introduced in House"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-02T19:25:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-21",
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
          "measure-id": "id119hr6279",
          "measure-number": "6279",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-21",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6279v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-11-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Urban Canal Modernization Act</strong></p><p>This bill expands the Bureau of Reclamation's responsibility under the Omnibus Public Land Management Act of 2009 to address aging irrigation and water resources infrastructure in western states to include additional work for urban canals of concern.</p><p>Specifically, the bill directs Reclamation or the operating entity of a transferred work (i.e., infrastructure owned by Reclamation, but maintained by a nonfederal entity) to carry out any necessary extraordinary operation and maintenance work for urban canals of concern, which are certain transferred works the failure of which would result in loss of life\u00a0and\u00a0property in the vicinity of the canal.</p><p>Reclamation must also provide federal funds to transferred works on a nonreimbursable basis sufficient to cover 35% of the cost of extraordinary operation and maintenance work for (1) urban canals of concern, and (2) certain project facilities which are in proximity to urbanized areas and which could pose a risk to public safety or\u00a0property if the facilities failed.</p><p>The bill further specifies that any reimbursable funds provided under the bill must be considered a nonfederal source of funds for purposes of federal grant cost-sharing requirements.\u00a0</p>"
        },
        "title": "Urban Canal Modernization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6279.xml",
    "summary": {
      "actionDate": "2025-11-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Urban Canal Modernization Act</strong></p><p>This bill expands the Bureau of Reclamation's responsibility under the Omnibus Public Land Management Act of 2009 to address aging irrigation and water resources infrastructure in western states to include additional work for urban canals of concern.</p><p>Specifically, the bill directs Reclamation or the operating entity of a transferred work (i.e., infrastructure owned by Reclamation, but maintained by a nonfederal entity) to carry out any necessary extraordinary operation and maintenance work for urban canals of concern, which are certain transferred works the failure of which would result in loss of life\u00a0and\u00a0property in the vicinity of the canal.</p><p>Reclamation must also provide federal funds to transferred works on a nonreimbursable basis sufficient to cover 35% of the cost of extraordinary operation and maintenance work for (1) urban canals of concern, and (2) certain project facilities which are in proximity to urbanized areas and which could pose a risk to public safety or\u00a0property if the facilities failed.</p><p>The bill further specifies that any reimbursable funds provided under the bill must be considered a nonfederal source of funds for purposes of federal grant cost-sharing requirements.\u00a0</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6279"
    },
    "title": "Urban Canal Modernization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Urban Canal Modernization Act</strong></p><p>This bill expands the Bureau of Reclamation's responsibility under the Omnibus Public Land Management Act of 2009 to address aging irrigation and water resources infrastructure in western states to include additional work for urban canals of concern.</p><p>Specifically, the bill directs Reclamation or the operating entity of a transferred work (i.e., infrastructure owned by Reclamation, but maintained by a nonfederal entity) to carry out any necessary extraordinary operation and maintenance work for urban canals of concern, which are certain transferred works the failure of which would result in loss of life\u00a0and\u00a0property in the vicinity of the canal.</p><p>Reclamation must also provide federal funds to transferred works on a nonreimbursable basis sufficient to cover 35% of the cost of extraordinary operation and maintenance work for (1) urban canals of concern, and (2) certain project facilities which are in proximity to urbanized areas and which could pose a risk to public safety or\u00a0property if the facilities failed.</p><p>The bill further specifies that any reimbursable funds provided under the bill must be considered a nonfederal source of funds for purposes of federal grant cost-sharing requirements.\u00a0</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6279"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6279ih.xml"
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
      "title": "Urban Canal Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-22T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Urban Canal Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-22T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Public Land Management Act of 2009 to authorize certain extraordinary operation and maintenance work for urban canals of concern.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T09:18:23Z"
    }
  ]
}
```
