# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1380
- Title: Meat and Poultry Special Investigator Act
- Congress: 119
- Bill type: HR
- Bill number: 1380
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-02-27T21:41:19Z
- Update date including text: 2026-02-27T21:41:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1380",
    "number": "1380",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Meat and Poultry Special Investigator Act",
    "type": "HR",
    "updateDate": "2026-02-27T21:41:19Z",
    "updateDateIncludingText": "2026-02-27T21:41:19Z"
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
          "date": "2025-02-14T18:33:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-20T20:39:12Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1380ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1380\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Packers and Stockyards Act, 1921, to establish the Office of the Special Investigator for Competition Matters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Meat and Poultry Special Investigator Act .\n#### 2. Office of the Special Investigator for Competition Matters\nThe Packers and Stockyards Act, 1921, is amended by inserting after section 415 ( 7 U.S.C. 228d ) the following:\n416. Office of the Special Investigator for Competition Matters (a) Establishment There is established within the Packers and Stockyards Division of the Department of Agriculture an office, to be known as the Office of the Special Investigator for Competition Matters (referred to in this section as the Office ). (b) Special investigator for competition matters The Office shall be headed by the Special Investigator for Competition Matters (referred to in this section as the Special Investigator ), who shall be appointed by the Secretary. (c) Duties The Special Investigator shall\u2014 (1) use all available tools, including subpoenas, to investigate and prosecute violations of this Act; (2) serve as a Department of Agriculture liaison to, and act in consultation with, the Department of Justice and the Federal Trade Commission with respect to competition and trade practices in the food and agricultural sector; (3) act in consultation with the Department of Homeland Security with respect to national security and critical infrastructure security in the food and agricultural sector; and (4) maintain a staff of attorneys and other professionals with appropriate expertise. (d) Prosecutorial authority Notwithstanding title 28, United States Code, the Special Investigator shall have the authority to bring any civil or administrative action authorized under this Act. .",
      "versionDate": "2025-02-14",
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
        "updateDate": "2025-03-20T19:52:36Z"
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
          "measure-id": "id119hr1380",
          "measure-number": "1380",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1380v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Meat and Poultry Special Investigator Act</strong></p><p>This bill establishes\u00a0the Office of the Special Investigator for Competition Matters within the Agricultural Marketing Service's Packers and Stockyards Division. </p><p>Specifically, the office must use all available tools (e.g., subpoenas) to investigate and prosecute violations of the Packers and Stockyards Act of 1921 (P&S Act). Further, the bill grants the office the authority to bring any civil or administrative action authorized by that act.</p><p>Additionally, the office must</p><ul><li>serve as a liaison to the Department of Justice and the Federal Trade Commission with respect to competition and trade practices in the food and agricultural sector,</li><li>consult with the Department of Homeland Security on national security and critical infrastructure security in the food and agricultural sector, and</li><li>maintain a staff of attorneys and other professionals with appropriate expertise.</li></ul><p>As background,\u00a0the purposes of the P&S\u00a0Act are to\u00a0assure fair competition and trade practices, safeguard farmers and ranchers, protect consumers, and protect livestock, meat, and poultry industry members from unfair, deceptive, unjustly discriminatory, and monopolistic practices.\u00a0Those engaged in the business of marketing livestock, meat, and poultry in commerce are subject to the P&S\u00a0Act.</p>"
        },
        "title": "Meat and Poultry Special Investigator Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1380.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Meat and Poultry Special Investigator Act</strong></p><p>This bill establishes\u00a0the Office of the Special Investigator for Competition Matters within the Agricultural Marketing Service's Packers and Stockyards Division. </p><p>Specifically, the office must use all available tools (e.g., subpoenas) to investigate and prosecute violations of the Packers and Stockyards Act of 1921 (P&S Act). Further, the bill grants the office the authority to bring any civil or administrative action authorized by that act.</p><p>Additionally, the office must</p><ul><li>serve as a liaison to the Department of Justice and the Federal Trade Commission with respect to competition and trade practices in the food and agricultural sector,</li><li>consult with the Department of Homeland Security on national security and critical infrastructure security in the food and agricultural sector, and</li><li>maintain a staff of attorneys and other professionals with appropriate expertise.</li></ul><p>As background,\u00a0the purposes of the P&S\u00a0Act are to\u00a0assure fair competition and trade practices, safeguard farmers and ranchers, protect consumers, and protect livestock, meat, and poultry industry members from unfair, deceptive, unjustly discriminatory, and monopolistic practices.\u00a0Those engaged in the business of marketing livestock, meat, and poultry in commerce are subject to the P&S\u00a0Act.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1380"
    },
    "title": "Meat and Poultry Special Investigator Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Meat and Poultry Special Investigator Act</strong></p><p>This bill establishes\u00a0the Office of the Special Investigator for Competition Matters within the Agricultural Marketing Service's Packers and Stockyards Division. </p><p>Specifically, the office must use all available tools (e.g., subpoenas) to investigate and prosecute violations of the Packers and Stockyards Act of 1921 (P&S Act). Further, the bill grants the office the authority to bring any civil or administrative action authorized by that act.</p><p>Additionally, the office must</p><ul><li>serve as a liaison to the Department of Justice and the Federal Trade Commission with respect to competition and trade practices in the food and agricultural sector,</li><li>consult with the Department of Homeland Security on national security and critical infrastructure security in the food and agricultural sector, and</li><li>maintain a staff of attorneys and other professionals with appropriate expertise.</li></ul><p>As background,\u00a0the purposes of the P&S\u00a0Act are to\u00a0assure fair competition and trade practices, safeguard farmers and ranchers, protect consumers, and protect livestock, meat, and poultry industry members from unfair, deceptive, unjustly discriminatory, and monopolistic practices.\u00a0Those engaged in the business of marketing livestock, meat, and poultry in commerce are subject to the P&S\u00a0Act.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1380"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1380ih.xml"
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
      "title": "Meat and Poultry Special Investigator Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Meat and Poultry Special Investigator Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Packers and Stockyards Act, 1921, to establish the Office of the Special Investigator for Competition Matters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:57Z"
    }
  ]
}
```
