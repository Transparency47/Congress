# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6150?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6150
- Title: Protect American Fisheries Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6150
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-02-25T09:06:31Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6150",
    "number": "6150",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Protect American Fisheries Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:31Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "LA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AL"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "ME"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "LA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6150ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6150\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Ms. Mace (for herself, Mr. Donalds , Mr. Carter of Louisiana , Mr. Moore of Alabama , Mr. Golden of Maine , Mr. Weber of Texas , Mr. Vicente Gonzalez of Texas , Mr. Higgins of Louisiana , and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Magnuson-Stevens Fishery Conservation and Management Act to add an economic cause as an allowable cause to declare a fishery resource disaster.\n#### 1. Short title\nThis Act may be cited as the Protect American Fisheries Act of 2025 .\n#### 2. Economic fishery resource disasters\nSection 312(a) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1861a(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), by inserting economic cause, after discrete anthropogenic cause, ;\n**(B)**\nby redesignating subparagraphs (D) through (G) as subparagraphs (F) through (I), respectively;\n**(C)**\nby redesignating subparagraph (C) as subparagraph (D);\n**(D)**\nby inserting after subparagraph (B) the following:\n(C) Economic cause The term economic cause means any activity carried out by a foreign person that the Secretary determines\u2014 (i) distorts the market for a fishery resource; (ii) disrupts the sustainable harvest of a fishery resource; or (iii) hinders the operational or economic viability of a fishery resource. ;\n**(E)**\nin subparagraph (D)(i), as so redesignated, by inserting or significant disruption to the fishery resource or economy of a fishing community after fishery resource ; and\n**(F)**\nby inserting after subparagraph (D), as so redesignated, the following:\n(E) Foreign person The term foreign person means\u2014 (i) an individual who is not a citizen or national of the United States; (ii) a government of a foreign country and any unit of such government; (iii) an international financial institution (as the term international financial institutions is defined in section 1701(c) of the International Financial Institutions Act ( 22 U.S.C. 262r(c) )); (iv) a partnership, association, corporation, organization, or other combination of persons organized under the laws of or having its principal place of business in a foreign country; and (v) a partnership, association, corporation, organization, or other combination of persons organized under the laws of the United States that is owned by, directly or indirectly controlled by, or subject to the direction of a person or an entity described in clauses (i) through (iv). ;\n**(2)**\nin paragraph (3)(B)(v)\u2014\n**(A)**\nin subclause (III), by striking and at the end;\n**(B)**\nin subclause (IV), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after subclause (IV) the following:\n(V) if applicable with respect to the cause of the fishery resource disaster, information documenting the adverse effects of activities carried out by a foreign person on the operational or economic viability of the applicable fishery, including\u2014 (aa) illegal, unreported, or unregulated fishing, including the use of forced or child labor; (bb) predatory pricing; and (cc) the provision of subsidies that\u2014 (AA) have an adverse effect on the price in the United States or export markets of seafood produced by the applicable fishery; or (BB) otherwise cause a distortion of such markets. ;\n**(3)**\nin paragraph (4)(B)(i)(II)\u2014\n**(A)**\nin item (ii), by striking and at the end;\n**(B)**\nin item (jj), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(kk) prices in the United States or export markets of seafood produced in the fishery; and (ll) if the requester submits information described in paragraph (3)(B)(v)(V), any activities carried out by a foreign person that contribute to an economic cause of the fishery resource disaster and the specific economic effects thereof. ; and\n**(4)**\nin paragraph (5)(A)\u2014\n**(A)**\nin clause (iii)\u2014\n**(i)**\nby striking a combination and inserting any combination ; and\n**(ii)**\nby striking and an anthropogenic cause and inserting , anthropogenic cause, or economic cause ;\n**(B)**\nby redesignating clauses (iii) and (iv) as clauses (iv) and (v), respectively; and\n**(C)**\nby inserting after clause (ii) the following:\n(iii) an economic cause; .",
      "versionDate": "2025-11-19",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-09T22:37:21Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6150ih.xml"
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
      "title": "Protect American Fisheries Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T10:08:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect American Fisheries Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T10:08:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Magnuson-Stevens Fishery Conservation and Management Act to add an economic cause as an allowable cause to declare a fishery resource disaster.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T10:03:30Z"
    }
  ]
}
```
