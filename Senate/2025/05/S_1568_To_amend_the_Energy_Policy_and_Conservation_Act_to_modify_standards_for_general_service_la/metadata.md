# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1568?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1568
- Title: LIT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1568
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1568",
    "number": "1568",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "LIT Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T16:48:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "WV"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "AR"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MO"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "UT"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TN"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1568is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1568\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Lee (for himself, Mr. Justice , Mr. Cotton , Mr. Schmitt , Mr. Curtis , and Mr. Hagerty ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Energy Policy and Conservation Act to modify standards for general service lamps, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Liberating Incandescent Technology Act of 2025 or the LIT Act of 2025 .\n#### 2. General services lamps\n##### (a) Covered products\n**(1) In general**\nSection 322(a) of the Energy Policy and Conservation Act ( 42 U.S.C. 6292(a) ) is amended\u2014\n**(A)**\nby striking paragraph (14); and\n**(B)**\nby redesignating paragraphs (15) through (20) as paragraphs (14) through (19), respectively.\n**(2) Conforming amendments**\n**(A)**\nSection 321(6)(B) of the Energy Policy and Conservation Act ( 42 U.S.C. 6291(6)(B) ) is amended by striking (15), (16), (17), and (20) and inserting (14), (15), (16), and (19) .\n**(B)**\nSection 324 of the Energy Policy and Conservation Act ( 42 U.S.C. 6294 ) is amended\u2014\n**(i)**\nin subsection (a)(2)(C)(i), by striking 322(a)(19) and inserting 322(a)(18) ;\n**(ii)**\nin subsection (b)(1)(B), by striking (13), and paragraphs (15) through (20) and inserting (19) ; and\n**(iii)**\nin subsection (c)\u2014\n**(I)**\nin paragraph (7)\u2014\n**(aa)**\nby striking product and inserting products ; and\n**(bb)**\nby striking (17), and (18) and inserting and (17) ; and\n**(II)**\nin paragraph (8), in the matter preceding subparagraph (A), by striking (15) or (17) and inserting (14) or (16) .\n**(C)**\nSection 325(n)(1) of the Energy Policy and Conservation Act ( 42 U.S.C. 6295(n)(1) ) is amended by striking (11), and in paragraphs (13) and (14) and inserting (11) and (13) .\n##### (b) Standards\n**(1) In general**\nSection 325 of the Energy Policy and Conservation Act ( 42 U.S.C. 6295 ) is amended\u2014\n**(A)**\nby striking subsection (i) and inserting the following:\n(i) Reserved ; and\n**(B)**\nin subsection (l), by striking paragraph (4).\n**(2) Conforming amendments**\n**(A)**\nSection 323(b) of the Energy Policy and Conservation Act ( 42 U.S.C. 6293(b) ) is amended\u2014\n**(i)**\nby striking paragraph (6); and\n**(ii)**\nby redesignating paragraphs (7) through (18) as paragraphs (6) through (17), respectively.\n**(B)**\nSection 324(a)(2)(D) of the Energy Policy and Conservation Act ( 42 U.S.C. 6294(a)(2)(D) ) is amended\u2014\n**(i)**\nin clause (i), in the second sentence, by striking Except as provided in clause (ii), such rules and inserting Such rules ;\n**(ii)**\nby striking clause (ii);\n**(iii)**\nby redesignating clause (iii) as clause (ii); and\n**(iv)**\nin subclause (II) of clause (ii) (as so redesignated)\u2014\n**(I)**\nin item (aa), by striking ; and and inserting a period;\n**(II)**\nby striking item (bb); and\n**(III)**\nin the matter preceding item (aa), by striking shall\u2014 and all that follows through complete in item (aa) and inserting shall complete .\n**(C)**\nSection 327 of the Energy Policy and Conservation Act ( 42 U.S.C. 6297 ) is amended\u2014\n**(i)**\nin subsection (b)\u2014\n**(I)**\nin paragraph (1)(B), by striking 2007 in the matter preceding clause (i) and all that follows through the period at the end of clause (ii) and inserting 2007; ; and\n**(II)**\nin paragraph (4), by striking or is a regulation (or portion thereof) regulating fluorescent or incandescent lamps other than those to which section 325(i) is applicable, ; and\n**(ii)**\nin subsection (c)(1), by striking , except that and all that follows through such lamps .\n**(D)**\nSection 334 of the Energy Policy and Conservation Act ( 42 U.S.C. 6304 ) is amended in the second sentence by striking a general service incandescent lamp that does not comply with the applicable standard established under section 325(i) or .\n##### (c) Termination of rules\nThe following rules shall have no force or effect:\n**(1)**\nThe rule of the Department of Energy entitled Energy Conservation Program: Energy Conservation Standards for General Services Lamps (87 Fed. Reg. 27439 (May 9, 2022)).\n**(2)**\nThe rule of the Department of Energy entitled Energy Conservation Program: Definitions for General Service Lamps (87 Fed. Reg. 27461 (May 9, 2022)).\n**(3)**\nThe rule of the Department of Energy entitled Energy Conservation Program: Energy Conservation Standards for General Services Lamps (89 Fed. Reg. 28856 (April 19, 2024)).",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3341",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LIT Act of 2025",
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
        "name": "Energy",
        "updateDate": "2025-06-04T14:44:02Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1568is.xml"
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
      "title": "LIT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LIT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Liberating Incandescent Technology Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy Policy and Conservation Act to modify standards for general service lamps, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:40Z"
    }
  ]
}
```
