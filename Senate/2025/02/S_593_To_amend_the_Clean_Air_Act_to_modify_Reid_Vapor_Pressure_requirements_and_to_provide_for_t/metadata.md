# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/593?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/593
- Title: Nationwide Consumer and Fuel Retailer Choice Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 593
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-04-14T11:03:25Z
- Update date including text: 2026-04-14T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/593",
    "number": "593",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Nationwide Consumer and Fuel Retailer Choice Act of 2025",
    "type": "S",
    "updateDate": "2026-04-14T11:03:25Z",
    "updateDateIncludingText": "2026-04-14T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
            "date": "2025-02-13T20:04:46Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-13T20:04:46Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MN"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "KS"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "KS"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MN"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SD"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "MS"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "ND"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "AZ"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "WV"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "KY"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "IN"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s593is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 593\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mrs. Fischer (for herself, Ms. Duckworth , Mrs. Capito , Ms. Klobuchar , Mr. Thune , Mr. Ricketts , Mr. Durbin , Mr. Moran , Mr. Marshall , Mr. Grassley , Ms. Ernst , Ms. Baldwin , Ms. Smith , and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Clean Air Act to modify Reid Vapor Pressure requirements and to provide for the return of certain retired credits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nationwide Consumer and Fuel Retailer Choice Act of 2025 .\n#### 2. Clean Air Act amendments\n##### (a) Ethanol waiver\n**(1) Existing waivers**\nSection 211(f)(4) of the Clean Air Act ( 42 U.S.C. 7545(f)(4) ) is amended\u2014\n**(A)**\nby striking (4) The Administrator, upon and inserting the following:\n(4) Waivers (A) In general The Administrator, on ;\n**(B)**\nin subparagraph (A) (as so designated)\u2014\n**(i)**\nin the first sentence\u2014\n**(I)**\nby striking of this subsection each place it appears; and\n**(II)**\nby striking if he determines and inserting if the Administrator determines ; and\n**(ii)**\nin the second sentence, by striking The Administrator and inserting the following:\n(B) Final action The Administrator ; and\n**(C)**\nby adding at the end the following:\n(C) Reid vapor pressure A fuel or fuel additive may be introduced into commerce if\u2014 (i) (I) the Administrator determines that the fuel or fuel additive is substantially similar to a fuel or fuel additive utilized in the certification of any model year vehicle pursuant to paragraph (1)(A); or (II) the fuel or fuel additive has been granted a waiver under subparagraph (A) and meets all of the conditions of that waiver other than any limitation of the waiver with respect to the Reid Vapor Pressure of the fuel or fuel additive; and (ii) the fuel or fuel additive meets all other applicable Reid Vapor Pressure requirements under subsection (h). .\n**(2) Reid vapor pressure limitation**\nSection 211(h) of the Clean Air Act ( 42 U.S.C. 7545(h) ) is amended\u2014\n**(A)**\nby striking vapor pressure each place it appears and inserting Vapor Pressure ;\n**(B)**\nin paragraph (4), in the matter preceding subparagraph (A), by striking 10 percent and inserting 10 to 15 percent ; and\n**(C)**\nin paragraph (5)(A)\u2014\n**(i)**\nby striking Upon notification, accompanied by and inserting On receipt of a notification that is submitted after the date of enactment of the Nationwide Consumer and Fuel Retailer Choice Act of 2025 , and is accompanied by appropriate ;\n**(ii)**\nby striking 10 percent and inserting 10 to 15 percent ; and\n**(iii)**\nby adding at the end the following: Upon the enactment of the Nationwide Consumer and Fuel Retailer Choice Act of 2025 , any State for which the notification from the Governor of a State was submitted before the date of enactment of the Nationwide Consumer and Fuel Retailer Choice Act of 2025 and to which the Administrator applied the Reid Vapor Pressure limitation established by paragraph (1) shall instead have the Reid Vapor Pressure limitation established by paragraph (4) apply to all fuel blends containing gasoline and 10 to 15 percent denatured anhydrous ethanol that are sold, offered for sale, dispensed, supplied, offered for supply, transported, or introduced into commerce in the area during the high ozone season. .\n##### (b) Generation of credits by small refineries under the renewable fuel program\nSection 211(o)(9) of the Clean Air Act ( 42 U.S.C. 7545(o)(9) ) is amended by adding at the end the following:\n(E) Credits generated for 2016\u20132018 compliance years (i) Rule For any small refinery described in clause (ii) or (iii), the credits described in the respective clause shall be\u2014 (I) returned to the small refinery and, notwithstanding paragraph (5)(C), deemed eligible for future compliance years; or (II) applied as a credit in the EPA Moderated Transaction System (EMTS) account of the small refinery. (ii) Compliance years 2016 and 2017 Clause (i) applies with respect to any small refinery that\u2014 (I) retired credits generated for compliance years 2016 or 2017; and (II) submitted a petition under subparagraph (B)(i) for that compliance year that remained outstanding as of December 1, 2022. (iii) Compliance year 2018 In addition to small refineries described in clause (ii), clause (i) applies with respect to any small refinery\u2014 (I) that submitted a petition under subparagraph (B)(i) for compliance year 2018 by September 1, 2019; (II) that retired credits generated for compliance year 2018 as part of the compliance demonstration of the small refinery for compliance year 2018 by March 31, 2019; and (III) for which\u2014 (aa) the petition remained outstanding as of December 1, 2022; or (bb) the Administrator denied the petition as of July 1, 2022, and has not returned the retired credits as of December 1, 2022. .",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1346",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Nationwide Consumer and Fuel Retailer Choice Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
        "updateDate": "2025-03-13T15:19:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s593",
          "measure-number": "593",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s593v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Nationwide Consumer and Fuel Retailer Choice Act of 2025</strong></p><p>This bill amends the Clean Air Act to address the limitations on Reid Vapor Pressure (a measure of gasoline's volatility) that are placed on gasoline during the summer ozone season. Specifically, the bill applies the waiver for Reid Vapor Pressure requirements that is applicable to gasoline blended with 10% ethanol (E10) to gasoline blended with up to 15% ethanol (E15). This change allows gasoline that is blended with 10% to 15% ethanol to be sold year-round.</p><p>Currently, states may be excluded from the waiver for Reid Vapor Pressure requirements by submitting documentation supporting that the waiver would increase air pollution. The bill nullifies existing state exclusions, but states may submit documentation after enactment of the bill to be excluded going forward.</p><p>The bill also modifies the Renewable Fuel Standard Program, which requires transportation fuel sold or introduced into commerce in the United States to contain minimum volumes of renewable fuel. Under the existing program, obligated parties, such as small refineries, must satisfy the volume obligations by either blending renewable fuels into their gasoline or diesel fuel products or by acquiring credits that represent the required renewable fuel volume. The bill directs the Environmental Protection Agency to return compliance credits to small refineries under certain circumstances.</p>"
        },
        "title": "Nationwide Consumer and Fuel Retailer Choice Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s593.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nationwide Consumer and Fuel Retailer Choice Act of 2025</strong></p><p>This bill amends the Clean Air Act to address the limitations on Reid Vapor Pressure (a measure of gasoline's volatility) that are placed on gasoline during the summer ozone season. Specifically, the bill applies the waiver for Reid Vapor Pressure requirements that is applicable to gasoline blended with 10% ethanol (E10) to gasoline blended with up to 15% ethanol (E15). This change allows gasoline that is blended with 10% to 15% ethanol to be sold year-round.</p><p>Currently, states may be excluded from the waiver for Reid Vapor Pressure requirements by submitting documentation supporting that the waiver would increase air pollution. The bill nullifies existing state exclusions, but states may submit documentation after enactment of the bill to be excluded going forward.</p><p>The bill also modifies the Renewable Fuel Standard Program, which requires transportation fuel sold or introduced into commerce in the United States to contain minimum volumes of renewable fuel. Under the existing program, obligated parties, such as small refineries, must satisfy the volume obligations by either blending renewable fuels into their gasoline or diesel fuel products or by acquiring credits that represent the required renewable fuel volume. The bill directs the Environmental Protection Agency to return compliance credits to small refineries under certain circumstances.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s593"
    },
    "title": "Nationwide Consumer and Fuel Retailer Choice Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nationwide Consumer and Fuel Retailer Choice Act of 2025</strong></p><p>This bill amends the Clean Air Act to address the limitations on Reid Vapor Pressure (a measure of gasoline's volatility) that are placed on gasoline during the summer ozone season. Specifically, the bill applies the waiver for Reid Vapor Pressure requirements that is applicable to gasoline blended with 10% ethanol (E10) to gasoline blended with up to 15% ethanol (E15). This change allows gasoline that is blended with 10% to 15% ethanol to be sold year-round.</p><p>Currently, states may be excluded from the waiver for Reid Vapor Pressure requirements by submitting documentation supporting that the waiver would increase air pollution. The bill nullifies existing state exclusions, but states may submit documentation after enactment of the bill to be excluded going forward.</p><p>The bill also modifies the Renewable Fuel Standard Program, which requires transportation fuel sold or introduced into commerce in the United States to contain minimum volumes of renewable fuel. Under the existing program, obligated parties, such as small refineries, must satisfy the volume obligations by either blending renewable fuels into their gasoline or diesel fuel products or by acquiring credits that represent the required renewable fuel volume. The bill directs the Environmental Protection Agency to return compliance credits to small refineries under certain circumstances.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s593"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s593is.xml"
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
      "title": "Nationwide Consumer and Fuel Retailer Choice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nationwide Consumer and Fuel Retailer Choice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Clean Air Act to modify Reid Vapor Pressure requirements and to provide for the return of certain retired credits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:48Z"
    }
  ]
}
```
