# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6021
- Title: Archie Cavanaugh Migratory Bird Treaty Amendment Act
- Congress: 119
- Bill type: HR
- Bill number: 6021
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2026-04-08T15:04:01Z
- Update date including text: 2026-04-08T15:04:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6021",
    "number": "6021",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "B001323",
        "district": "",
        "firstName": "Nicholas",
        "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
        "lastName": "Begich",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Archie Cavanaugh Migratory Bird Treaty Amendment Act",
    "type": "HR",
    "updateDate": "2026-04-08T15:04:01Z",
    "updateDateIncludingText": "2026-04-08T15:04:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
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
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T15:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-28T18:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6021ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6021\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Begich introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Migratory Bird Treaty Act to clarify the treatment of authentic Alaska Native articles of handicraft containing nonedible migratory bird parts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Archie Cavanaugh Migratory Bird Treaty Amendment Act .\n#### 2. Purpose\nThe purpose of this Act is to clarify the treatment of authentic Alaska Native articles of handicraft (as defined in subsection (c)(1) of section 2 of the Migratory Bird Treaty Act ( 16 U.S.C. 703 )) under\u2014\n**(1)**\nthe Convention between the United States and Great Britain for the Protection of Migratory Birds, signed at Washington August 16, 1916 (39 Stat. 1702; USTS 628);\n**(2)**\nthe Convention between the United States and Mexico for the Protection of Migratory Birds and Game Mammals, signed at Mexico City February 7, 1936 (50 Stat. 1311; USTS 912);\n**(3)**\nthe Convention between the United States and Japan for the Protection of Migratory Birds and Birds in Danger of Extinction and Their Environment, signed at Tokyo March 4, 1974 (TIAS 7990); and\n**(4)**\nthe Convention between the United States and the Soviet Union Concerning the Conservation of Migratory Birds and Their Environment, signed at Moscow November 19, 1976 (TIAS 9073).\n#### 3. Clarification for Alaska Native articles containing migratory bird parts\n##### (a) In general\nSection 2 of the Migratory Bird Treaty Act ( 16 U.S.C. 703 ) is amended by adding at the end the following:\n(c) Clarification for authentic alaska native articles of handicraft (1) Definitions In this subsection: (A) Alaska native The term Alaska Native means a member of any Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) that is based in the State of Alaska, as verified through issuance of\u2014 (i) a Tribal enrollment card; (ii) a Certificate of Degree of Indian Blood (commonly known as a CDIB ) by the Bureau of Indian Affairs; or (iii) a permit under the Silver Hand program of the Alaska State Council on the Arts. (B) Authentic alaska native article of handicraft (i) In general The term authentic Alaska Native article of handicraft means any item that is\u2014 (I) composed, wholly or in a significant respect, of natural materials that were found, foraged, or gifted; and (II) produced, decorated, or fashioned in significant part\u2014 (aa) by an Alaska Native; (bb) in the exercise of traditional Alaska Native handicrafts; and (cc) without the use of any mass copying device. (ii) Inclusions The term authentic Alaska Native article of handicraft includes\u2014 (I) any weaving, carving, stitching, sewing, lacing, beading, drawing, or painting that meets the criteria described in clause (i); and (II) any item, including clothing, described in subclause (I) that combines the techniques described in that subclause. (2) Clarification for certain authentic alaska native articles of handicraft Subject to paragraph (3) and notwithstanding any other provision of this Act, nothing in this Act prohibits the possession, offering for sale, sale, offering to barter, barter, offering to purchase, purchase, delivery for shipment, shipment, causing to be shipped or delivered for transportation, transport, causing to be transported, carrying, causing to be carried, or receiving for shipment, transportation, or carriage of any authentic Alaska Native article of handicraft on the basis that the authentic Alaska Native article of handicraft contains a nonedible migratory bird part. (3) Limitation This subsection does not apply to an authentic Alaska Native article of handicraft containing a part of a migratory bird that was taken in a wasteful or illegal manner. .\n##### (b) Administration\nNot later than 180 days after the date of enactment of this Act\u2014\n**(1)**\nthe Secretary of State shall work with the Secretary of the Interior to enter into appropriate bilateral procedures, as necessary, with countries that are parties to the treaties described in paragraphs (1) through (4) of section 2 to clarify the treatment of authentic Alaska Native articles of handicraft (as defined in subsection (c)(1) of section 2 of the Migratory Bird Treaty Act ( 16 U.S.C. 703 )) containing nonedible migratory bird parts from the species of migratory birds listed in those treaties in accordance with the amendments made by subsection (a); and\n**(2)**\nthe Secretary of the Interior shall modify any regulations implementing the Migratory Bird Treaty Act ( 16 U.S.C. 703 et seq. ), as appropriate, to implement the amendments made by this Act.\n##### (c) Technical amendment\nSection 2(a) of the Migratory Bird Treaty Act ( 16 U.S.C. 703 ) is amended by inserting a comma after March 4, 1972 .",
      "versionDate": "2025-11-12",
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
        "actionDate": "2025-01-24",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "255",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Archie Cavanaugh Migratory Bird Treaty Amendment Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alaska Natives and Hawaiians",
            "updateDate": "2026-02-06T16:53:41Z"
          },
          {
            "name": "Birds",
            "updateDate": "2026-02-06T16:53:41Z"
          },
          {
            "name": "Historical and cultural resources",
            "updateDate": "2026-02-06T16:53:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-11-19T16:54:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-12",
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
          "measure-id": "id119hr6021",
          "measure-number": "6021",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-12",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6021v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-11-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Archie Cavanaugh Migratory Bird Treaty Amendment Act</strong></p><p>This bill states that nothing in the Migratory Bird Treaty Act of 1918 (MBTA) prohibits possessing, selling, bartering, purchasing, shipping, or transporting any authentic Alaska Native handicraft, clothing, or art on the basis that it contains a nonedible migratory bird part, so long as the bird was not taken in a wasteful or illegal manner. (The MBTA implements four international treaties that the United States entered into with Canada, Mexico, Japan, and Russia. The MBTA prohibits the taking of protected migratory bird species without prior authorization.)</p><p>The bill directs the Department of\u00a0State to work with the Department of the Interior to enter into appropriate bilateral procedures with countries that are parties to the treaties under the MBTA\u00a0to clarify the treatment of Alaska Native handicraft containing nonedible migratory bird parts from the species of migratory birds listed in those treaties. Further, Interior must modify any regulations implementing the MBTA to implement this bill.</p>"
        },
        "title": "Archie Cavanaugh Migratory Bird Treaty Amendment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6021.xml",
    "summary": {
      "actionDate": "2025-11-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Archie Cavanaugh Migratory Bird Treaty Amendment Act</strong></p><p>This bill states that nothing in the Migratory Bird Treaty Act of 1918 (MBTA) prohibits possessing, selling, bartering, purchasing, shipping, or transporting any authentic Alaska Native handicraft, clothing, or art on the basis that it contains a nonedible migratory bird part, so long as the bird was not taken in a wasteful or illegal manner. (The MBTA implements four international treaties that the United States entered into with Canada, Mexico, Japan, and Russia. The MBTA prohibits the taking of protected migratory bird species without prior authorization.)</p><p>The bill directs the Department of\u00a0State to work with the Department of the Interior to enter into appropriate bilateral procedures with countries that are parties to the treaties under the MBTA\u00a0to clarify the treatment of Alaska Native handicraft containing nonedible migratory bird parts from the species of migratory birds listed in those treaties. Further, Interior must modify any regulations implementing the MBTA to implement this bill.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6021"
    },
    "title": "Archie Cavanaugh Migratory Bird Treaty Amendment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Archie Cavanaugh Migratory Bird Treaty Amendment Act</strong></p><p>This bill states that nothing in the Migratory Bird Treaty Act of 1918 (MBTA) prohibits possessing, selling, bartering, purchasing, shipping, or transporting any authentic Alaska Native handicraft, clothing, or art on the basis that it contains a nonedible migratory bird part, so long as the bird was not taken in a wasteful or illegal manner. (The MBTA implements four international treaties that the United States entered into with Canada, Mexico, Japan, and Russia. The MBTA prohibits the taking of protected migratory bird species without prior authorization.)</p><p>The bill directs the Department of\u00a0State to work with the Department of the Interior to enter into appropriate bilateral procedures with countries that are parties to the treaties under the MBTA\u00a0to clarify the treatment of Alaska Native handicraft containing nonedible migratory bird parts from the species of migratory birds listed in those treaties. Further, Interior must modify any regulations implementing the MBTA to implement this bill.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6021"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6021ih.xml"
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
      "title": "Archie Cavanaugh Migratory Bird Treaty Amendment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T08:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Archie Cavanaugh Migratory Bird Treaty Amendment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T08:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Migratory Bird Treaty Act to clarify the treatment of authentic Alaska Native articles of handicraft containing nonedible migratory bird parts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T08:33:24Z"
    }
  ]
}
```
