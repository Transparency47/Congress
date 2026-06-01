# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/690?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/690
- Title: To prohibit the use of Federal funds to implement Salmonella framework for raw poultry products.
- Congress: 119
- Bill type: HR
- Bill number: 690
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-01-28T16:51:10Z
- Update date including text: 2026-01-28T16:51:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/690",
    "number": "690",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M000871",
        "district": "1",
        "firstName": "Tracey",
        "fullName": "Rep. Mann, Tracey [R-KS-1]",
        "lastName": "Mann",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "To prohibit the use of Federal funds to implement Salmonella framework for raw poultry products.",
    "type": "HR",
    "updateDate": "2026-01-28T16:51:10Z",
    "updateDateIncludingText": "2026-01-28T16:51:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-28",
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
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:14:01Z",
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
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AR"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr690ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 690\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Mann (for himself and Mr. Womack ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo prohibit the use of Federal funds to implement Salmonella framework for raw poultry products.\n#### 1. Prohibition on use of Federal funds to implement Salmonella framework for raw poultry products\nNo Federal funds may be used to finalize, implement, administer, or enforce the proposed rule and proposed determination entitled Salmonella Framework for Raw Poultry Products published by the Food Safety and Inspection Service of the Department of Agriculture in the Federal Register on August 7, 2024 (89 Fed. Reg. 64678 et seq.).",
      "versionDate": "2025-01-23",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-25T15:19:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr690",
          "measure-number": "690",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2026-01-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr690v00",
            "update-date": "2026-01-28"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits using federal funds to finalize, implement, administer, or enforce the proposed determination and proposed rule on\u00a0<em>Salmonella </em>in raw poultry products. The Food Safety and Inspection Service (FSIS) proposed the rule and the determination in the proposed <em>Salmonella Framework for Raw Poultry Products</em> that was published<em> </em>on August 7, 2024.</p><p>The FSIS's proposed determination\u00a0declares raw chicken carcasses, chicken parts, ground chicken, and ground turkey products that contain certain types and levels of <em>Salmonella</em> as adulterated, thus prohibiting these products from entering commerce.\u00a0</p><p>The FSIS's proposed\u00a0rule\u00a0would revise the current\u00a0regulations on how poultry slaughter establishments monitor and document microbial contamination throughout the slaughter and dressing operation. This includes new requirements for\u00a0microbial monitoring programs, increased sampling and testing, and additional\u00a0recordkeeping.</p>"
        },
        "title": "To prohibit the use of Federal funds to implement Salmonella framework for raw poultry products."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr690.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits using federal funds to finalize, implement, administer, or enforce the proposed determination and proposed rule on\u00a0<em>Salmonella </em>in raw poultry products. The Food Safety and Inspection Service (FSIS) proposed the rule and the determination in the proposed <em>Salmonella Framework for Raw Poultry Products</em> that was published<em> </em>on August 7, 2024.</p><p>The FSIS's proposed determination\u00a0declares raw chicken carcasses, chicken parts, ground chicken, and ground turkey products that contain certain types and levels of <em>Salmonella</em> as adulterated, thus prohibiting these products from entering commerce.\u00a0</p><p>The FSIS's proposed\u00a0rule\u00a0would revise the current\u00a0regulations on how poultry slaughter establishments monitor and document microbial contamination throughout the slaughter and dressing operation. This includes new requirements for\u00a0microbial monitoring programs, increased sampling and testing, and additional\u00a0recordkeeping.</p>",
      "updateDate": "2026-01-28",
      "versionCode": "id119hr690"
    },
    "title": "To prohibit the use of Federal funds to implement Salmonella framework for raw poultry products."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits using federal funds to finalize, implement, administer, or enforce the proposed determination and proposed rule on\u00a0<em>Salmonella </em>in raw poultry products. The Food Safety and Inspection Service (FSIS) proposed the rule and the determination in the proposed <em>Salmonella Framework for Raw Poultry Products</em> that was published<em> </em>on August 7, 2024.</p><p>The FSIS's proposed determination\u00a0declares raw chicken carcasses, chicken parts, ground chicken, and ground turkey products that contain certain types and levels of <em>Salmonella</em> as adulterated, thus prohibiting these products from entering commerce.\u00a0</p><p>The FSIS's proposed\u00a0rule\u00a0would revise the current\u00a0regulations on how poultry slaughter establishments monitor and document microbial contamination throughout the slaughter and dressing operation. This includes new requirements for\u00a0microbial monitoring programs, increased sampling and testing, and additional\u00a0recordkeeping.</p>",
      "updateDate": "2026-01-28",
      "versionCode": "id119hr690"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr690ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds to implement Salmonella framework for raw poultry products.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:22Z"
    },
    {
      "title": "To prohibit the use of Federal funds to implement Salmonella framework for raw poultry products.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:27Z"
    }
  ]
}
```
