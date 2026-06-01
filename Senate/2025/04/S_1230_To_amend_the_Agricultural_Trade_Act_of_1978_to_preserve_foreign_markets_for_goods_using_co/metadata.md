# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1230
- Title: SAFETY Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1230
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-12-05T21:55:19Z
- Update date including text: 2026-04-22T16:27:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2095)
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2095)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1230",
    "number": "1230",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "SAFETY Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:55:19Z",
    "updateDateIncludingText": "2026-04-22T16:27:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2095)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T19:49:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "WI"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "KS"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1230is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1230\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Thune (for himself, Ms. Baldwin , Mr. Marshall , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Trade Act of 1978 to preserve foreign markets for goods using common names, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025 .\n#### 2. Preserving foreign markets for goods using common names\n##### (a) Definitions\nSection 102 of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5602 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking As used in this Act\u2014 and inserting In this Act: ;\n**(2)**\nby redesignating paragraphs (2) through (8) as paragraphs (3), (5), (6), (7), (8), (9), and (4), respectively, and reordering accordingly;\n**(3)**\nby inserting after paragraph (1) the following:\n(2) Common name (A) In general The term common name means a name that\u2014 (i) is ordinarily or customarily used for an agricultural commodity or food product; (ii) is typically placed on the packaging and product label of the agricultural commodity or food product; (iii) with respect to wine\u2014 (I) is\u2014 (aa) ordinarily or customarily used for a wine grape varietal name; or (bb) a traditional term or expression that is typically placed on the packaging and label of the wine; and (II) does not mean any appellation of origin for wine listed in subpart C of part 9 of title 27, Code of Federal Regulations (or successor regulations); and (iv) the use of which is consistent with standards of the Codex Alimentarius Commission. (B) Examples The following names shall be considered common names under subparagraph (A): (i) With respect to food products: (I) American. (II) Asiago. (III) Basmati. (IV) Black forest ham. (V) Bologna. (VI) Bratwurst. (VII) Chevre. (VIII) Chorizo. (IX) Colby. (X) Feta. (XI) Fontina. (XII) Gorgonzola. (XIII) Grana. (XIV) Gruyere. (XV) Kielbasa. (XVI) Limburger and Limburgo. (XVII) Mascarpone. (XVIII) Monterey and Monterey jack. (XIX) Mortadella. (XX) Munster and muenster. (XXI) Neufchatel. (XXII) Parmesan. (XXIII) Pecorino. (XXIV) Pepper Jack. (XXV) Prosciutto. (XXVI) Ricotta. (XXVII) Romano. (XXVIII) Salami. (XXIX) Swiss. (ii) With respect to wine: (I) The list of grape varietal terms in section 4.91 of title 27, Code of Federal Regulations (or a successor regulation). (II) The grape variety designations administratively approved by the Alcohol and Tobacco Tax and Trade Bureau. (III) The following nonvarietal descriptors: (aa) Chateau. (bb) Classic. (cc) Clos. (dd) Cream. (ee) Crusted and Crusting. (ff) Noble. (gg) Ruby. (hh) Sur lie. (ii) Tawny. (jj) Vintage. (kk) Vintage character. (iii) With respect to beer: (I) Bitter. (II) Pale Ale. (III) India Pale Ale. (IV) Mild. (V) Porter. (VI) Stout. (VII) Barleywine. (VIII) Dubbel. (IX) Quadrupel. (X) Witbier. (XI) Saison. (XII) Biere de Garde. (XIII) Oud Red. (XIV) Altbier. (XV) Weisse. (XVI) Gose. (XVII) Hefeweizen. (XVIII) Dunkel. (XIX) Helles. (XX) Rauchbier. (XXI) Pilsener. (XXII) Maerzen. (XXIII) Schwarzbier. (XXIV) Doppelbock. (XXV) Bock. (XXVI) Kellerbier. (XXVII) Munchener and Munich style. (XXVIII) Oktoberfest. (XXIX) Dortmunder. (XXX) Kolsch and Koelsch. (XXXI) Budejovick\u00b4e pivo (Budweiser beer). (XXXII) Cream. (XXXIII) Grodziskie. (XXXIV) Jerez and sherry. (XXXV) Lager. (C) Considerations In making a determination under subparagraph (A), the Secretary may take into account\u2014 (i) competent sources, such as dictionaries, newspapers, professional journals and literature, and information posted on websites that are determined by the Secretary to be reliable in reporting market information; (ii) the use of the common name in a domestic, regional, or international product standard, including a standard promulgated by the Codex Alimentarius Commission, for the agricultural commodity or food product; and (iii) the ordinary and customary use of the common name in the production or marketing of the agricultural commodity or food product in the United States or in other countries. ; and\n**(4)**\nin paragraph (7) (as so redesignated), in subparagraph (A)\u2014\n**(A)**\nin clause (v), by striking or at the end;\n**(B)**\nin clause (vi), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(vii) prohibits or disallows the use of the common name of an agricultural commodity or food product of the United States. .\n##### (b) Negotiations To defend use of common names\nTitle III of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5652 et seq. ) is amended by adding at the end the following:\n303. Negotiations to defend the use of common names (a) In general The Secretary shall coordinate efforts with the United States Trade Representative to secure the right of United States agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters that assure the current and future use of each common name in connection with United States agricultural commodities or food products. (b) Briefing The Secretary and the United States Trade Representative shall jointly provide to the Committee on Agriculture, Nutrition, and Forestry of the Senate, the Committee on Finance of the Senate, the Committee on Agriculture of the House of Representatives, and the Committee on Ways and Means of the House of Representatives a semi-annual briefing on their efforts and success in carrying out subsection (a). .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2558",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAFETY Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-14T17:01:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119s1230",
          "measure-number": "1230",
          "measure-type": "s",
          "orig-publish-date": "2025-04-01",
          "originChamber": "SENATE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1230v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to secure foreign markets for goods using common names.</p><p>In general, the bill defines <em>common name</em> as a name that (1) is ordinarily or customarily used for an agricultural commodity or food product, (2) is typically placed on the packaging and product label of the agricultural commodity or food product, and (3) the use of which is consistent with standards of the Codex Alimentarius Commission. The bill includes a list of names that will be considered common names for (1) food products (e.g., basmati, bratwurst, and parmesan); (2) wine, including grape varietal terms, grape variety designations, and non-varietal descriptors such as chateau and vintage; and (3) beer (e.g., bitter, pale ale, and hefeweizen).</p><p>Specifically, USDA must coordinate efforts with the Office of the U.S. Trade Representative (USTR) to secure the right of U.S. agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets. Through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters, USDA and the USTR must assure the current and future use of each common name in connection with U.S. agricultural commodities or food products.</p><p>USDA and the\u00a0USTR must jointly brief Congress on these efforts on a semi-annual basis.</p>"
        },
        "title": "SAFETY Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1230.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to secure foreign markets for goods using common names.</p><p>In general, the bill defines <em>common name</em> as a name that (1) is ordinarily or customarily used for an agricultural commodity or food product, (2) is typically placed on the packaging and product label of the agricultural commodity or food product, and (3) the use of which is consistent with standards of the Codex Alimentarius Commission. The bill includes a list of names that will be considered common names for (1) food products (e.g., basmati, bratwurst, and parmesan); (2) wine, including grape varietal terms, grape variety designations, and non-varietal descriptors such as chateau and vintage; and (3) beer (e.g., bitter, pale ale, and hefeweizen).</p><p>Specifically, USDA must coordinate efforts with the Office of the U.S. Trade Representative (USTR) to secure the right of U.S. agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets. Through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters, USDA and the USTR must assure the current and future use of each common name in connection with U.S. agricultural commodities or food products.</p><p>USDA and the\u00a0USTR must jointly brief Congress on these efforts on a semi-annual basis.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s1230"
    },
    "title": "SAFETY Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to secure foreign markets for goods using common names.</p><p>In general, the bill defines <em>common name</em> as a name that (1) is ordinarily or customarily used for an agricultural commodity or food product, (2) is typically placed on the packaging and product label of the agricultural commodity or food product, and (3) the use of which is consistent with standards of the Codex Alimentarius Commission. The bill includes a list of names that will be considered common names for (1) food products (e.g., basmati, bratwurst, and parmesan); (2) wine, including grape varietal terms, grape variety designations, and non-varietal descriptors such as chateau and vintage; and (3) beer (e.g., bitter, pale ale, and hefeweizen).</p><p>Specifically, USDA must coordinate efforts with the Office of the U.S. Trade Representative (USTR) to secure the right of U.S. agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets. Through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters, USDA and the USTR must assure the current and future use of each common name in connection with U.S. agricultural commodities or food products.</p><p>USDA and the\u00a0USTR must jointly brief Congress on these efforts on a semi-annual basis.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s1230"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1230is.xml"
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
      "title": "SAFETY Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFETY Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safeguarding American Food and Export Trade Yields Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Trade Act of 1978 to preserve foreign markets for goods using common names, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:53Z"
    }
  ]
}
```
