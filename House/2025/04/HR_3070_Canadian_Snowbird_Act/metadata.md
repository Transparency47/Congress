# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3070?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3070
- Title: Canadian Snowbird Act
- Congress: 119
- Bill type: HR
- Bill number: 3070
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2026-04-29T08:07:12Z
- Update date including text: 2026-04-29T08:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3070",
    "number": "3070",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Canadian Snowbird Act",
    "type": "HR",
    "updateDate": "2026-04-29T08:07:12Z",
    "updateDateIncludingText": "2026-04-29T08:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:04:35Z",
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
          "date": "2025-04-29T14:04:30Z",
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
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "AZ"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NV"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "AZ"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "AZ"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
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
      "sponsorshipDate": "2025-05-19",
      "state": "FL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "VT"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NV"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "FL"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "NC"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "FL"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3070ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3070\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Ms. Lee of Florida (for herself, Ms. Stefanik , Mr. Stanton , Mr. Morelle , Mr. Amodei of Nevada , Mr. Bean of Florida , Mr. Bergman , Ms. Salazar , Mr. Carter of Georgia , Ms. Wasserman Schultz , Mr. Ciscomani , Mr. Rutherford , and Mr. Calvert ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Immigration and Nationality Act to authorize admission of Canadian retirees as long-term visitors for pleasure described in section 101(a)(15)(B) of such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Canadian Snowbird Act .\n#### 2. Admission of Canadian retirees\nSection 214 of the Immigration and Nationality Act ( 8 U.S.C. 1184 ) is amended by adding at the end the following:\n(s) Canadian retirees (1) In general The Secretary of Homeland Security may admit an alien as a visitor described in section 101(a)(15)(B) if the alien demonstrates, to the satisfaction of the Secretary, that the alien\u2014 (A) is a citizen of Canada; (B) is at least 50 years of age; (C) maintains a residence in Canada; (D) owns a residence in the United States or has signed a rental agreement for accommodations in the United States for the duration of the alien\u2019s stay in the United States; (E) is not inadmissible under section 212; (F) is not described in any ground of deportability under section 237; (G) will not engage in employment or labor for hire in the United States other than employment or labor for hire for a person or entity not based in the United States by whom the Canadian citizen was employed in Canada or for whom the Canadian citizen performed services in Canada; and (H) will not seek any form of assistance or benefit described in section 403(a) of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1613(a) ). (2) Spouse The spouse of an alien described in paragraph (1) may be admitted under the same terms as the principal alien if the spouse satisfies the requirements of paragraph (1), other than subparagraph (D). (3) Immigrant intent In determining eligibility for admission under this subsection, maintenance of a residence in the United States shall not be considered evidence of intent by the alien to abandon the alien\u2019s residence in Canada. (4) Period of admission During any single 365-day period, an alien may be admitted as a visitor for pleasure described in section 101(a)(15)(B) pursuant to this subsection for a period not to exceed 240 days, beginning on the date of admission. Time spent outside of the United States during such period of admission shall not be counted for purposes of determining the termination date of such period. .\n#### 3. Nonresident alien tax status\nSubparagraph (B) of section 7701(b)(1) of the Internal Revenue Code of 1986 is amended by inserting , or, notwithstanding subparagraph (A)(ii), is a Canadian citizen described in section 214(s) of the Immigration and Nationality Act ( 8 U.S.C. 1184(s) ) after (within the meaning of subparagraph (A)) .",
      "versionDate": "2025-04-29",
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
        "name": "Immigration",
        "updateDate": "2025-05-22T13:07:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-29",
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
          "measure-id": "id119hr3070",
          "measure-number": "3070",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-29",
          "originChamber": "HOUSE",
          "update-date": "2026-03-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3070v00",
            "update-date": "2026-03-09"
          },
          "action-date": "2025-04-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Canadian Snowbird Act</strong></p><p>This bill authorizes the Department of Homeland Security to admit into the United States qualifying Canadian citizens as long-term nonimmigrant visitors.</p><p>A qualifying Canadian citizen is an individual who (1) is at least 50 years old, (2) maintains a Canadian residence, (3) owns a U.S. residence or has rented a U.S. accommodation for the duration of the individual's stay, (4) is not inadmissible or deportable, (5) will not engage in employment or labor for hire in the United States other than for a non-U.S.-based person or entity by whom the Canadian citizen was employed in Canada or for whom the Canadian citizen performed services in Canada, and (6) will not seek certain forms of assistance or benefits. A qualified individual may be admitted for up to 240 days during any single 365-day period.</p><p>The spouse of such an individual may be admitted under the same terms, except that the spouse is not required to separately satisfy the requirement for owning or renting a residence in the United States.</p><p>An individual admitted into the United States under this bill shall have nonresident alien tax status.</p>"
        },
        "title": "Canadian Snowbird Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3070.xml",
    "summary": {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Canadian Snowbird Act</strong></p><p>This bill authorizes the Department of Homeland Security to admit into the United States qualifying Canadian citizens as long-term nonimmigrant visitors.</p><p>A qualifying Canadian citizen is an individual who (1) is at least 50 years old, (2) maintains a Canadian residence, (3) owns a U.S. residence or has rented a U.S. accommodation for the duration of the individual's stay, (4) is not inadmissible or deportable, (5) will not engage in employment or labor for hire in the United States other than for a non-U.S.-based person or entity by whom the Canadian citizen was employed in Canada or for whom the Canadian citizen performed services in Canada, and (6) will not seek certain forms of assistance or benefits. A qualified individual may be admitted for up to 240 days during any single 365-day period.</p><p>The spouse of such an individual may be admitted under the same terms, except that the spouse is not required to separately satisfy the requirement for owning or renting a residence in the United States.</p><p>An individual admitted into the United States under this bill shall have nonresident alien tax status.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr3070"
    },
    "title": "Canadian Snowbird Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Canadian Snowbird Act</strong></p><p>This bill authorizes the Department of Homeland Security to admit into the United States qualifying Canadian citizens as long-term nonimmigrant visitors.</p><p>A qualifying Canadian citizen is an individual who (1) is at least 50 years old, (2) maintains a Canadian residence, (3) owns a U.S. residence or has rented a U.S. accommodation for the duration of the individual's stay, (4) is not inadmissible or deportable, (5) will not engage in employment or labor for hire in the United States other than for a non-U.S.-based person or entity by whom the Canadian citizen was employed in Canada or for whom the Canadian citizen performed services in Canada, and (6) will not seek certain forms of assistance or benefits. A qualified individual may be admitted for up to 240 days during any single 365-day period.</p><p>The spouse of such an individual may be admitted under the same terms, except that the spouse is not required to separately satisfy the requirement for owning or renting a residence in the United States.</p><p>An individual admitted into the United States under this bill shall have nonresident alien tax status.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr3070"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3070ih.xml"
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
      "title": "Canadian Snowbird Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Canadian Snowbird Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to authorize admission of Canadian retirees as long-term visitors for pleasure described in section 101(a)(15)(B) of such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:32Z"
    }
  ]
}
```
