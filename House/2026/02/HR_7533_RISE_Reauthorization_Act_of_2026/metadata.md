# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7533?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7533
- Title: RISE Reauthorization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7533
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-03-13T08:05:49Z
- Update date including text: 2026-03-13T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7533",
    "number": "7533",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000481",
        "district": "2",
        "firstName": "Shomari",
        "fullName": "Rep. Figures, Shomari [D-AL-2]",
        "lastName": "Figures",
        "party": "D",
        "state": "AL"
      }
    ],
    "title": "RISE Reauthorization Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-13T08:05:49Z",
    "updateDateIncludingText": "2026-03-13T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:01:40Z",
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
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "AL"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7533ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7533\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Figures (for himself, Mr. Mannion , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to reauthorize and expand the Rural Innovation Stronger Economy grant program.\n#### 1. Short title\nThis Act may be cited as the Rural Innovation Stronger Economy Reauthorization Act of 2026 or the RISE Reauthorization Act of 2026 .\n#### 2. Rural Innovation Stronger Economy grant program reauthorization and expansion\n##### (a) In general\nSection 379I of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008w ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)(i)\u2014\n**(I)**\nby striking the industry clusters that are objectively identified as ; and\n**(II)**\nby inserting industries in the area served by the partnership after declining ; and\n**(ii)**\nin subparagraph (B)(ii)\u2014\n**(I)**\nby striking subclause (I); and\n**(II)**\nby redesignating subclauses (II) through (IV) as subclauses (I) through (III), respectively;\n**(B)**\nby striking paragraph (2); and\n**(C)**\nby redesignating paragraphs (3) through (5) as paragraphs (2) through (4), respectively;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and indenting the clauses appropriately;\n**(ii)**\nin clause (ii) (as so redesignated), by striking opportunities, networks, and industry clusters and inserting opportunities and networks ;\n**(iii)**\nby striking the paragraph designation and heading and all that follows through The Secretary in the matter preceding clause (i) (as so redesignated) and inserting the following:\n(1) Grant program (A) In general The Secretary ; and\n**(iv)**\nby adding at the end the following:\n(B) Targeted community types In carrying out the grant program under this paragraph, the Secretary shall\u2014 (i) target a broad base of rural community types that will benefit from the program, with an emphasis on communities with a population of fewer than 20,000 inhabitants; and (ii) of the total amount of grants awarded for each fiscal year, award not less than 10 percent to carry out activities that will benefit rural communities with a population of fewer than 10,000 inhabitants. ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby redesignating clauses (i) and (ii) as subclauses (I) and (II), respectively, and indenting the subclauses appropriately; and\n**(II)**\nin subclause (II) (as so redesignated), by striking industry cluster ;\n**(ii)**\nby striking subparagraph (C);\n**(iii)**\nin subparagraph (D), by striking industry clusters, ;\n**(iv)**\nby redesignating subparagraphs (A), (B), (D), (E), and (F) as clauses (i), (ii), (iii), (iv), and (v), respectively, and indenting the clauses appropriately; and\n**(v)**\nin the matter preceding clause (i) (as so redesignated), by striking shall consider\u2014 and inserting the following:\nshall\u2014 (A) ensure that a diverse set of industry bases is represented; (B) only select an eligible entity to receive a grant with the concurrence of the applicable State office of the rural development mission area; and (C) take into consideration\u2014 ;\n**(3)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (A), by adding and after the semicolon at the end; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking industry clusters, ;\n**(ii)**\nin clause (vii), by striking small businesses in regional industry clusters, including ;\n**(iii)**\nin clause (ix), by striking in the identified industry clusters ; and\n**(iv)**\nin clause (x), by striking industry cluster ;\n**(4)**\nin subsection (e)(2)(B)\u2014\n**(A)**\nin clause (viii)\u2014\n**(i)**\nin subclause (I), by striking industry cluster and inserting activities funded with the grant ; and\n**(ii)**\nin subclause (II), by striking held by the industry cluster and inserting relating to those activities convened by relevant organizations ;\n**(B)**\nin clauses (xi) and (xii), by striking industry cluster each place it appears and inserting participating regional ; and\n**(C)**\nin clause (xiii), by striking the project activities and inserting activities funded with the grant ; and\n**(5)**\nby striking subsection (f) and inserting the following:\n(f) Authorization of appropriations There are authorized to be appropriated to carry out this section $50,000,000 for each of fiscal years 2026 through 2030. .\n##### (b) Conforming amendment\nSection 6306(h)(3)(B)(ii) of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2204b\u20133(h)(3)(B)(ii) ) is amended, in the matter preceding subclause (I), by striking section 379I(a)(4) of the Consolidated Farm and Rural Development Act and inserting section 379I(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008w(a) ) .",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3861",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Innovation Stronger Economy (RISE) Reauthorization Act of 2026",
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
        "updateDate": "2026-02-27T16:29:55Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7533ih.xml"
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
      "title": "RISE Reauthorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RISE Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Innovation Stronger Economy Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to reauthorize and expand the Rural Innovation Stronger Economy grant program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T06:18:35Z"
    }
  ]
}
```
