# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4800
- Title: Fisheries Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4800
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-09-12T18:51:32Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4800",
    "number": "4800",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Fisheries Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-12T18:51:32Z",
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
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:03:15Z",
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
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "LA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4800ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4800\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Higgins of Louisiana (for himself and Mr. Fields ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Magnuson-Stevens Fishery Conservation and Management Act to make certain freshwater fisheries eligible for fishery resource disaster relief.\n#### 1. Short title\nThis Act may be cited as the Fisheries Modernization Act of 2025 .\n#### 2. Certain freshwater fisheries eligible for fishery resource disaster relief\n##### (a) In general\nSection 312(a) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1861a(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), by inserting infrastructure-related cause, after discrete anthropogenic cause, ;\n**(B)**\nby redesignating subparagraphs (E) through (G) as subparagraphs (F) through (H), respectively; and\n**(C)**\nby inserting after subparagraph (D) the following:\n(E) Infrastructure-related cause The term infrastructure-related cause means an event\u2014 (i) caused by the operation or failure of Federal or State infrastructure, including\u2014 (I) flood control systems; (II) spillways; (III) levees; and (IV) diversions; and (ii) that results in measurable disruption to commercial or subsistence fishery activity, aquatic habitat, or water quality. ;\n**(2)**\nin paragraph (2)(A), by inserting , including with respect to the red swamp crawfish (Procambarus clarkii) and white river crawfish (Procambarus zonangulus) fisheries after in accordance with this subsection ;\n**(3)**\nin paragraph (3)(B)(v)\u2014\n**(A)**\nin subclause (III), by striking and at the end;\n**(B)**\nin subclause (IV), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(V) with respect to the red swamp crawfish (Procambarus clarkii) and white river crawfish (Procambarus zonangulus) fisheries, information related to hydrological conditions, water quality degradation, extreme flooding or drought, or other environmental disruptions that directly impact viability. ; and\n**(4)**\nin paragraph (5)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby redesignating clauses (iii) and (iv) as clauses (iv) and (v), respectively;\n**(ii)**\nby inserting after clause (ii) the following:\n(iii) an infrastructure-related cause; ; and\n**(iii)**\nin clause (iv), as so redesignated, by striking a combination of a natural cause and an anthropogenic cause and inserting any combination of clauses (i) through (iii) ; and\n**(B)**\nin subparagraph (D), by striking and safety, and inserting and safety, and including a disaster affecting the red swamp crawfish (Procambarus clarkii) and white river crawfish (Procambarus zonangulus) fisheries, .\n##### (b) Rule of construction\nNothing in this section may be construed to limit, reduce, or otherwise affect the eligibility of any marine or anadromous fishery for fishery resource disaster assistance under section 312 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1861a ).",
      "versionDate": "2025-07-29",
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
        "updateDate": "2025-09-12T18:51:32Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4800ih.xml"
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
      "title": "Fisheries Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fisheries Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Magnuson-Stevens Fishery Conservation and Management Act to make certain freshwater fisheries eligible for fishery resource disaster relief.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T12:18:22Z"
    }
  ]
}
```
