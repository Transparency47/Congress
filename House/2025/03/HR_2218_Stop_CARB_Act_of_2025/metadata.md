# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2218
- Title: Stop CARB Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2218
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-05-20T08:07:43Z
- Update date including text: 2026-05-20T08:07:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2218",
    "number": "2218",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop CARB Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:43Z",
    "updateDateIncludingText": "2026-05-20T08:07:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MN"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "IL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2218ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2218\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Nehls (for himself, Mr. Donalds , Mr. Sessions , Mr. Stauber , Mr. Ogles , and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to eliminate a waiver under that Act, to eliminate an authorization for States to use new motor vehicle emission and new motor vehicle engine emissions standards identical to standards adopted in California, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop California from Advancing Regulatory Burden Act of 2025 or the Stop CARB Act of 2025 .\n#### 2. Repeal of waivers of State standards\n##### (a) In general\nSection 209 of the Clean Air Act ( 42 U.S.C. 7543 ) is amended\u2014\n**(1)**\nby striking subsection (b);\n**(2)**\nin subsection (c), by striking the last sentence;\n**(3)**\nby redesignating subsections (c) and (d) as subsections (b) and (c), respectively; and\n**(4)**\nby striking subsection (e) and inserting the following:\n(d) Prohibition on certain state standards for nonroad engines or vehicles No State or any political subdivision thereof shall adopt or attempt to enforce any standard or other requirement that directly or indirectly relates to the control of emissions from nonroad engines or nonroad vehicles, including the following new nonroad engines or nonroad vehicles subject to regulation under this Act: (1) New engines that are used in construction equipment, construction vehicles, farm equipment, or farm vehicles. (2) New locomotives or new engines used in locomotives. .\n##### (b) Effect\nNotwithstanding any other provision of law, as of the date of enactment of this Act\u2014\n**(1)**\nno waiver issued under subsection (b) of section 209 of the Clean Air Act ( 42 U.S.C. 7543 ) (as in effect on the day before the date of enactment of this Act) before the date of enactment of this Act shall have any force or effect; and\n**(2)**\nany application for a waiver under that subsection (as in effect on the day before the date of enactment of this Act) pending before the Administrator of the Environmental Protection Agency on the date of enactment of this Act shall be considered denied.\n##### (c) Conforming amendments\n**(1)**\nSection 202(i)(2)(A) of the Clean Air Act ( 42 U.S.C. 7521(i)(2)(A) ) is amended, in the matter preceding clause (i), in the first sentence, by striking , taking into consideration the waiver provisions of section 209(b) .\n**(2)**\nSection 211 of the Clean Air Act ( 42 U.S.C. 7545 ) is amended\u2014\n**(A)**\nin subsection (c)(4)\u2014\n**(i)**\nin subparagraph (A), in the matter preceding clause (i), by striking or (C) ;\n**(ii)**\nby striking subparagraph (B); and\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B);\n**(B)**\nin subsection (k)(1)(B)(ii), by striking (other than a refiner or importer in a State that has received a waiver under section 209(b) with respect to gasoline produced for use in that State) ; and\n**(C)**\nin subsection (o)(6)\u2014\n**(i)**\nby striking subparagraph (E);\n**(ii)**\nin subparagraph (F), by striking any State that has received a waiver under section 209(b) or ; and\n**(iii)**\nby redesignating subparagraph (F) as subparagraph (E).\n**(3)**\nSection 241(2) of the Clean Air Act ( 42 U.S.C. 7581(2) is amended, in the second sentence, by striking (or any CARB and all that follows through section 243(e)) .\n**(4)**\nSection 242(b) of the Clean Air Act ( 42 U.S.C. 7582(b) ) is amended by striking except as provided in section 244 with respect to administration and enforcement, and each place it appears.\n**(5)**\nSection 243 of the Clean Air Act ( 42 U.S.C. 7583 ) is amended by striking subsections (e), (f), and (g).\n**(6)**\nSection 244 of the Clean Air Act ( 42 U.S.C. 7584 ) is repealed.\n**(7)**\nSection 247(b) of the Clean Air Act ( 42 U.S.C. 7587(b) ) is amended, in the second sentence, by striking section 242, 243, 244, and inserting sections 242, 243, .\n#### 3. Repeal of authorization to use California new motor vehicle emission standards\n##### (a) In general\nSection 177 of the Clean Air Act ( 42 U.S.C. 7507 ) is repealed.\n##### (b) Conforming amendment\nSection 249(e)(3) of the Clean Air Act ( 42 U.S.C. 7589(e)(3) ) is amended by striking the second sentence.",
      "versionDate": "2025-03-18",
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
        "actionDate": "2025-03-14",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1072",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop CARB Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-04-04T16:00:49Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2218ih.xml"
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
      "title": "Stop CARB Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop CARB Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop California from Advancing Regulatory Burden Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Clean Air Act to eliminate a waiver under that Act, to eliminate an authorization for States to use new motor vehicle emission and new motor vehicle engine emissions standards identical to standards adopted in California, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:20Z"
    }
  ]
}
```
