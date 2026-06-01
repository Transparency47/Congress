# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/821?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/821
- Title: Taiwan Assurance Implementation Act
- Congress: 119
- Bill type: S
- Bill number: 821
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2026-05-21T13:19:28Z
- Update date including text: 2026-05-21T13:19:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 52.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 52.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/821",
    "number": "821",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Taiwan Assurance Implementation Act",
    "type": "S",
    "updateDate": "2026-05-21T13:19:28Z",
    "updateDateIncludingText": "2026-05-21T13:19:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 52.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-03",
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
        "item": [
          {
            "date": "2025-04-28T20:38:31Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-27T17:57:32Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-03T22:24:16Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "DE"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s821is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 821\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Cornyn (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo provide for increased reporting regarding Department of State Taiwan guidelines.\n#### 1. Short title\nThis Act may be cited as the Taiwan Assurance Implementation Act .\n#### 2. Increased reporting regarding Department of State Taiwan guidelines\nSection 315 of the Taiwan Assurance Act of 2020 (subtitle B of title III of division FF of Public Law 116\u2013260 ; 134 Stat. 3100) is amended\u2014\n**(1)**\nin subsection (c)(1), by inserting and any successor document or related document that includes guidance on relations with Taiwan after memorandum ; and\n**(2)**\nby adding at the end the following new subsection:\n(d) Periodic reviews and updated reports (1) In general For as long as the Department of State maintains guidance that governs relations with Taiwan as described in subsection (a), the Secretary of State shall\u2014 (A) not less than once every five years, conduct a review of the Department of State\u2019s guidance that governs relations with Taiwan, including the periodic memorandum entitled, Guidelines on Relations with Taiwan and related documents, and reissue such guidance to executive branch departments and agencies; and (B) not later than 90 days after completing a review required by paragraph (1)(A), submit an updated report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives . (2) Matters to be included The updated reports required under paragraph (1)(B) shall include\u2014 (A) all the information required under subsection (c); (B) a description of how the updated guidance meets the goals and objectives described in subsection (b); and (C) an identification of self-imposed restrictions on relations with Taiwan lifted by the Secretary of State in the most recent updated guidance, including the periodic memorandum entitled Guidelines on Relations with Taiwan and related documents. .",
      "versionDate": "2025-03-03",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s821rs.xml",
      "text": "II\nCalendar No. 52\n119th CONGRESS\n1st Session\nS. 821\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Cornyn (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nApril 28, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo provide for increased reporting regarding Department of State Taiwan guidelines.\n#### 1. Short title\nThis Act may be cited as the Taiwan Assurance Implementation Act .\n#### 2. Increased reporting regarding Department of State Taiwan guidelines\nSection 315 of the Taiwan Assurance Act of 2020 (subtitle B of title III of division FF of Public Law 116\u2013260 ; 134 Stat. 3100) is amended\u2014\n**(1)**\nin subsection (c)(1), by inserting and any successor document or related document that includes guidance on relations with Taiwan after memorandum ; and\n**(2)**\nby adding at the end the following new subsection:\n(d) Periodic reviews and updated reports (1) In general For as long as the Department of State maintains guidance that governs relations with Taiwan as described in subsection (a), the Secretary of State shall\u2014 (A) not less than once every five years, conduct a review of the Department of State\u2019s guidance that governs relations with Taiwan, including the periodic memorandum entitled, Guidelines on Relations with Taiwan and related documents, and reissue such guidance to executive branch departments and agencies; and (B) not later than 90 days after completing a review required by paragraph (1)(A), submit an updated report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives . (2) Matters to be included The updated reports required under paragraph (1)(B) shall include\u2014 (A) all the information required under subsection (c); (B) a description of how the updated guidance meets the goals and objectives described in subsection (b); and (C) an identification of self-imposed restrictions on relations with Taiwan lifted by the Secretary of State in the most recent updated guidance, including the periodic memorandum entitled Guidelines on Relations with Taiwan and related documents. .",
      "versionDate": "2025-04-28",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-12-02",
        "text": "Became Public Law No: 119-45."
      },
      "number": "1512",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Taiwan Assurance Implementation Act",
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
            "name": "Asia",
            "updateDate": "2025-05-12T19:08:17Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-12T19:08:17Z"
          },
          {
            "name": "Department of State",
            "updateDate": "2025-05-12T19:08:17Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-05-12T19:08:17Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2025-05-12T19:08:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-08T16:39:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119s821",
          "measure-number": "821",
          "measure-type": "s",
          "orig-publish-date": "2025-03-03",
          "originChamber": "SENATE",
          "update-date": "2026-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s821v00",
            "update-date": "2026-05-21"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Taiwan Assurance Implementation Act</strong></p><p>This bill expands an existing requirement for the Department of State to review and report on its guidance to federal agencies on the U.S.-Taiwan relationship. (The U.S.-Taiwan relationship has been unofficial since 1979, when the United States established diplomatic relations with China and broke them with Taiwan.)</p><p>Current law requires the State Department to conduct a one-time review of its guidance governing relations with Taiwan and report to Congress on this review. Under this bill, the State Department must review that guidance, reissue it, and report to Congress every five years while the guidance is in effect.</p><p>The reports to Congress must (1) describe the results of the guidance review and any changes to it resulting from implementation of a law that encourages engagement between Taiwanese and U.S. officials; (2) describe how the guidance takes into account certain considerations, such as the sense of Congress that Taiwan is governed by a representative government peacefully constituted through free and fair elections; and (3) identify self-imposed restrictions on relations with Taiwan that the State Department has lifted in its most recent guidance update.</p>"
        },
        "title": "Taiwan Assurance Implementation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s821.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Taiwan Assurance Implementation Act</strong></p><p>This bill expands an existing requirement for the Department of State to review and report on its guidance to federal agencies on the U.S.-Taiwan relationship. (The U.S.-Taiwan relationship has been unofficial since 1979, when the United States established diplomatic relations with China and broke them with Taiwan.)</p><p>Current law requires the State Department to conduct a one-time review of its guidance governing relations with Taiwan and report to Congress on this review. Under this bill, the State Department must review that guidance, reissue it, and report to Congress every five years while the guidance is in effect.</p><p>The reports to Congress must (1) describe the results of the guidance review and any changes to it resulting from implementation of a law that encourages engagement between Taiwanese and U.S. officials; (2) describe how the guidance takes into account certain considerations, such as the sense of Congress that Taiwan is governed by a representative government peacefully constituted through free and fair elections; and (3) identify self-imposed restrictions on relations with Taiwan that the State Department has lifted in its most recent guidance update.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119s821"
    },
    "title": "Taiwan Assurance Implementation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Taiwan Assurance Implementation Act</strong></p><p>This bill expands an existing requirement for the Department of State to review and report on its guidance to federal agencies on the U.S.-Taiwan relationship. (The U.S.-Taiwan relationship has been unofficial since 1979, when the United States established diplomatic relations with China and broke them with Taiwan.)</p><p>Current law requires the State Department to conduct a one-time review of its guidance governing relations with Taiwan and report to Congress on this review. Under this bill, the State Department must review that guidance, reissue it, and report to Congress every five years while the guidance is in effect.</p><p>The reports to Congress must (1) describe the results of the guidance review and any changes to it resulting from implementation of a law that encourages engagement between Taiwanese and U.S. officials; (2) describe how the guidance takes into account certain considerations, such as the sense of Congress that Taiwan is governed by a representative government peacefully constituted through free and fair elections; and (3) identify self-imposed restrictions on relations with Taiwan that the State Department has lifted in its most recent guidance update.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119s821"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s821is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s821rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Taiwan Assurance Implementation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T11:03:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Taiwan Assurance Implementation Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-01T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Taiwan Assurance Implementation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for increased reporting regarding Department of State Taiwan guidelines.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:39Z"
    }
  ]
}
```
