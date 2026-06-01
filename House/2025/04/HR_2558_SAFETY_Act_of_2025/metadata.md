# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2558?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2558
- Title: SAFETY Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2558
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-04-10T20:11:55Z
- Update date including text: 2026-04-22T16:27:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-01 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-01 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2558",
    "number": "2558",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "SAFETY Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T20:11:55Z",
    "updateDateIncludingText": "2026-04-22T16:27:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:07:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-01T14:06:50Z",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "WI"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "MN"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2558ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2558\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Johnson of South Dakota (for himself, Mr. Costa , Mrs. Fischbach , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Agricultural Trade Act of 1978 to preserve foreign markets for goods using common names, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025 .\n#### 2. Preserving foreign markets for goods using common names\n##### (a) Definitions\nSection 102 of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5602 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking As used in this Act\u2014 and inserting In this Act: ;\n**(2)**\nby redesignating paragraphs (2) through (8) as paragraphs (3), (5), (6), (7), (8), (9), and (4), respectively, and reordering accordingly;\n**(3)**\nby inserting after paragraph (1) the following:\n(2) Common name (A) In general The term common name means a name that\u2014 (i) is ordinarily or customarily used for an agricultural commodity or food product; (ii) is typically placed on the packaging and product label of the agricultural commodity or food product; (iii) with respect to wine\u2014 (I) is\u2014 (aa) ordinarily or customarily used for a wine grape varietal name; or (bb) a traditional term or expression that is typically placed on the packaging and label of the wine; and (II) does not mean any appellation of origin for wine listed in subpart C of part 9 of title 27, Code of Federal Regulations (or successor regulations); and (iv) the use of which is consistent with standards of the Codex Alimentarius Commission. (B) Examples The following names shall be considered common names under subparagraph (A): (i) With respect to food products: (I) American. (II) Asiago. (III) Basmati. (IV) Black forest ham. (V) Bologna. (VI) Bratwurst. (VII) Chevre. (VIII) Chorizo. (IX) Colby. (X) Feta. (XI) Fontina. (XII) Gorgonzola. (XIII) Grana. (XIV) Gruyere. (XV) Kielbasa. (XVI) Limburger and Limburgo. (XVII) Mascarpone. (XVIII) Monterey and Monterey jack. (XIX) Mortadella. (XX) Munster and muenster. (XXI) Neufchatel. (XXII) Parmesan. (XXIII) Pecorino. (XXIV) Pepper Jack. (XXV) Prosciutto. (XXVI) Ricotta. (XXVII) Romano. (XXVIII) Salami. (XXIX) Swiss. (ii) With respect to wine: (I) The list of grape varietal terms in section 4.91 of title 27, Code of Federal Regulations (or a successor regulation). (II) The grape variety designations administratively approved by the Alcohol and Tobacco Tax and Trade Bureau. (III) The following nonvarietal descriptors: (aa) Chateau. (bb) Classic. (cc) Clos. (dd) Cream. (ee) Crusted and Crusting. (ff) Noble. (gg) Ruby. (hh) Sur lie. (ii) Tawny. (jj) Vintage. (kk) Vintage character. (iii) With respect to beer: (I) Bitter. (II) Pale Ale. (III) India Pale Ale. (IV) Mild. (V) Porter. (VI) Stout. (VII) Barleywine. (VIII) Dubbel. (IX) Quadrupel. (X) Witbier. (XI) Saison. (XII) Biere de Garde. (XIII) Oud Red. (XIV) Altbier. (XV) Weisse. (XVI) Gose. (XVII) Hefeweizen. (XVIII) Dunkel. (XIX) Helles. (XX) Rauchbier. (XXI) Pilsener. (XXII) Maerzen. (XXIII) Schwarzbier. (XXIV) Doppelbock. (XXV) Bock. (XXVI) Kellerbier. (XXVII) Munchener and Munich style. (XXVIII) Oktoberfest. (XXIX) Dortmunder. (XXX) Kolsch and Koelsch. (XXXI) Budejovick\u00b4e pivo (Budweiser beer). (XXXII) Cream. (XXXIII) Grodziskie. (XXXIV) Jerez and sherry. (XXXV) Lager. (C) Considerations In making a determination under subparagraph (A), the Secretary may take into account\u2014 (i) competent sources, such as dictionaries, newspapers, professional journals and literature, and information posted on websites that are determined by the Secretary to be reliable in reporting market information; (ii) the use of the common name in a domestic, regional, or international product standard, including a standard promulgated by the Codex Alimentarius Commission, for the agricultural commodity or food product; and (iii) the ordinary and customary use of the common name in the production or marketing of the agricultural commodity or food product in the United States or in other countries. ; and\n**(4)**\nin paragraph (7) (as so redesignated), in subparagraph (A)\u2014\n**(A)**\nin clause (v), by striking or at the end;\n**(B)**\nin clause (vi), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(vii) prohibits or disallows the use of the common name of an agricultural commodity or food product of the United States. .\n##### (b) Negotiations To defend use of common names\nTitle III of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5652 et seq. ) is amended by adding at the end the following:\n303. Negotiations to defend the use of common names (a) In general The Secretary shall coordinate efforts with the United States Trade Representative to secure the right of United States agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters that assure the current and future use of each common name in connection with United States agricultural commodities or food products. (b) Briefing The Secretary and the United States Trade Representative shall jointly provide to the Committee on Agriculture, Nutrition, and Forestry of the Senate, the Committee on Finance of the Senate, the Committee on Agriculture of the House of Representatives, and the Committee on Ways and Means of the House of Representatives a semi-annual briefing on their efforts and success in carrying out subsection (a). .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2026-04-21",
        "text": "Placed on the Union Calendar, Calendar No. 537."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2095)"
      },
      "number": "1230",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAFETY Act of 2025",
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
        "updateDate": "2025-05-14T16:49:35Z"
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
          "measure-id": "id119hr2558",
          "measure-number": "2558",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2558v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to secure foreign markets for goods using common names.</p><p>In general, the bill defines <em>common name</em> as a name that (1) is ordinarily or customarily used for an agricultural commodity or food product, (2) is typically placed on the packaging and product label of the agricultural commodity or food product, and (3) the use of which is consistent with standards of the Codex Alimentarius Commission. The bill includes a list of names that will be considered common names for (1) food products (e.g., basmati, bratwurst, and parmesan); (2) wine, including grape varietal terms, grape variety designations, and non-varietal descriptors such as chateau and vintage; and (3) beer (e.g., bitter, pale ale, and hefeweizen).</p><p>Specifically, USDA must coordinate efforts with the Office of the U.S. Trade Representative (USTR) to secure the right of U.S. agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets. Through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters, USDA and the USTR must assure the current and future use of each common name in connection with U.S. agricultural commodities or food products.</p><p>USDA and the\u00a0USTR must jointly brief Congress on these efforts on a semi-annual basis.</p>"
        },
        "title": "SAFETY Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2558.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to secure foreign markets for goods using common names.</p><p>In general, the bill defines <em>common name</em> as a name that (1) is ordinarily or customarily used for an agricultural commodity or food product, (2) is typically placed on the packaging and product label of the agricultural commodity or food product, and (3) the use of which is consistent with standards of the Codex Alimentarius Commission. The bill includes a list of names that will be considered common names for (1) food products (e.g., basmati, bratwurst, and parmesan); (2) wine, including grape varietal terms, grape variety designations, and non-varietal descriptors such as chateau and vintage; and (3) beer (e.g., bitter, pale ale, and hefeweizen).</p><p>Specifically, USDA must coordinate efforts with the Office of the U.S. Trade Representative (USTR) to secure the right of U.S. agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets. Through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters, USDA and the USTR must assure the current and future use of each common name in connection with U.S. agricultural commodities or food products.</p><p>USDA and the\u00a0USTR must jointly brief Congress on these efforts on a semi-annual basis.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr2558"
    },
    "title": "SAFETY Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safeguarding American Food and Export Trade Yields Act of 2025 or the SAFETY Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to secure foreign markets for goods using common names.</p><p>In general, the bill defines <em>common name</em> as a name that (1) is ordinarily or customarily used for an agricultural commodity or food product, (2) is typically placed on the packaging and product label of the agricultural commodity or food product, and (3) the use of which is consistent with standards of the Codex Alimentarius Commission. The bill includes a list of names that will be considered common names for (1) food products (e.g., basmati, bratwurst, and parmesan); (2) wine, including grape varietal terms, grape variety designations, and non-varietal descriptors such as chateau and vintage; and (3) beer (e.g., bitter, pale ale, and hefeweizen).</p><p>Specifically, USDA must coordinate efforts with the Office of the U.S. Trade Representative (USTR) to secure the right of U.S. agricultural producers, processors, and exporters to use common names for agricultural commodities or food products in foreign markets. Through the negotiation of bilateral, plurilateral, or multilateral agreements, memoranda of understanding, or exchanges of letters, USDA and the USTR must assure the current and future use of each common name in connection with U.S. agricultural commodities or food products.</p><p>USDA and the\u00a0USTR must jointly brief Congress on these efforts on a semi-annual basis.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr2558"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2558ih.xml"
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
      "title": "SAFETY Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFETY Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding American Food and Export Trade Yields Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Trade Act of 1978 to preserve foreign markets for goods using common names, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:44Z"
    }
  ]
}
```
