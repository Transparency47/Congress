# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2705
- Title: Nuclear Family Priority Act
- Congress: 119
- Bill type: HR
- Bill number: 2705
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-05-13T08:06:13Z
- Update date including text: 2026-05-13T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2705",
    "number": "2705",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001132",
        "district": "2",
        "firstName": "Elijah",
        "fullName": "Rep. Crane, Elijah [R-AZ-2]",
        "lastName": "Crane",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Nuclear Family Priority Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:13Z",
    "updateDateIncludingText": "2026-05-13T08:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "GA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "CO"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "AZ"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "TX"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "OH"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "AL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "WI"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "KY"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "TX"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "SC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "KS"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WI"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "GA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "SC"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "WV"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "TN"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "TN"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "SC"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2705ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2705\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Crane introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to make changes related to family-sponsored immigrants and to reduce the number of such immigrants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nuclear Family Priority Act .\n#### 2. Immediate relative definition\nSection 201(b)(2)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(2)(A)(i) ) is amended\u2014\n**(1)**\nby striking children, spouses, and parents and inserting children and spouses ; and\n**(2)**\nby striking States, except that and all that follows through of age. and inserting States. .\n#### 3. Change in family-sponsored immigrant categories\nSection 203(a) of the Immigration and Nationality Act ( 8 U.S.C. 1153(a) ) is amended to read as follows:\n(a) Preference allocation for spouses and children of permanent resident aliens Qualified immigrants who are the spouses or children of an alien lawfully admitted for permanent residence shall be allotted visas in a number not to exceed the worldwide level specified in section 201(c). .\n#### 4. Change in worldwide level of family-sponsored immigrants\nSection 201(c) of the Immigration and Nationality Act ( 8 U.S.C. 1151(c) ) is amended\u2014\n**(1)**\nby amending paragraph (1) to read as follows:\n(1) The worldwide level of family-sponsored immigrants under this subsection for a fiscal year is equal to\u2014 (A) 88,000; minus (B) the number computed under paragraph (2). ;\n**(2)**\nby striking paragraphs (2), (3), and (5); and\n**(3)**\nby redesignating paragraph (4) as paragraph (2).\n#### 5. Conforming amendments\n##### (a) Numerical limitation to any single foreign state\nSection 202 of the Immigration and Nationality Act ( 8 U.S.C. 1152 ) is amended\u2014\n**(1)**\nin subsection (a)(4)\u2014\n**(A)**\nby amending subparagraphs (A) and (B) to read as follows:\n(A) 75 percent of family-sponsored immigrants not subject to per country limitation Of the visa numbers made available under section 203(a) in any fiscal year, 75 percent shall be issued without regard to the numerical limitation under paragraph (2). (B) Treatment of remaining 25 percent for countries subject to subsection (e) (i) In general Of the visa numbers made available under section 203(a) in any fiscal year, the remaining 25 percent shall be available, in the case of a foreign state or dependent area that is subject to subsection (e) only to the extent that the total number of visas issued in accordance with subsection (A) to natives of the foreign state or dependent area is less than the subsection (e) ceiling (as defined in clause (ii)). (ii) Subsection (e) ceiling defined In clause (i), the term subsection (e) ceiling means, for a foreign state or dependent area, 77 percent of the maximum number of visas that may be made available under section 203(a) to immigrants who are natives of the state or area consistent with subsection (e). ; and\n**(B)**\nby striking subparagraphs (C) and (D); and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1), by adding and at the end;\n**(B)**\nby striking paragraph (2) and redesignating paragraph (3) as paragraph (2); and\n**(C)**\nin the final sentence, by striking respectively, and all that follows through the period at the end and inserting respectively. .\n##### (b) Rules for determining whether certain aliens are children\nSection 203(h) of the Immigration and Nationality Act ( 8 U.S.C. 1153(h) ) is amended by striking (a)(2)(A) each place such term appears and inserting (a) .\n##### (c) Procedure for granting immigrant status\nSection 204 of the Immigration and Nationality Act ( 8 U.S.C. 1154 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (A)(i), by striking to classification by reason of a relationship described in paragraph (1), (3), or (4) of section 203(a) or ;\n**(B)**\nin subparagraph (B), by striking 203(a)(2)(A) and 203(a)(2) each place such terms appear and inserting 203(a) ; and\n**(C)**\nin subparagraph (D)(i)(I), by striking a petitioner for preference status under paragraph (1), (2), or (3) and all that follows through the period at the end and inserting an individual under 21 years of age for purposes of adjudicating such petition and for purposes of admission as an immediate relative under section 201(b)(2)(A)(i) or a family-sponsored immigrant under section 203(a), as appropriate, notwithstanding the actual age of the individual. ;\n**(2)**\nin subsection (f)(1), by striking 201(b), 203(a)(1), or 203(a)(3), as appropriate. and inserting 201(b). ; and\n**(3)**\nby striking subsection (k).\n##### (d) Waivers of inadmissibility\nSection 212(d)(11) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(11) ) is amended by striking (other than paragraph (4) thereof) .\n##### (e) Conditional permanent resident status for certain alien spouses and sons and daughters\nSection 216(h)(1)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1186a(h)(1)(C) ) is amended by striking 203(a)(2) and inserting 203(a) .\n##### (f) Classes of deportable aliens\nSection 237(a)(1)(E)(ii) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(1)(E)(ii) ) is amended by striking 203(a)(2) and inserting 203(a) .\n#### 6. Nonimmigrant status for alien parent of adult United States citizens\n##### (a) In general\nSection 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) is amended\u2014\n**(1)**\nin subparagraph (U), by striking or at the end;\n**(2)**\nin subparagraph (V), by striking the period at the end and inserting or ; and\n**(3)**\nby adding at the end the following:\n(W) Subject to section 214(s), an alien who is a parent of a citizen of the United States, if the citizen is at least 21 years of age. .\n##### (b) Conditions on admission\nSection 214 of the Immigration and Nationality Act ( 8 U.S.C. 1184 ) is amended by adding at the end the following:\n(s) (1) The initial period of authorized admission for a nonimmigrant described in section 101(a)(15)(W) shall be 5 years. Such period may be extended by the Secretary of Homeland Security so long as the United States citizen son or daughter of the nonimmigrant is residing in the United States. (2) A nonimmigrant described in section 101(a)(15)(W) is not authorized to be employed in the United States and is not eligible, notwithstanding any other provision of law, for any Federal, State, or local public benefit. In the case of such a nonimmigrant, the United States citizen son or daughter shall be responsible for the support of the nonimmigrant, regardless of the resources of the nonimmigrant. (3) An alien is ineligible to receive a visa and ineligible to be admitted into the United States as a nonimmigrant described in section 101(a)(15)(W) unless the alien provides satisfactory proof that the United States citizen son or daughter has arranged for the provision to the alien, at no cost to the alien, of health insurance coverage applicable during the period of the alien\u2019s presence in the United States. .\n#### 7. Effective date; applicability\nThe amendments made by this Act shall take effect on the first day of the second fiscal year that begins after the date of the enactment of this Act, except that the following shall be considered invalid:\n**(1)**\nAny petition under section 204 of the Immigration and Nationality Act ( 8 U.S.C. 1154 ) seeking classification of an alien under a family-sponsored immigrant category eliminated by the amendments made by this Act that is filed after the date of the introduction of this Act in the House of Representatives.\n**(2)**\nAny application for an immigrant visa based on a petition described in paragraph (1).",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-08",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1328",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Nuclear Family Priority Act",
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
        "name": "Immigration",
        "updateDate": "2025-05-02T12:43:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-08",
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
          "measure-id": "id119hr2705",
          "measure-number": "2705",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-08",
          "originChamber": "HOUSE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2705v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2025-04-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Nuclear Family Priority Act</strong></p><p>This bill imposes limits on various types of family-sponsored immigration visas.</p><p>The\u00a0non-U.S. national\u00a0(<em>alien</em>\u00a0under federal law) parents of U.S. citizens\u00a0shall not qualify for visas for\u00a0immediate relatives, which are not subject to any direct numerical limits. Currently, the spouses, unmarried children under 21, and parents of citizens are considered immediate relatives.</p><p>The bill also creates a nonimmigrant visa for such parents of citizens. Such non-U.S. nationals shall not be eligible for employment or any public benefits.</p><p>The bill also reduces the baseline annual cap for family-sponsored visas from 480,000 to 88,000, and revises the methods for calculating the cap. Currently, the 480,000 cap may be adjusted depending on various factors but shall not be less than 226,000.</p><p>The bill eliminates preference allocations (visa categories subject to various annual caps) for various family-sponsored visas, including those for the siblings and married children of citizens. The bill provides for a preference allocation for the unmarried children under 21 and spouses of permanent residents, subject to the 88,000 annual cap.</p>"
        },
        "title": "Nuclear Family Priority Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2705.xml",
    "summary": {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Nuclear Family Priority Act</strong></p><p>This bill imposes limits on various types of family-sponsored immigration visas.</p><p>The\u00a0non-U.S. national\u00a0(<em>alien</em>\u00a0under federal law) parents of U.S. citizens\u00a0shall not qualify for visas for\u00a0immediate relatives, which are not subject to any direct numerical limits. Currently, the spouses, unmarried children under 21, and parents of citizens are considered immediate relatives.</p><p>The bill also creates a nonimmigrant visa for such parents of citizens. Such non-U.S. nationals shall not be eligible for employment or any public benefits.</p><p>The bill also reduces the baseline annual cap for family-sponsored visas from 480,000 to 88,000, and revises the methods for calculating the cap. Currently, the 480,000 cap may be adjusted depending on various factors but shall not be less than 226,000.</p><p>The bill eliminates preference allocations (visa categories subject to various annual caps) for various family-sponsored visas, including those for the siblings and married children of citizens. The bill provides for a preference allocation for the unmarried children under 21 and spouses of permanent residents, subject to the 88,000 annual cap.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr2705"
    },
    "title": "Nuclear Family Priority Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Nuclear Family Priority Act</strong></p><p>This bill imposes limits on various types of family-sponsored immigration visas.</p><p>The\u00a0non-U.S. national\u00a0(<em>alien</em>\u00a0under federal law) parents of U.S. citizens\u00a0shall not qualify for visas for\u00a0immediate relatives, which are not subject to any direct numerical limits. Currently, the spouses, unmarried children under 21, and parents of citizens are considered immediate relatives.</p><p>The bill also creates a nonimmigrant visa for such parents of citizens. Such non-U.S. nationals shall not be eligible for employment or any public benefits.</p><p>The bill also reduces the baseline annual cap for family-sponsored visas from 480,000 to 88,000, and revises the methods for calculating the cap. Currently, the 480,000 cap may be adjusted depending on various factors but shall not be less than 226,000.</p><p>The bill eliminates preference allocations (visa categories subject to various annual caps) for various family-sponsored visas, including those for the siblings and married children of citizens. The bill provides for a preference allocation for the unmarried children under 21 and spouses of permanent residents, subject to the 88,000 annual cap.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr2705"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2705ih.xml"
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
      "title": "Nuclear Family Priority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nuclear Family Priority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to make changes related to family-sponsored immigrants and to reduce the number of such immigrants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T02:48:26Z"
    }
  ]
}
```
