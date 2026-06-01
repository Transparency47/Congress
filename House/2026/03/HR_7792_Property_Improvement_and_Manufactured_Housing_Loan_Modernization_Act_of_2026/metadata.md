# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7792?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7792
- Title: Property Improvement and Manufactured Housing Loan Modernization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7792
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-03-09T17:10:51Z
- Update date including text: 2026-03-09T17:10:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7792",
    "number": "7792",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "H001047",
        "district": "4",
        "firstName": "James",
        "fullName": "Rep. Himes, James A. [D-CT-4]",
        "lastName": "Himes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Property Improvement and Manufactured Housing Loan Modernization Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-09T17:10:51Z",
    "updateDateIncludingText": "2026-03-09T17:10:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7792ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7792\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mr. Himes (for himself, Mr. Pappas , Mr. Harder of California , and Mr. Liccardo ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend title I of the National Housing Act to increase the loan limits and clarify that property improvement loans may be used for construction of accessory dwelling units.\n#### 1. Short title\nThis Act may be cited as the Property Improvement and Manufactured Housing Loan Modernization Act of 2026 .\n#### 2. National Housing Act amendments\n##### (a) In general\nSection 2 of the National Housing Act ( 12 U.S.C. 1703 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting construction of additional or accessory dwelling units, as defined by the Secretary, after improvements, ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking subparagraph (A) and inserting the following new subparagraph:\n(A) $75,000 if made for the purpose of financing alterations, repairs and improvements upon or in connection with an existing single-family structure, including a manufactured home; ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking $60,000 and inserting $150,000 ;\n**(II)**\nby striking $12,000 and inserting $37,500 ; and\n**(III)**\nby striking an apartment house or ;\n**(iii)**\nby striking subparagraphs (C) and (D) and inserting the following:\n(C) (i) $106,405 if made for the purpose of financing the purchase of a single-section manufactured home; and (ii) $195,322 if made for the purpose of financing the purchase of a multi-section manufactured home; (D) (i) $149,782 if made for the purpose of financing the purchase of a single-section manufactured home and a suitably developed lot on which to place the home; and (ii) $238,699 if made for the purpose of financing the purchase of a multi-section manufactured home and a suitably developed lot on which to place the home; ;\n**(iv)**\nin subparagraph (E)\u2014\n**(I)**\nby striking $23,226 and inserting $43,377 ; and\n**(II)**\nby striking the period at the end and inserting a semicolon;\n**(v)**\nin subparagraph (F), by striking and at the end;\n**(vi)**\nin subparagraph (G), by striking the period at the end and inserting ; and ; and\n**(vii)**\nby inserting after subparagraph (G) the following:\n(H) such principal amount as the Secretary may prescribe if made for the purpose of financing the construction of an accessory dwelling unit. ; and\n**(viii)**\nin the matter preceding paragraph (2)\u2014\n**(I)**\nby striking regulation and inserting notice ;\n**(II)**\nby striking increase and inserting set ;\n**(III)**\nby striking (ii), (C), (D), and (E) and inserting through (H) ;\n**(IV)**\nby inserting , or as necessary to achieve the goals of the Federal Housing Administration, periodically reset the dollar amount limitations in subparagraphs (A) through (H) based on justification and methodology set forth in advance by regulation before the period at the end; and\n**(V)**\nby adjusting the margins appropriately;\n**(B)**\nin paragraph (3), by striking exceeds\u2014 and all that follows through the period at the end and inserting exceeds such period of time as determined by the Secretary, not to exceed 30 years. ;\n**(C)**\nby striking paragraph (9) and inserting the following:\n(9) Annual indexing of certain dollar amount limitations The Secretary shall develop or choose 1 or more methods of indexing in order to annually set the loan limits established in paragraph (1), based on data the Secretary determines is appropriate for purposes of this section. ; and\n**(D)**\nin paragraph (11), by striking lease\u2014 and all that follows through the period at the end and inserting unless such lease meets the terms and conditions established by the Secretary .\n##### (b) Deadline for development or choice of new index; interim index\n**(1) Deadline for development or choice of new index**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Housing and Urban Development shall develop or choose 1 or more methods of indexing as required under section 2(b)(9) of the National Housing Act ( 12 U.S.C. 1703(b)(9) ), as amended by subsection (a) of this section.\n**(2) Interim index**\nDuring the period beginning on the date of enactment of this Act and ending on the date on which the Secretary of Housing and Urban Development develops or chooses 1 or more methods of indexing as required under section 2(b)(9) of the National Housing Act ( 12 U.S.C. 1703(b)(9) ), as amended by subsection (a) of this section, the method of indexing established by the Secretary under that section before the date of enactment of this Act shall apply.\n#### 3. HUD study of off-site construction\n##### (a) Definitions\nIn this section:\n**(1) Off-site construction housing**\nThe term off-site construction housing includes manufactured homes and modular homes.\n**(2) Manufactured home**\nThe term manufactured home means any home constructed in accordance with the construction and safety standards established under the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5401 et seq. ).\n**(3) Modular home**\nThe term modular home means a home that is constructed in a factory in 1 or more modules, each of which meets applicable State and local building codes of the area in which the home will be located, and that are transported to the home building site, installed on foundations, and completed.\n##### (b) Study\nThe Secretary of Housing and Urban Development shall conduct a study and submit to Congress a report on the cost effectiveness of off-site construction housing, that includes\u2014\n**(1)**\nan analysis of the advantages and the impact of centralization in a factory and transportation to a construction site on cost, precision, and materials waste;\n**(2)**\nthe extent to which off-site construction housing meets housing quality standards under the National Standards for the Physical Inspection of Real Estate, or other standards as the Secretary may prescribe, compared to the extent for site-built homes, for such standards;\n**(3)**\nthe expected replacement and maintenance costs over the first 40 years of life of off-site construction homes compared to those costs for site-built homes; and\n**(4)**\nopportunities for use beyond single-family housing, such as applications in accessory dwelling units, two- to four-unit housing, and large multifamily housing.",
      "versionDate": "2026-03-04",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-03-09T17:10:51Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7792ih.xml"
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
      "title": "Property Improvement and Manufactured Housing Loan Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Property Improvement and Manufactured Housing Loan Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title I of the National Housing Act to increase the loan limits and clarify that property improvement loans may be used for construction of accessory dwelling units.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T09:18:22Z"
    }
  ]
}
```
