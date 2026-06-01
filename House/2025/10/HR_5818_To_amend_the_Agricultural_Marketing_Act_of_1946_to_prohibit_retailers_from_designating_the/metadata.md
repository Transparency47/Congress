# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5818?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5818
- Title: Country of Origin Labeling Enforcement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5818
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-03-27T08:06:40Z
- Update date including text: 2026-03-27T08:06:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5818",
    "number": "5818",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Country of Origin Labeling Enforcement Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:40Z",
    "updateDateIncludingText": "2026-03-27T08:06:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
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
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "OH"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "KY"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "AZ"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "WI"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MT"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5818ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5818\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Ms. Hageman (for herself, Mr. Khanna , Mr. Davidson , Mr. Massie , Mr. Roy , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to prohibit retailers from designating the United States as the country of origin of foreign beef, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Country of Origin Labeling Enforcement Act of 2025 .\n#### 2. Country of origin labeling for beef\n##### (a) Definitions\nSection 281 of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1638 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) through (7) as paragraphs (2) through (8), respectively;\n**(2)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) Beef The term beef means meat produced from cattle (including veal). ;\n**(3)**\nin paragraph (2)(A)(i) (as so redesignated), by striking lamb and venison and inserting beef, lamb, and venison ; and\n**(4)**\nin paragraph (2)(A)(ii) (as so redesignated), by striking ground lamb and ground venison and inserting ground beef, ground lamb, and ground venison .\n##### (b) Notice of country of origin\nSection 282(a)(2) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1638a(a)(2) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting beef, after for ;\n**(2)**\nin each of subparagraphs (A) through (D), by inserting beef, before lamb each place it appears; and\n**(3)**\nin subparagraph (E)\u2014\n**(A)**\nin the subparagraph heading, by inserting beef, after Ground ; and\n**(B)**\nby inserting ground beef, before ground lamb each place it appears.\n##### (c) Enforcement\nSection 283(b) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1638b(b) ) is amended by striking $1,000 for each violation and inserting $1,000 for each violation (or in the case of a covered commodity that is beef, $5,000 for each pound of beef not in compliance with the requirements of section 282) .\n##### (d) Rule of construction\nNo ruling by the World Trade Organization or by any other international organization of which the United States is a member that is established before, on, or after the date of enactment of this Act may be construed to limit, alter, or affect the authority of the Secretary of Agriculture to require country of origin labeling in accordance with the amendments made by this section.",
      "versionDate": "2025-10-24",
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
        "updateDate": "2025-12-09T21:14:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-24",
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
          "measure-id": "id119hr5818",
          "measure-number": "5818",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-24",
          "originChamber": "HOUSE",
          "update-date": "2026-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5818v00",
            "update-date": "2026-02-18"
          },
          "action-date": "2025-10-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Country of Origin Labeling Enforcement Act of 2025</strong></p><p>This bill requires retailers to notify their customers of the country of origin of beef. </p><p>In general, under the Department of Agriculture's (USDA's) mandatory Country of Origin Labeling (COOL) requirements, retailers (such as grocery stores, supermarkets, and club warehouses) must provide certain information to consumers regarding the origin of specific foods (e.g., lamb, chicken, fish, and perishable agriculture products). This bill expands these requirements to include mandatory COOL for beef (including ground beef).</p><p>In order to designate beef as exclusively having a country of origin of the United States, the product must generally be derived from an animal that was exclusively born, raised, and slaughtered in the United States. </p><p>A retailer (or a supplier for the retailer) who willfully violates the COOL requirements for beef may be subject to a USDA fine of $5,000 for each pound of beef that is not in compliance. Under current law, the USDA fine may not exceed $1,000 for each COOL violation.</p><p>The bill specifies that no ruling by the World Trade Organization (or by any other international organization of which the United States is a member) may be construed to limit, alter, or affect USDA's authority to implement COOL under this bill.</p>"
        },
        "title": "Country of Origin Labeling Enforcement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5818.xml",
    "summary": {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Country of Origin Labeling Enforcement Act of 2025</strong></p><p>This bill requires retailers to notify their customers of the country of origin of beef. </p><p>In general, under the Department of Agriculture's (USDA's) mandatory Country of Origin Labeling (COOL) requirements, retailers (such as grocery stores, supermarkets, and club warehouses) must provide certain information to consumers regarding the origin of specific foods (e.g., lamb, chicken, fish, and perishable agriculture products). This bill expands these requirements to include mandatory COOL for beef (including ground beef).</p><p>In order to designate beef as exclusively having a country of origin of the United States, the product must generally be derived from an animal that was exclusively born, raised, and slaughtered in the United States. </p><p>A retailer (or a supplier for the retailer) who willfully violates the COOL requirements for beef may be subject to a USDA fine of $5,000 for each pound of beef that is not in compliance. Under current law, the USDA fine may not exceed $1,000 for each COOL violation.</p><p>The bill specifies that no ruling by the World Trade Organization (or by any other international organization of which the United States is a member) may be construed to limit, alter, or affect USDA's authority to implement COOL under this bill.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119hr5818"
    },
    "title": "Country of Origin Labeling Enforcement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Country of Origin Labeling Enforcement Act of 2025</strong></p><p>This bill requires retailers to notify their customers of the country of origin of beef. </p><p>In general, under the Department of Agriculture's (USDA's) mandatory Country of Origin Labeling (COOL) requirements, retailers (such as grocery stores, supermarkets, and club warehouses) must provide certain information to consumers regarding the origin of specific foods (e.g., lamb, chicken, fish, and perishable agriculture products). This bill expands these requirements to include mandatory COOL for beef (including ground beef).</p><p>In order to designate beef as exclusively having a country of origin of the United States, the product must generally be derived from an animal that was exclusively born, raised, and slaughtered in the United States. </p><p>A retailer (or a supplier for the retailer) who willfully violates the COOL requirements for beef may be subject to a USDA fine of $5,000 for each pound of beef that is not in compliance. Under current law, the USDA fine may not exceed $1,000 for each COOL violation.</p><p>The bill specifies that no ruling by the World Trade Organization (or by any other international organization of which the United States is a member) may be construed to limit, alter, or affect USDA's authority to implement COOL under this bill.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119hr5818"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5818ih.xml"
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
      "title": "Country of Origin Labeling Enforcement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Country of Origin Labeling Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Marketing Act of 1946 to prohibit retailers from designating the United States as the country of origin of foreign beef, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T04:18:16Z"
    }
  ]
}
```
