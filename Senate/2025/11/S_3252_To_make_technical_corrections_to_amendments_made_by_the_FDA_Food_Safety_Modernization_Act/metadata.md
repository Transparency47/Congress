# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3252
- Title: FSMA Fee Technical Corrections Act
- Congress: 119
- Bill type: S
- Bill number: 3252
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-05T15:02:35Z
- Update date including text: 2026-01-05T15:02:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8277-8278)
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8277-8278)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3252",
    "number": "3252",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "FSMA Fee Technical Corrections Act",
    "type": "S",
    "updateDate": "2026-01-05T15:02:35Z",
    "updateDateIncludingText": "2026-01-05T15:02:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8277-8278)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T19:06:52Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3252is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3252\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Durbin (for himself, Mr. Blumenthal , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo make technical corrections to amendments made by the FDA Food Safety Modernization Act to allow the Food and Drug Administration to assess and collect food-related reinspection fees and recall fees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FSMA Fee Technical Corrections Act .\n#### 2. Food-related fees\n##### (a) In general\nParagraph (2) of section 743(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201331(b) ) is amended to read as follows:\n(2) Fee methodology; fee amounts (A) In general Subject to adjustments made by the Secretary in accordance with subparagraph (B), fees established for a fiscal year\u2014 (i) under subsection (a)(1)(A) shall be in the amount equal to $15,000, multiplied, for fiscal year 2026 and each subsequent fiscal year, by the adjustment factor described in subsection (c)(3); (ii) under subsection (a)(1)(B) shall be in the amount equal to $15,000, multiplied, for fiscal year 2026 and each subsequent fiscal year, by the adjustment factor described in subsection (c)(3); (iii) under subsection (a)(1)(C) shall be based on the Secretary's estimate of 100 percent of the costs of the activities described in such subsection for such fiscal year; and (iv) under subsection (a)(1)(D) shall be in the amount equal to $15,000, multiplied, for fiscal year 2026 and each subsequent fiscal year, by the adjustment factor described in subsection (c)(3). (B) Other considerations (i) Fee adjustment for small businesses (I) In general In the case of a facility or importer that, at the time of the reinspection or recall order, is a small business as defined in subsection (a)(2)(E), the amount of the fee under subparagraph (A), (B), or (D) of subsection (a)(1), for a fiscal year, shall be adjusted to be equal to 1/3 of the amount of the fee calculated under clause (i), (ii), or (iv) of subparagraph (A), as applicable, for such fiscal year. (II) Publication of schedule The schedule of such adjusted fee amounts shall be published annually with the user fee notice under subsection (e). (III) Guidance Not later than 270 days after the date of enactment of the FSMA Fee Technical Corrections Act , the Secretary shall publish guidance to describe how a food facility or importer may request a fee reduction under this clause, which shall be issued for immediate implementation to facilitate timely fee reductions, as applicable. (ii) Voluntary qualified importer program In establishing the fee amounts under subparagraph (A)(iii) for a fiscal year, the Secretary shall provide for the number of importers who have submitted to the Secretary a notice under section 806(c) informing the Secretary of the intent of such importer to participate in the program under section 806 in such fiscal year. (iii) Crediting of carryover fees In establishing the fee amounts under subparagraph (A) for a fiscal year, the Secretary shall provide for the crediting toward fee revenue of estimated carryover fee collections from the previous fiscal year if the Secretary overestimated the amount of fees needed to carry out activities described in paragraph (3) for such previous year, and shall account for any adjustment of fees under clause (i). .\n##### (b) Use of fees\nParagraph (3) of section 743(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201331(b) ) is amended to read as follows:\n(3) Use of fees (A) Oversight of facilities and importers Fees collected pursuant to subparagraphs (A), (B), and (D) of subsection (a)(1) shall be available solely for the costs of oversight of foreign and domestic facilities and importers. (B) Voluntary qualified importer program Fees collected pursuant to subparagraph (C) of subsection (a)(1) shall be available solely for the costs of the voluntary qualified importer program under section 806. .\n##### (c) Limitation on amount\nSection 743(c)(4)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201331(c)(4)(A) ) is amended\u2014\n**(1)**\nin clause (i), by striking $20,000,000 and inserting $25,000,000 ; and\n**(2)**\nin clause (ii), by striking $25,000,000 and inserting $30,000,000 .\n##### (d) Definition of reinspection\nSection 743(a)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201331(a)(2) ) is amended\u2014\n**(1)**\nby amending subparagraph (A) to read as follows:\n(A) the term reinspection means\u2014 (i) with respect to domestic and foreign facilities, 1 or more inspections conducted under section 704 subsequent to an inspection conducted under such provision which identified noncompliance resulting in a classification of official action indicated , specifically to determine whether compliance has been achieved to the Secretary\u2019s satisfaction; and (ii) with respect to importers, 1 or more inspections conducted under the foreign supplier verification program under section 805 subsequent to an inspection conducted under such provision which identified noncompliance resulting in a classification of official action indicated , specifically to determine whether compliance has been achieved to the Secretary\u2019s satisfaction; ;\n**(2)**\nin subparagraph (B)(ii), by striking ; and and inserting a semicolon;\n**(3)**\nin subparagraph (C), by striking the period and inserting a semicolon; and\n**(4)**\nby adding at the end the following:\n(D) the term importer means an importer of human or animal food that is subject to the foreign supplier verification program requirements under section 805; and (E) the term small business means\u2014 (i) with respect to a domestic or foreign facility, a business (including any subsidiaries or affiliates) employing fewer than 500 full-time equivalent employees; (ii) with respect to an importer of human food, an importer (including any subsidiaries and affiliates) averaging less than $1,000,000 per year, adjusted for inflation, during the 3-year period preceding the applicable calendar year, in sales of human food combined with the United States market value of human food imported, manufactured, processed, packed, or held without sale (such as food imported for a fee); and (iii) with respect to an importer of animal food, an importer (including any subsidiaries and affiliates) averaging less than $2,500,000 per year, adjusted for inflation, during the 3-year period preceding the applicable calendar year, in sales of animal food combined with the United States market value of animal food imported, manufactured, processed, packed, or held without sale (such as food imported for a fee). .",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "name": "Health",
        "updateDate": "2026-01-05T15:02:35Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3252is.xml"
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
      "title": "FSMA Fee Technical Corrections Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FSMA Fee Technical Corrections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to make technical corrections to amendments made by the FDA Food Safety Modernization Act to allow the Food and Drug Administration to assess and collect food-related reinspection fees and recall fees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:51Z"
    }
  ]
}
```
