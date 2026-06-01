# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2672?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2672
- Title: Religious Workforce Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2672
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-02-19T19:41:25Z
- Update date including text: 2026-02-19T19:41:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2672",
    "number": "2672",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Religious Workforce Protection Act",
    "type": "HR",
    "updateDate": "2026-02-19T19:41:25Z",
    "updateDateIncludingText": "2026-02-19T19:41:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
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
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:03:35Z",
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
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "KS"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "IL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "VA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MI"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NY"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "GA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "MS"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "ID"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "GA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "TN"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "WA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "GA"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "ID"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IN"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MN"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "MN"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "WI"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "CO"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "UT"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2672ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2672\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Carey (for himself, Mr. Neal , Ms. Salazar , and Mr. Stauber ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the continuation of lawful nonimmigrant status for certain religious workers affected by the backlog for religious worker immigrant visas.\n#### 1. Short title\nThis Act may be cited as the Religious Workforce Protection Act .\n#### 2. Extension of nonimmigrant status for religious workers caught in long backlogs for lawful permanent residence\n##### (a) In general\nSection 214(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1184(a)(2) ) is amended by adding at the end the following:\n(C) Notwithstanding section 101(a)(15)(R)(ii), an alien may apply for, and the Secretary of Homeland Security may grant, an extension of nonimmigrant status under section 101(a)(15)(R) until such alien\u2019s application for adjustment of status or an immigrant visa has been processed and a decision has been made on such application if the alien\u2014 (i) is the principal or derivative beneficiary of an immigrant petition filed pursuant to section 204(a) for a preference status under section 203(b)(4); and (ii) is eligible to be granted such immigrant status absent the application of the numerical limitations under sections 201, 202, and 203. .\n##### (b) Conforming amendment\nSection 101(a)(15)(R)(ii) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(R)(ii) ) is amended by inserting , except as provided in section 214(a)(2)(C), after 5 years .\n#### 3. Limited job flexibility for certain religious workers with long-delayed applications for lawful permanent residence\nSection 204(j) of the Immigration and Nationality Act ( 8 U.S.C. 1154(j) ) is amended by striking subsection (a)(1)(D) and inserting subsection (a)(1)(F) or subsection (a)(1)(G)(i) (with respect to special immigrants described in section 101(a)(27)(C)) .\n#### 4. Exemption to 1-year foreign residence requirement for certain nonimmigrant religious workers\nAn alien described in section 214(a)(2)(C) of the Immigration and Nationality Act, as added by section 2(a), who departed from the United States due to the 5-year limitation on nonimmigrant status under section 101(a)(15)(R) of such Act ( 8 U.S.C. 1101(a)(15)(R) ) shall be exempt from the 1-year foreign residence requirement set forth in section 214.2(r)(6) of title 8, Code of Federal Regulations.",
      "versionDate": "2025-04-07",
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
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1298",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Religious Workforce Protection Act",
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
        "updateDate": "2025-05-05T13:20:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2672",
          "measure-number": "2672",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2672v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Religious Workforce Protection Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) to extend the nonimmigrant visa status of certain religious workers.</p><p>Under current law, if specified conditions are met, nonimmigrant religious workers may receive a visa for a period not to exceed five years. The bill allows\u00a0DHS to grant an extension until the individual\u2019s application for adjustment of status to permanent resident or an immigrant visa has been processed and a decision has been made. To be eligible for the extension, the individual must be (1) the beneficiary of a certain type of immigrant petition, and (2) eligible for such immigrant status\u00a0absent the application of certain numerical limitations.</p><p>Such individuals who have pending adjustment of status applications are also granted certain job\u00a0flexibilities, such as the ability to change employers. Individuals who have previously departed the U.S. due to the expiration of their visa are exempt from the one-year foreign residence requirement to renew their visa.</p>"
        },
        "title": "Religious Workforce Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2672.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Religious Workforce Protection Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) to extend the nonimmigrant visa status of certain religious workers.</p><p>Under current law, if specified conditions are met, nonimmigrant religious workers may receive a visa for a period not to exceed five years. The bill allows\u00a0DHS to grant an extension until the individual\u2019s application for adjustment of status to permanent resident or an immigrant visa has been processed and a decision has been made. To be eligible for the extension, the individual must be (1) the beneficiary of a certain type of immigrant petition, and (2) eligible for such immigrant status\u00a0absent the application of certain numerical limitations.</p><p>Such individuals who have pending adjustment of status applications are also granted certain job\u00a0flexibilities, such as the ability to change employers. Individuals who have previously departed the U.S. due to the expiration of their visa are exempt from the one-year foreign residence requirement to renew their visa.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr2672"
    },
    "title": "Religious Workforce Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Religious Workforce Protection Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) to extend the nonimmigrant visa status of certain religious workers.</p><p>Under current law, if specified conditions are met, nonimmigrant religious workers may receive a visa for a period not to exceed five years. The bill allows\u00a0DHS to grant an extension until the individual\u2019s application for adjustment of status to permanent resident or an immigrant visa has been processed and a decision has been made. To be eligible for the extension, the individual must be (1) the beneficiary of a certain type of immigrant petition, and (2) eligible for such immigrant status\u00a0absent the application of certain numerical limitations.</p><p>Such individuals who have pending adjustment of status applications are also granted certain job\u00a0flexibilities, such as the ability to change employers. Individuals who have previously departed the U.S. due to the expiration of their visa are exempt from the one-year foreign residence requirement to renew their visa.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr2672"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2672ih.xml"
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
      "title": "Religious Workforce Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Religious Workforce Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the continuation of lawful nonimmigrant status for certain religious workers affected by the backlog for religious worker immigrant visas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T05:18:38Z"
    }
  ]
}
```
