# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1072?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1072
- Title: Stop CARB Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1072
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1072",
    "number": "1072",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
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
    "title": "Stop CARB Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
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
            "date": "2025-03-14T16:51:18Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-14T16:51:18Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "LA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NE"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "KS"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "ND"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "AK"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OK"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "ID"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "WV"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "WV"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "WY"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "SC"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "OH"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1072is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1072\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mr. Lee (for himself, Mr. Cassidy , Mr. Ricketts , Mr. Marshall , Mr. Daines , Mr. Risch , Mr. Scott of Florida , Mr. Cramer , Mr. Sullivan , Mr. Mullin , Mr. Crapo , Mr. Justice , Mrs. Capito , Mr. Cruz , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Clean Air Act to eliminate a waiver under that Act, to eliminate an authorization for States to use new motor vehicle emission and new motor vehicle engine emissions standards identical to standards adopted in California, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop California from Advancing Regulatory Burden Act of 2025 or the Stop CARB Act of 2025 .\n#### 2. Repeal of waivers of State standards\n##### (a) In general\nSection 209 of the Clean Air Act ( 42 U.S.C. 7543 ) is amended\u2014\n**(1)**\nby striking subsection (b);\n**(2)**\nin subsection (c), by striking the last sentence;\n**(3)**\nby redesignating subsections (c) and (d) as subsections (b) and (c), respectively; and\n**(4)**\nby striking subsection (e) and inserting the following:\n(d) Prohibition on state standards for nonroad engines or vehicles No State or any political subdivision thereof shall adopt or attempt to enforce any standard or other requirement that directly or indirectly relates to the control of emissions from nonroad engines or nonroad vehicles, including the following new nonroad engines or nonroad vehicles subject to regulation under this Act: (1) New engines that are used in construction equipment, construction vehicles, farm equipment, or farm vehicles. (2) New locomotives or new engines used in locomotives. .\n##### (b) Effect\nNotwithstanding any other provision of law, as of the date of enactment of this Act\u2014\n**(1)**\nno waiver issued under subsection (b) of section 209 of the Clean Air Act ( 42 U.S.C. 7543 ) (as in effect on the day before the date of enactment of this Act) before the date of enactment of this Act shall have any force or effect; and\n**(2)**\nany application for a waiver under that subsection (as in effect on the day before the date of enactment of this Act) pending before the Administrator of the Environmental Protection Agency on the date of enactment of this Act shall be considered denied.\n##### (c) Conforming amendments\n**(1)**\nSection 202(i)(2)(A) of the Clean Air Act ( 42 U.S.C. 7521(i)(2)(A) ) is amended, in the matter preceding clause (i), in the first sentence, by striking , taking into consideration the waiver provisions of section 209(b) .\n**(2)**\nSection 211 of the Clean Air Act ( 42 U.S.C. 7545 ) is amended\u2014\n**(A)**\nin subsection (c)(4)\u2014\n**(i)**\nin subparagraph (A), in the matter preceding clause (i), by striking or (C) ;\n**(ii)**\nby striking subparagraph (B); and\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B);\n**(B)**\nin subsection (k)(1)(B)(ii), by striking (other than a refiner or importer in a State that has received a waiver under section 209(b) with respect to gasoline produced for use in that State) ; and\n**(C)**\nin subsection (o)(6)\u2014\n**(i)**\nby striking subparagraph (E);\n**(ii)**\nin subparagraph (F), by striking any State that has received a waiver under section 209(b) or ; and\n**(iii)**\nby redesignating subparagraph (F) as subparagraph (E).\n**(3)**\nSection 241(2) of the Clean Air Act ( 42 U.S.C. 7581(2) ) is amended, in the second sentence, by striking (or any CARB and all that follows through section 243(e)) .\n**(4)**\nSection 242(b) of the Clean Air Act ( 42 U.S.C. 7582(b) ) is amended by striking except as provided in section 244 with respect to administration and enforcement, and each place it appears.\n**(5)**\nSection 243 of the Clean Air Act ( 42 U.S.C. 7583 ) is amended by striking subsections (e), (f), and (g).\n**(6)**\nSection 244 of the Clean Air Act ( 42 U.S.C. 7584 ) is repealed.\n**(7)**\nSection 247(b) of the Clean Air Act ( 42 U.S.C. 7587(b) ) is amended, in the second sentence, by striking section 242, 243, 244, and inserting sections 242, 243, .\n#### 3. Repeal of authorization to use California new motor vehicle emission standards\n##### (a) In general\nSection 177 of the Clean Air Act ( 42 U.S.C. 7507 ) is repealed.\n##### (b) Conforming amendment\nSection 249(e)(3) of the Clean Air Act ( 42 U.S.C. 7589(e)(3) ) is amended by striking the second sentence.",
      "versionDate": "2025-03-14",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2218",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop CARB Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-04-11T12:13:21Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1072is.xml"
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
      "title": "Stop CARB Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop CARB Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop California from Advancing Regulatory Burden Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Clean Air Act to eliminate a waiver under that Act, to eliminate an authorization for States to use new motor vehicle emission and new motor vehicle engine emissions standards identical to standards adopted in California, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:18:17Z"
    }
  ]
}
```
